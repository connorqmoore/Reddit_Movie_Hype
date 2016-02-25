import json
import requests
import praw
import pprint
from collections import Counter
import pickle

# cache these for dev purposes
# pickle?
r = praw.Reddit(user_agent='reddit_hype')
deadpool = r.search('deadpool')
subreddits = Counter()
for x in range(10):
	entry = next(deadpool)
	subreddit = entry.subreddit
	subreddits[subreddit] += 1


with open( "pickled/saved_queries.p", "wb" ) as f:
	pickle.dump(subreddits, f)

print('Pickled')