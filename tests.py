import unittest
from unittest import mock
from spoonacular_utils import *

class TestSpoonacularMethods(unittest.TestCase):
    
    fake_json_good = {'results': [{'id': 638871, 'title': 'Chocolate Cake with Coffee Marscarpone Icing', 'image': 'https://spoonacular.com/recipeImages/638871-312x231.jpg', 'imageType': 'jpg'}], 'offset': 0, 'number': 1, 'totalResults': 77}
    fake_json_bad = {}
    empty_spoonacular_resp = {'results': [], 'offset': 0, 'number': 1, 'totalResults': 0}
    
    @mock.patch("requests.Response.json", return_value=fake_json_good)
    def test_good_search(self, mock_check):
        result = search_recipe(mock_check, "Chocolate Cake")
        self.assertEqual(638871, result)
    
    @mock.patch("requests.Response.json", return_value=empty_spoonacular_resp)
    # No Results from spoonacular
    def test_bad_search(self, mock_check):
        result = search_recipe(mock_check, "Chocolate Cake")
        self.assertIsNone(result)
    
    
if __name__ == '__main__':
    unittest.main()