import unittest
from unittest.mock import patch, MagicMock

from services.model_services import building_service as bs
class TestBuildingService(unittest.TestCase):
    def setUp(self):
        self.name = "TestBuilding1"
        self.price = 21
        self.income = 2
        self.build_time = 0

    @patch('models.building.Building')
    def test_create_building(self,MockBuilding):
        created_building = bs.create_building(self.name,self.price,self.income,self.build_time)
        MockBuilding.assert_called_once_with(self.name,self.price,self.income,self.build_time)
        self.assertEqual(created_building, MockBuilding.return_value)

if __name__ == "__main__":
    unittest.main()