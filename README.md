# project1-js843
A simple web app to retrieve recipes and quotes relating to them on Twitter.

## Table of Contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Technical Difficulties](#technical-difficulties)
* [Known Issues](#known-issues)

## Technologies
* Python 3.6.12+
* pip 18.1+
* tweepy 3.9.0+
* Flask 1.1.2+
* python-dotenv 0.14.0+

## Setup
- Clone the repo: `git clone https://github.com/fidelitousone/project1-js843.git`
- `cd` into app directory
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

### Working in the Quota Restraint of the Spoonacular API
The Spoonacular API, with a free account hard enforces a limit of 150
quests at most per day for particular recipes. Therefore, it is not a
luxury that I could have kept refreshing the page repeatedly in order 
to test results without being blocked or repeatedly making new accounts.
In order to bypass this, I decided to unit test my code instead.
By utilizing the unit test library, and using the mock library to simulate
obtaining data from the API itself.

### Working With and Properly Manipulating and Parsing JSON
This should have been the easier part, but this didn't prove to be 
the case. I quickly found out that my app was running into errors
repeatedly due to JSON being returned incorrectly, or just formatted
in completely wrong ways. When I was testing my code, the error I 
encountered the most was that I was trying to access JSON but ended up
accessing string array elements because the JSON wasn't returned correctly.
Eventually, the solution, although, a hacky one was a suggestion from StackOverflow
where I dumped the json and loaded it into a different variable to absolutely ensure
that JSON data was being read and not a dict or a list.

## Known Issues
### Tweet Relevancy
Not every tweet obtained is actually relevant to the actual food. Instead it
might be a retweet to someone talking about that food, lambasting that 
particular food or may just be completely irrelevant altogether because 
its just in their twitter handle. A solution, given more time, would be to 
generate a list of extremely specific search terms about the tweet. Additionally,
another approach would be to implement some kind of machine learning to get
a desired tweet.

### Front End Design Flaws
One of the most obvious flaws in the actual web page design is that it is not
responsive. When changing screen sizes, it quickly breaks. Given more time, 
I could have properly set up a better layout and a design that could
accomdoate different screen sizes. For any recipe that may have more than
20 ingredients for whatever reason runs into severe issues as the list runs
off the div.
