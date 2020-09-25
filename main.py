import tweepy
import random
import flask
import os
from dotenv import load_dotenv
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
    
    return (
        food_data_json["title"]
    )
    

def get_food_quote(twitter_api, food_query):
    """
    Retreives a random tweet from a list of 100 tweets based on the food_query
    and gives the tweet text and info about it.
    
    
    Parameters:
    twitter_api (API): twitter api object
    food_query (string): search terms for specific recipe or food
    
    Returns:
    tuple: Tweet text, twitter handle, exact time posted
    
    """
    twitter_query = twitter_api.search(food_query, count=100)
    
    try:
        random_tweet = random.choice(twitter_query)
    except IndexError:
        return ("", "", "", "")

    t = twitter_api.get_status(random_tweet.id, tweet_mode="extended")
    try:
        return (
            t.retweeted_status.full_text, 
            f"{t.retweeted_status.author._json['screen_name']}", 
            t.retweeted_status.created_at
        )
    except AttributeError:
        return (
            t.full_text, 
            f"{t.author._json['screen_name']}", 
            t.created_at
        )


load_dotenv()

api_key = os.environ['CONSUMER_API_KEY']
secret_key = os.environ['CONSUMER_SECRET_KEY']
app_secret_key = os.environ['APP_SECRET']
app_key = os.environ['APP_KEY']
spoonacular_api_key = os.environ['SPOONACULAR_API_KEY']

try:
    auth = tweepy.OAuthHandler(api_key, secret_key)
    auth.set_access_token(app_secret_key, app_key)
except tweepy.TweepError:
    print("Tweepy Error, check API keys!")
    exit(1)


api = tweepy.API(auth)
app = flask.Flask(__name__)

@app.route("/")
def index():
    random_foods = [
        "ras malai",
        "jian bing",
        "chocolate cake",
        "aloo paratha",
        "vanilla ice cream",
        "tonkatsu",
        "rarebit"
        ]
    queried_food = random.choice(random_foods)
    quote = get_food_quote(api, queried_food)
    spoon = food_information(spoonacular_api_key, queried_food)
    return flask.render_template(
        "index.html",
        content = quote[0],
        author = quote[1],
        at = quote[2],
        queried_food=spoon
    )

if (__name__ == "__main__"):
    app.run (
        debug=True,
        port=int(os.getenv('PORT', 8080)),
        host=os.getenv('IP', '0.0.0.0')
    )