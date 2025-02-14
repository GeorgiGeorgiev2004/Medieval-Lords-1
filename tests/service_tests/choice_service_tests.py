import unittest
from unittest.mock import patch, MagicMock
from services.model_services import choice_service as cs
from configuration.character_configuration import generateAdministrator, generateFighter

class TestChoiceService(unittest.TestCase):
    def setUp(self):
        self.char1 = generateAdministrator()
        self.char2 = generateFighter()

        self.choice = MagicMock()
        self.choice.text = 'Choice1'
        self.choice.consequences = {'gold': +50}
        self.choice.return_value = 'gold'
        self.choice.other_char = None

        self.choice1 = MagicMock()
        self.choice1.text = 'Choice2'
        self.choice1.consequences = {'gold': +50}
        self.choice1.return_value = 'gold'
        self.choice1.other_char = self.char2

        self.choice2 = MagicMock()
        self.choice2.text = 'Choice3'
        self.choice2.return_value = 'Liliacs'
        self.choice2.consequences = {'Liliacs': 321}
        self.choice2.other_char = None

        self.event = MagicMock()
        self.event.text = "event"
        self.event.choices = [self.choice, self.choice1, self.choice2]

    @patch("services.model_services.character_service.handle_modifiers")
    def test_handle_choice_works_correctly(self, mock_handle_modifiers):
        cs.handle_choice(self.char1, self.event, 0)
        mock_handle_modifiers.assert_called_once_with(self.char1,self.choice.return_value, 50)

    @patch("services.model_services.character_service.handle_modifiers")
    def test_handle_choice_other_char_works_correctly(self, mock_handle_modifiers):
        cs.handle_choice(self.char1, self.event, 1)
        mock_handle_modifiers.assert_called_once_with(self.char2, self.choice1.return_value, 50)

    @patch("builtins.print")
    def test_handle_choice_breaks_correctly(self, mock_print):
        cs.handle_choice(self.char1, self.event, 2)
        mock_print.assert_called_with("Lord we lack knowledge of: Liliacs")

    @patch("builtins.input", return_value="Not found answer")
    def test_pick_a_choice_breaks_correctly(self, mock_input):
        from models.custom_error import BadAnswerError
        with self.assertRaises(BadAnswerError):
            cs.pick_a_choice(self.char1, self.event)

    @patch("builtins.input", return_value="Choice1")
    @patch("services.model_services.choice_service.handle_choice")
    def test_pick_a_choice_valid_input(self, mock_handle_choice,mock_input):
        cs.pick_a_choice(self.char1, self.event)
        mock_handle_choice.assert_called_once_with(self.char1, self.event,0) #choice1 has id of 0

if __name__ == "__main__":
    unittest.main()