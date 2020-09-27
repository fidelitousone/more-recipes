import requests
import json
import random

def search_recipe(spoonacular_api, query):
    """
    Request a search from spoonacular's API regarding a recipe
    
    
    Parameters:
    spoonacular_api (string): Spoonacular API Key
    query (string): Search terms for recipe
    
    Returns:
    string: recipe id
    None: if no results were found based on query
    
    """
    payload = {
        "apiKey": spoonacular_api,
        "query": query
    }
    url = "https://api.spoonacular.com/recipes/complexSearch"
    search_result = requests.get(url, params=payload)
    search_result_json = search_result.json()
    
            
    try:
        resultant = random.choice(search_result_json["results"])
        return resultant["id"]
    except IndexError:
        return None


def food_information(spoonacular_api, recipe_id):
    """
    Request recipe information from Spoonacular's API
    
    
    Parameters:
    spoonacular_api (string): Spoonacular API Key
    recipe_id (int): Spoonacular recipe ID
    
    Returns:
    json: json with recipe information
    None: If recipe search query gets no results
    
    """
    payload = {
        "apiKey": spoonacular_api,
        "includeNutrition": "false"
    }
    if recipe_id is None or not type(recipe_id):
        return None
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    spoonacular_food_data = requests.get(url, params=payload)
    food_data_json = spoonacular_food_data.json()
    
    return food_data_json
    

def parse_food_information(food_json):
    """
    Parses relevant json information from spoonacular json
    
    
    Parameters:
    food_json (json): Spoonacular json data
    
    Returns:
    tuple: with indices to title, servinmgs, image, and prep time.
    """
    
    if food_json is None:
        return ("No Recipe Data Found for this food :(", "", "", "")
    
    try:
        dataaa = json.dumps(food_json)
        data = json.loads(dataaa)
    except ValueError:
        return ("No Recipe Data Found for this food :(", "", "", "")
        
        
    ingredients_list = []
    
    if "extendedIngredients" not in data:
        return ("No Recipe Data Found for this food :(", "", "", "")
    
    for item in data["extendedIngredients"]:
        ingredients_list.append(item["originalString"])
    
    
    return (
        data["title"],
        data["servings"],
        data["image"],
        #prep time
        data["readyInMinutes"],
        ingredients_list,
        data["sourceUrl"]
    )
    
