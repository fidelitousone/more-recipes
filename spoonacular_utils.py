import requests
import json


def search_recipe(spoonacular_api, query):
    payload = {
        "apiKey": spoonacular_api,
        "query": query,
        "number": 1
    }
    url = "https://api.spoonacular.com/recipes/complexSearch"
    search_result = requests.get(url, params=payload)
    search_result_json = search_result.json()
    
    try:
        return search_result_json["results"][0]["id"]
    except IndexError:
        return None


def food_information(spoonacular_api, query):
    payload = {
        "apiKey": spoonacular_api,
        "includeNutrition": "false"
    }
    recipe_id = search_recipe(spoonacular_api, query)
    if recipe_id is None:
        return f"Spoonacular couldn't find {query}"
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"
    spoonacular_food_data = requests.get(url, params=payload)
    food_data_json = spoonacular_food_data.json()
    
    return food_data_json
    

def parse_food_information(food_json):
        
    return (
        food_json["title"],
        food_json["servings"],
        food_json["image"],
        #prep time
        food_json["readyInMinutes"]
    )
    
