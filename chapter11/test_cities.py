import unittest
from city_functions import city_functions
class CityTestCase(unittest.TestCase):
    """测试函数city_functions"""
    def test_city_country(self):
        city_country = city_functions("Santiago", "Chile")
        self.assertEqual(city_country, "Santiago, Chile")
    def test_city_population(self):
        city_country = city_functions("Santiago", "Chile", 5000000)
        self.assertEqual(city_country,"Santiago, Chile-population5000000" )
unittest.main()