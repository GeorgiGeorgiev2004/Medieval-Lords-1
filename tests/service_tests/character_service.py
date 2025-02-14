import unittest
from unittest.mock import patch, MagicMock
from services.model_services import character_service as cs
from common.constants import Modifiers as ccm
from configuration.character_configuration import generateAdministrator

class TestCharacterService(unittest.TestCase):
    def setUp(self):
        self.char = generateAdministrator()
        self.char2 = generateAdministrator()
    #region handle_modifiers_calls_correct
    @patch("services.model_services.character_service._handle_modifiers_stats")
    def test_handle_modifiers_stats_calls_correctly(self, _handle_modifiers_stats):
        cs.handle_modifiers(self.char, ccm.stats, {"strength": 41})
        _handle_modifiers_stats.assert_called_once_with(self.char, {"strength": 41})

    @patch("services.model_services.character_service._handle_modifiers_numerical")
    def test_handle_modifiers_numerical_calls_correctly(self, _handle_modifiers_numerical):
        cs.handle_modifiers(self.char, ccm.gold, 11)
        _handle_modifiers_numerical.assert_called_once_with(self.char, ccm.gold, 11)

    @patch("services.model_services.character_service._handle_modifiers_trait")
    def test_handle_modifiers_trait_calls_correctly(self, _handle_modifiers_trait):
        cs.handle_modifiers(self.char, ccm.traits, "Insufferable")
        _handle_modifiers_trait.assert_called_once_with(self.char, "Insufferable")

    @patch("services.model_services.character_service._handle_modifiers_title")
    def test_handle_modifiers_title_calls_correctly(self, _handle_modifiers_title):
        cs.handle_modifiers(self.char, ccm.title, "Mesopotamian Farmer")
        _handle_modifiers_title.assert_called_once_with(self.char, "Mesopotamian Farmer")
    #endregion

    #region handler_upadating_values
    def test_handle_modifiers_stats_updates_value(self):
        cs._handle_modifiers_stats(self.char, {ccm.stats_strength: 5})
        self.assertEqual(self.char.modifiers[ccm.stats][ccm.stats_strength], 6)

    def test_handle_modifiers_numerical_updates_value(self):
        cs._handle_modifiers_numerical(self.char, ccm.army_morale, 0.1)
        self.assertAlmostEqual(self.char.modifiers[ccm.army_morale], 0.8)

    @patch("builtins.input", return_value="Y")
    def test_handle_modifiers_traits_updates_value_add(self,mock_input):
        cs._handle_modifiers_trait(self.char, "Brave")
        self.assertIn("Brave", self.char.modifiers[ccm.traits])

    @patch("builtins.input", return_value="N")
    def test_handle_modifiers_traits_updates_value_delete(self, mock_input):
        cs._handle_modifiers_trait(self.char, "Generous")
        self.assertNotIn("Generous", self.char.modifiers[ccm.traits])

    def test_handle_modifiers_title_updates_value(self):
        cs._handle_modifiers_title(self.char, ccm.title, "Warlord of the southern regions")
        self.assertEqual(self.char.modifiers[ccm.title], "Warlord of the southern regions")

    #On another note in the same region testing the modify_stat which was intended as a supporting func in events i think
    def test_modify_stat(self):
        cs.modify_stat(self.char, ccm.stats_knowledge, 2)
        self.assertEqual(self.char.modifiers["stats"][ccm.stats_knowledge], 5)

    #endregion

    #region modifier_calc_time
    def test_calc_morale(self):
        result = cs.calc_morale(self.char2)
        expected_morale = self.char2.modifiers[ccm.army_morale]+(0.025 * self.char2.modifiers[ccm.stats][ccm.stats_strength] +
                           (sum([trait.modifier_value[1] for trait in self.char2.modifiers[ccm.traits] if
                                trait.modif_flag is ccm.stats_strength])))
        self.assertAlmostEqual(result, expected_morale)

    def test_calc_tax_mod(self):
        tax = cs.calc_tax_mod(self.char2)
        expected_tax = self.char2.modifiers[ccm.tax_income_mod]+(0.015 * self.char2.modifiers[ccm.stats][ccm.stats_administrative] +
                        (sum([trait.modifier_value[1] for trait in self.char2.modifiers[ccm.traits] if
                                trait.modif_flag is ccm.stats_administrative])))
        self.assertAlmostEqual(tax, expected_tax)

    def test_calc_upkeep(self):
        upkeep = cs.calc_upkeep(self.char2)
        expected_upkeep = self.char2.modifiers[ccm.upkeep_cost]+(0.015 * self.char2.modifiers[ccm.stats][ccm.stats_tactics] +
                           (sum([trait.modifier_value[1] for trait in self.char2.modifiers[ccm.traits] if
                                trait.modif_flag is ccm.stats_tactics])))
        self.assertAlmostEqual(upkeep, expected_upkeep)
    #endregion

    @patch("builtins.input", return_value="TestChar1")
    @patch("services.model_services.character_service.generate_heroes")
    def test_char_selector_correct(self, mock_generate_heroes, mock_input):
        mock_char = MagicMock()
        mock_char.first_name = "TestChar1"
        mock_generate_heroes.return_value = [mock_char]

        with patch("builtins.print") as mock_print:
            result = cs.char_selector()
            self.assertEqual(result, 1)
            self.assertIn("TestChar1 selected!", mock_print.call_args_list[-1][0][0])# Last print extraction. Any better way?

    @patch("builtins.input", return_value="EvilTwinOfTestChar1") #Evil pronounced -> iivil. https://youtu.be/7jv1Zw5FwRg?t=31 fitting valentine's.
    @patch("services.model_services.character_service.generate_heroes")
    def test_char_selector_incorrect(self, mock_generate_heroes, mock_input):
        mock_char = MagicMock()
        mock_char.first_name = "TestChar1"
        mock_generate_heroes.return_value = [mock_char]

        with patch("builtins.print") as mock_print:
            result = cs.char_selector()
            self.assertIsNone(result)
            self.assertIn("Opsa broski try again maybe?", mock_print.call_args_list[-1][0][0])

if __name__ == "__main__":
    unittest.main()