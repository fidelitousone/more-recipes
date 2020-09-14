import tweepy
import json
import random    

def get_secrets():
    secret_api_information = []
    try:
        with open(".env") as f:
            for line in f:
                secret_api_information.append(line.strip())
        return secret_api_information
    except FileNotFoundError:
        print(".env config file wasn't found!")
        exit(1)


def get_food_quote(twitter_api, food_query):
    twitter_query = api.search("chocolate cake", count=100)

    random_tweet = twitter_query[random.randint(0,100)]

    t = api.get_status(random_tweet.id, tweet_mode="extended")
    try:
        return (t.retweeted_status.full_text, f"@{t.retweeted_status.author._json['screen_name']}", t.retweeted_status.created_at)
    except AttributeError:
        return (t.full_text, f"@{t.author._json['screen_name']}", t.created_at)


api_information = get_secrets()

try:
    auth = tweepy.OAuthHandler(api_information[0], api_information[1])
    auth.set_access_token(api_information[2], api_information[3])
except tweepy.TweepError:
    print("Tweepy Error, check API keys!")
    exit(1)

api = tweepy.API(auth)