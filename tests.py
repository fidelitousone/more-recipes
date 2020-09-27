import unittest
from unittest import mock
from spoonacular_utils import *
import json

class TestSpoonacularMethods(unittest.TestCase):
    
    fake_json_good = {'results': [{'id': 638871, 'title': 'Chocolate Cake with Coffee Marscarpone Icing', 'image': 'https://spoonacular.com/recipeImages/638871-312x231.jpg', 'imageType': 'jpg'}], 'offset': 0, 'number': 1, 'totalResults': 77}
    fake_json_bad = {}
    empty_spoonacular_resp = {'results': [], 'offset': 0, 'number': 1, 'totalResults': 0}
    
    response_spoon = {
      "aggregateLikes": 1,
      "spoonacularScore": 32,
      "healthScore": 4,
      "creditsText": "Foodista.com – The Cooking Encyclopedia Everyone Can Edit",
      "license": "CC BY 3.0",
      "sourceName": "Foodista",
      "pricePerServing": 122.65,
      "extendedIngredients": [
        {
          "id": 1053,
          "aisle": "Milk, Eggs, Other Dairy",
          "image": "fluid-cream.jpg",
          "consistency": "liquid",
          "name": "heavy cream",
          "original": "1 1/2 cups heavy cream",
          "originalString": "1 1/2 cups heavy cream",
          "originalName": "heavy cream",
          "amount": 1.5,
          "unit": "cups",
          "meta": [],
          "metaInformation": [],
          "measures": {
            "us": {
              "amount": 1.5,
              "unitShort": "cups",
              "unitLong": "cups"
            },
            "metric": {
              "amount": 354.882,
              "unitShort": "ml",
              "unitLong": "milliliters"
            }
          }
        },
        {
          "id": 1077,
          "aisle": "Milk, Eggs, Other Dairy",
          "image": "milk.png",
          "consistency": "liquid",
          "name": "whole milk",
          "original": "1 cup whole milk",
          "originalString": "1 cup whole milk",
          "originalName": "whole milk",
          "amount": 1,
          "unit": "cup",
          "meta": [
            "whole"
          ],
          "metaInformation": [
            "whole"
          ],
          "measures": {
            "us": {
              "amount": 1,
              "unitShort": "cup",
              "unitLong": "cup"
            },
            "metric": {
              "amount": 236.588,
              "unitShort": "ml",
              "unitLong": "milliliters"
            }
          }
        },
        {
          "id": 19335,
          "aisle": "Baking",
          "image": "sugar-in-bowl.png",
          "consistency": "solid",
          "name": "sugar",
          "original": "1/2 cup sugar",
          "originalString": "1/2 cup sugar",
          "originalName": "sugar",
          "amount": 0.5,
          "unit": "cup",
          "meta": [],
          "metaInformation": [],
          "measures": {
            "us": {
              "amount": 0.5,
              "unitShort": "cups",
              "unitLong": "cups"
            },
            "metric": {
              "amount": 118.294,
              "unitShort": "ml",
              "unitLong": "milliliters"
            }
          }
        },
        {
          "id": 1082047,
          "aisle": "Spices and Seasonings",
          "image": "salt.jpg",
          "consistency": "solid",
          "name": "kosher salt",
          "original": "Pinch of kosher salt",
          "originalString": "Pinch of kosher salt",
          "originalName": "Pinch of kosher salt",
          "amount": 1,
          "unit": "pinch",
          "meta": [],
          "metaInformation": [],
          "measures": {
            "us": {
              "amount": 1,
              "unitShort": "pinch",
              "unitLong": "pinch"
            },
            "metric": {
              "amount": 1,
              "unitShort": "pinch",
              "unitLong": "pinch"
            }
          }
        },
        {
          "id": 2050,
          "aisle": "Baking",
          "image": "vanilla-extract.jpg",
          "consistency": "liquid",
          "name": "vanilla extract",
          "original": "1 vanilla bean or 1 teaspoon vanilla extract",
          "originalString": "1 vanilla bean or 1 teaspoon vanilla extract",
          "originalName": "vanilla bean or 1 teaspoon vanilla extract",
          "amount": 1,
          "unit": "",
          "meta": [],
          "metaInformation": [],
          "measures": {
            "us": {
              "amount": 1,
              "unitShort": "",
              "unitLong": ""
            },
            "metric": {
              "amount": 1,
              "unitShort": "",
              "unitLong": ""
            }
          }
        },
        {
          "id": 1125,
          "aisle": "Milk, Eggs, Other Dairy",
          "image": "egg-yolk.jpg",
          "consistency": "solid",
          "name": "egg yolks",
          "original": "5 egg yolks",
          "originalString": "5 egg yolks",
          "originalName": "egg yolks",
          "amount": 5,
          "unit": "",
          "meta": [],
          "metaInformation": [],
          "measures": {
            "us": {
              "amount": 5,
              "unitShort": "",
              "unitLong": ""
            },
            "metric": {
              "amount": 5,
              "unitShort": "",
              "unitLong": ""
            }
          }
        }
      ],
      "id": 663880,
      "title": "True vanilla ice cream",
      "readyInMinutes": 45,
      "servings": 3,
      "sourceUrl": "https://www.foodista.com/recipe/ZP3JT33Z/true-vanilla-ice-cream",
      "image": "https://spoonacular.com/recipeImages/663880-556x370.jpg",
      "imageType": "jpg",
      "summary": "True vanillan ice cream is a dessert that serves 3. For <b>$1.23 per serving</b>, this recipe <b>covers 12%</b> of your daily requirements of vitamins and minerals. Watching your figure? This gluten free and lacto ovo vegetarian recipe has <b>687 calories</b>, <b>10g of protein</b>, and <b>55g of fat</b> per serving. 1 person found this recipe to be yummy and satisfying. <b>Summer</b> will be even more special with this recipe. A mixture of teaspoon vanillan extract, milk, sugar, and a handful of other ingredients are all it takes to make this recipe so yummy. From preparation to the plate, this recipe takes approximately <b>approximately 45 minutes</b>. It is brought to you by Foodista. Overall, this recipe earns a <b>rather bad spoonacular score of 30%</b>. Similar recipes are <a href=\"https://spoonacular.com/recipes/true-vanilla-ice-cream-186641\">True Vanillan Ice Cream</a>, <a href=\"https://spoonacular.com/recipes/true-mint-ice-cream-512098\">True Mint Ice Cream</a>, and <a href=\"https://spoonacular.com/recipes/vanilla-ice-cream-plus-a-coffee-and-vanilla-ice-cream-dessert-521655\">Vanillan ice cream (plus a coffee and vanillan ice cream dessert)</a>.",
      "cuisines": [],
      "dishTypes": [
        "dessert"
      ],
      "diets": [
        "gluten free",
        "lacto ovo vegetarian"
      ],
      "occasions": [
        "summer"
      ],
      "winePairing": {
        "pairedWines": [
          "cream sherry",
          "moscato dasti",
          "port"
        ],
        "pairingText": "Vanillan Ice Cream works really well with Cream Sherry, Moscato d'Asti, and Port. A common wine pairing rule is to make sure your wine is sweeter than your food. Delicate desserts go well with Moscato d'Asti, nutty desserts with cream sherry, and caramel or chocolate desserts pair well with port. You could try NV Solera Cream Sherry. Reviewers quite like it with a 4.5 out of 5 star rating and a price of about 17 dollars per bottle.",
        "productMatches": [
          {
            "id": 428475,
            "title": "NV Solera Cream Sherry",
            "description": "The Solera Cream Sherry has a brilliant amber and deep copper hue. With butterscotch and pecan aromas, the sweet salted nut and brown spice aromas carry a complex caramel accent. A sweet entry leads to a rounded, lush, moderately full-bodied palate with a lengthy, flavorful finish.",
            "price": "$16.99",
            "imageUrl": "https://spoonacular.com/productImages/428475-312x231.jpg",
            "averageRating": 0.9,
            "ratingCount": 4,
            "score": 0.823076923076923,
            "link": "https://www.amazon.com/NV-Solera-Cream-Sherry-750/dp/B00HSME8OW?tag=spoonacular-20"
          }
        ]
      },
      "instructions": "Combine heavy cream, whole milk, 1/4 cup sugar and salt in a medium saucepan. Split vanilla bean lengthwise and scrape in seeds; add pod (or use 1 teaspoon vanilla extract). Bring mixture just to a simmer, stirring to dissolve sugar. Remove from heat. If using vanilla bean, cover; let sit 30 minutes.\nWhisk 5 large egg yolks and 1/4 cup sugar in a medium bowl until pale, about 2 minutes. Gradually whisk in 1/2 cup warm cream mixture. Whisk yolk mixture into remaining cream mixture. Cook over medium heat, stirring constantly, until thick enough to coat a wooden spoon, 2 to 3 minutes.\nStrain custard into a medium bowl set over a bowl of ice water; let cool, stirring occasionally. At this point, you can transfer the mixture to a bowl and cover it by putting plastic wrap directly on the top of the custard. It can cool overnight in the fridge and processed in the morning.\nProcess custard in an ice cream maker according to manufacturers instructions. Transfer to an airtight container; cover. Freeze until firm, at least 4 hours and up to 1 week.",
      "analyzedInstructions": [
        {
          "name": "",
          "steps": [
            {
              "number": 1,
              "step": "Combine heavy cream, whole milk, 1/4 cup sugar and salt in a medium saucepan. Split vanilla bean lengthwise and scrape in seeds; add pod (or use 1 teaspoon vanilla extract). Bring mixture just to a simmer, stirring to dissolve sugar.",
              "ingredients": [
                {
                  "id": 2050,
                  "name": "vanilla extract",
                  "localizedName": "vanilla extract",
                  "image": "vanilla-extract.jpg"
                },
                {
                  "id": 93622,
                  "name": "vanilla bean",
                  "localizedName": "vanilla bean",
                  "image": "vanilla.jpg"
                },
                {
                  "id": 1053,
                  "name": "heavy cream",
                  "localizedName": "heavy cream",
                  "image": "fluid-cream.jpg"
                },
                {
                  "id": 1077,
                  "name": "whole milk",
                  "localizedName": "whole milk",
                  "image": "milk.png"
                },
                {
                  "id": 93818,
                  "name": "seeds",
                  "localizedName": "seeds",
                  "image": "sunflower-seeds.jpg"
                },
                {
                  "id": 19335,
                  "name": "sugar",
                  "localizedName": "sugar",
                  "image": "sugar-in-bowl.png"
                },
                {
                  "id": 2047,
                  "name": "salt",
                  "localizedName": "salt",
                  "image": "salt.jpg"
                }
              ],
              "equipment": [
                {
                  "id": 404669,
                  "name": "sauce pan",
                  "localizedName": "sauce pan",
                  "image": "sauce-pan.jpg"
                }
              ]
            },
            {
              "number": 2,
              "step": "Remove from heat. If using vanilla bean, cover; let sit 30 minutes.",
              "ingredients": [
                {
                  "id": 93622,
                  "name": "vanilla bean",
                  "localizedName": "vanilla bean",
                  "image": "vanilla.jpg"
                }
              ],
              "equipment": [],
              "length": {
                "number": 30,
                "unit": "minutes"
              }
            },
            {
              "number": 3,
              "step": "Whisk 5 large egg yolks and 1/4 cup sugar in a medium bowl until pale, about 2 minutes. Gradually whisk in 1/2 cup warm cream mixture.",
              "ingredients": [
                {
                  "id": 1125,
                  "name": "egg yolk",
                  "localizedName": "egg yolk",
                  "image": "egg-yolk.jpg"
                },
                {
                  "id": 1053,
                  "name": "cream",
                  "localizedName": "cream",
                  "image": "fluid-cream.jpg"
                },
                {
                  "id": 19335,
                  "name": "sugar",
                  "localizedName": "sugar",
                  "image": "sugar-in-bowl.png"
                }
              ],
              "equipment": [
                {
                  "id": 404661,
                  "name": "whisk",
                  "localizedName": "whisk",
                  "image": "whisk.png"
                },
                {
                  "id": 404783,
                  "name": "bowl",
                  "localizedName": "bowl",
                  "image": "bowl.jpg"
                }
              ],
              "length": {
                "number": 2,
                "unit": "minutes"
              }
            },
            {
              "number": 4,
              "step": "Whisk yolk mixture into remaining cream mixture. Cook over medium heat, stirring constantly, until thick enough to coat a wooden spoon, 2 to 3 minutes.",
              "ingredients": [
                {
                  "id": 1053,
                  "name": "cream",
                  "localizedName": "cream",
                  "image": "fluid-cream.jpg"
                },
                {
                  "id": 1125,
                  "name": "egg yolk",
                  "localizedName": "egg yolk",
                  "image": "egg-yolk.jpg"
                }
              ],
              "equipment": [
                {
                  "id": 404732,
                  "name": "wooden spoon",
                  "localizedName": "wooden spoon",
                  "image": "wooden-spoon.jpg"
                },
                {
                  "id": 404661,
                  "name": "whisk",
                  "localizedName": "whisk",
                  "image": "whisk.png"
                }
              ],
              "length": {
                "number": 2,
                "unit": "minutes"
              }
            },
            {
              "number": 5,
              "step": "Strain custard into a medium bowl set over a bowl of ice water; let cool, stirring occasionally. At this point, you can transfer the mixture to a bowl and cover it by putting plastic wrap directly on the top of the custard. It can cool overnight in the fridge and processed in the morning.",
              "ingredients": [
                {
                  "id": 14412,
                  "name": "water",
                  "localizedName": "water",
                  "image": "water.png"
                },
                {
                  "id": 19170,
                  "name": "custard",
                  "localizedName": "custard",
                  "image": "custard.png"
                },
                {
                  "id": 10018364,
                  "name": "wrap",
                  "localizedName": "wrap",
                  "image": "flour-tortilla.jpg"
                }
              ],
              "equipment": [
                {
                  "id": 404730,
                  "name": "plastic wrap",
                  "localizedName": "plastic wrap",
                  "image": "plastic-wrap.jpg"
                },
                {
                  "id": 404783,
                  "name": "bowl",
                  "localizedName": "bowl",
                  "image": "bowl.jpg"
                }
              ]
            },
            {
              "number": 6,
              "step": "Process custard in an ice cream maker according to manufacturers instructions.",
              "ingredients": [
                {
                  "id": 19095,
                  "name": "ice cream",
                  "localizedName": "ice cream",
                  "image": "vanilla-ice-cream.png"
                },
                {
                  "id": 19170,
                  "name": "custard",
                  "localizedName": "custard",
                  "image": "custard.png"
                }
              ],
              "equipment": [
                {
                  "id": 404791,
                  "name": "ice cream machine",
                  "localizedName": "ice cream machine",
                  "image": "ice-cream-machine.jpg"
                }
              ]
            },
            {
              "number": 7,
              "step": "Transfer to an airtight container; cover. Freeze until firm, at least 4 hours and up to 1 week.",
              "ingredients": [],
              "equipment": [],
              "length": {
                "number": 240,
                "unit": "minutes"
              }
            }
          ]
        }
      ],
      "spoonacularSourceUrl": "https://spoonacular.com/true-vanilla-ice-cream-663880"
    }
    
    food_json = json.dumps(response_spoon)
    tester = str(response_spoon)
    correct_ingredients = ["1 1/2 cups heavy cream","1 cup whole milk","1/2 cup sugar","Pinch of kosher salt", "1 vanilla bean or 1 teaspoon vanilla extract", "5 egg yolks"]
    
    @mock.patch("requests.Response.json", return_value=fake_json_good)
    def test_good_search(self, mock_check):
        result = search_recipe(mock_check, "Chocolate Cake")
        self.assertEqual(638871, result)
    
    @mock.patch("requests.Response.json", return_value=empty_spoonacular_resp)
    # No Results from spoonacular
    def test_bad_search(self, mock_check):
        result = search_recipe(mock_check, "Chocolate Cake")
        self.assertIsNone(result)
    
    # Mangled or bad data given to parse
    def test_bad_data_handle_parsefood(self):
        result = parse_food_information("m;cvm;lal")
        self.assertIs(type(result), tuple)
        
    def test_get_recipe_title(self):
        result = parse_food_information(self.response_spoon)
        self.assertEqual(result[0], "True vanilla ice cream")
        
    def test_get_recipe_servings(self):
        result = parse_food_information(self.response_spoon)
        self.assertEqual(result[1], 3)
        
    def test_get_recipe_image(self):
        result = parse_food_information(self.response_spoon)
        self.assertEqual(result[2], "https://spoonacular.com/recipeImages/663880-556x370.jpg")
        
    def test_get_recipe_preptime(self):
        result = parse_food_information(self.response_spoon)
        self.assertEqual(result[3], 45)
        
    def test_get_recipe_ingredients(self):
        result = parse_food_information(self.response_spoon)
        self.assertEqual(result[4][0], "1 1/2 cups heavy cream")
    
    def test_check_recipe_ingredients(self):
      result = parse_food_information(self.response_spoon)
      self.assertCountEqual(result[4], self.correct_ingredients)
      
    def test_check_recipe_url(self):
      result = parse_food_information(self.response_spoon)
      self.assertAlmostEqual(result[5], "https://www.foodista.com/recipe/ZP3JT33Z/true-vanilla-ice-cream")
    
if __name__ == '__main__':
    unittest.main()