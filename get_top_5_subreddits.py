import json
import requests
import praw
import pprint
from collections import Counter
import pickle

# cache these for dev purposes
# pickle?
r = praw.Reddit(user_agent='reddit_hype')

with open( "pickled/saved_queries.p", "rb" ) as f:
	subreddits = pickle.load(f)


