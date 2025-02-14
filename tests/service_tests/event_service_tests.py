import unittest
from unittest.mock import patch, MagicMock
from services.model_services import event_service as es

class TestEventService(unittest.TestCase):

    @patch("builtins.print")
    def test_display_event(self, mock_print):
        mock_event = MagicMock()
        mock_event.name = "EventName"
        mock_event.description = "EventDesc"
        mock_choice1 = MagicMock()
        mock_choice1.__str__.return_value = "EventChoice1"
        mock_choice1.text = "Attack"
        mock_choice2 = MagicMock()
        mock_choice2.__str__.return_value = "EventChoice2"
        mock_choice2.text = "Negotiate"
        mock_event.choices = [mock_choice1, mock_choice2]
        es.display_event(mock_event)
        mock_print.assert_any_call("EventName")
        mock_print.assert_any_call("EventDesc")
        mock_print.assert_any_call("EventChoice1")
        mock_print.assert_any_call("EventChoice2")
        self.assertEqual(mock_print.call_count, 4)


