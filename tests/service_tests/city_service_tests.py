import unittest
from unittest.mock import patch, MagicMock
from services.model_services import city_service as cs

class TestCityService(unittest.TestCase):
    def setUp(self):
        self.city = MagicMock()
        self.city.slots = 3
        self.city.pop = 13
        self.building1 = MagicMock()
        self.building1.name = 'Lumberjack'
        self.building2 = MagicMock()
        self.building2.name = 'Mine'
        self.city.buildings = [self.building1, self.building2]

    @patch("builtins.print")
    def test_show_building_slots(self, mock_print):
        cs.show_building_slots(self.city)
        mock_print.assert_called_once_with(3)

    @patch("builtins.print")
    def test_show_building_pop(self, mock_print):
        cs.show_pop(self.city)
        mock_print.assert_called_once_with(13)

    @patch("builtins.print")
    def test_show_city_buildings(self, mock_print):
        self.city.buildings = "Lumberjack, Market"
        cs.show_city_buildings(self.city)
        mock_print.assert_called_once_with( "Lumberjack, Market" )
        self.city.buildings = []

    @patch("builtins.input", return_value="Lumberjack")
    def test_add_building_no_free_slots(self,mock_input):
        from models.custom_error import NoFreeSlotsToBuildIn
        self.city.slots = 2
        self.city.buildings = ["Castle", "Barracks"]

        with self.assertRaises(NoFreeSlotsToBuildIn):
            cs.add_building(self.city)

    @patch("builtins.input", return_value="Lumberjack")
    @patch("common.constants.GameEssentials.PLAYER_CHARACTER")
    def test_add_building_no_cash_para(self,mock_player,mock_input):
        from models.custom_error import YokParichok
        mock_player.modifiers = { "gold": 50 }

        with self.assertRaises(YokParichok):
            cs.add_building(self.city)

    @patch("builtins.input", side_effect=["Church"])
    @patch("builtins.print")
    @patch("common.constants.GameEssentials.PLAYER_CHARACTER")
    def test_add_building_success(self, mock_player, mock_print, mock_input):
        mock_player.modifiers = { "gold": 150 }
        cs.add_building(self.city)
        self.assertEqual(len(self.city.buildings), 3)
        self.assertEqual(self.city.buildings[2].name, "Church")
        self.assertEqual(mock_player.modifiers["gold"], 60)

    @patch("builtins.input", side_effect=["Mine"])
    @patch("builtins.print")
    @patch("common.constants.GameEssentials.PLAYER_CHARACTER")
    def test_remove_building_success(self, mock_player, mock_print, mock_input):
        cs.remove_building(self.city)
        self.assertEqual(len(self.city.buildings), 1)
        self.assertNotIn("Mine", self.city.buildings)

    #Addressing this issue -> no test because I don't remember what the logic behind this was
    def test_calc_city_slots(self):
        pass