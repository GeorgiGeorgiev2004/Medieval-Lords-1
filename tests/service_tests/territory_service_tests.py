import unittest
from unittest.mock import patch, MagicMock

from services.model_services import territory_service as t
class TestTerryService(unittest.TestCase):

    def setUp(self):
        self.mock_terry = MagicMock()
        self.mock_terry.city_slots = 3
        self.mock_terry.cities = [MagicMock(name='Ahtopol'), MagicMock(name='Vihren')]

        self.mock_terry.cities[0].__str__.return_value = "Ahtopol"
        self.mock_terry.cities[1].__str__.return_value = "Vihren"



    def test_display_terry(self):
        expected_output = "In your territory that can contain 3 cities the currently avaluable are: Ahtopol, Vihren"
        self.assertEqual(t.display_terry(self.mock_terry), expected_output)

    def test_terry_find_cities(self):
        city_names = [str(city) for city in self.mock_terry.cities]
        city_search_false = "Ah topol"
        city_search_true = "Ahtopol"
        self.assertNotIn(city_search_false, city_names)
        self.assertIn(city_search_true, city_names)

if __name__ == "__main__":
    unittest.main()