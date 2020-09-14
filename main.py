import tweepy
    

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
            
api_information = get_secrets()
print(api_information)

try:
    auth = tweepy.OAuthHandler(api_information[0], api_information[1])
    auth.set_access_token(api_information[2], api_information[3])
except tweepy.TweepError:
    print("Tweepy Error, check API keys!")
    exit(1)

api = tweepy.API(auth)
