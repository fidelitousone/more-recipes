# project1-js843
A simple web app to retrieve recipes and quotes relating to them on Twitter.

## Table of Contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Technical Difficulties](#technical_difficulties)

## Technologies
* Python 3.6.12+
* pip 18.1+
* tweepy 3.9.0+
* Flask 1.1.2+
* python-dotenv 0.14.0

## Setup
- Clone the repo: <code>git clone https://github.com/fidelitousone/project1-js843.git</code>
- <code>cd</code> into app directory
- Install dependencies: <code>pip install flask tweepy python-dotenv</code>
- run `./install.sh`
- Enter corresponding keys
- run `python main.py`

## Technical Difficulties
### Obtaining Tweet Information
One of the things I ran into issues with is actually obtaining the tweet
information. One of the issues being that I was having trouble getting the 
full text from the tweet. Instead, I was getting the shortened tweet. I ended up
finding out that there was a function call specifically designed for obtaining
the full tweet. However, this still didn't get the actual tweet and I would
run into exceptions where that method didn't exist. I found out that search
was actually getting retweets as well which is a different type of object.

My solution ended up being that I checked if a tweet was a retweet or not,
then I'd get the full text of the tweet from that specific object.

### Getting a Random Tweet
I was unsure about how to go about the implementation of obtaining a random
tweet from the search results. However, I figured that just generating a
random number which stands for some index in the list would do. This ran
into some problems as I was getting index errors. Obviously, this was due
to no search results from the query. My second implementation was to just
get the length of the search object and handle a returned empty list.
Finally the last implementation was just to use random.choice() which
essentially avoids one-off errors altogether.