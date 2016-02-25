import json
import requests
from imdbpy import IMDb
import pickle

# cache these for dev purposes
# pickle?
movie_dict = {}
ia = IMDb()


# with open( "pickled/saved_movie_data.p", "wb" ) as f:
# 	pickle.dump(movie_dict, f)