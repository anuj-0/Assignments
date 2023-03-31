from bson.son import SON
import pymongo
from pymongo import MongoClient
import json
from load_data import load_data
from insert_data import insert_comment, insert_user, insert_movie, insert_theatre
from movies_analysis import *
from comments_analysis import *
from theatre_analysis import *

"""Created a connection using pymongo.MongoClient to connect with MongoDB."""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]

"""Bulk load the JSON files in the individual MongoDB collections. """
# load_data()

"""Python methods and MongoDB queries to insert new comments, 
    movies, theatres, and users into respective MongoDB collections."""

# Comment Analysis
# a
# top_users_by_max_comments()

# b
# top_movies_by_comments()

# c
# total_comments_by_year(2001)


# Movies Analysis
# a
# top_movies_by_imdb_rating(5)
# top_movies_by_imdb_rating_in_given_year(5, 2010)
# top_movies_by_imdb_rating_and_votes(5)
# movies_matching_given_pattern('star', 5)

# b
# top_directors_by_movies(5)
# top_directors_by_movies_in_given_year(5, 2010)
# top_directors_by_movie_in_given_genre(5, 'Action')

# c
# top_actors_by_movie(5)
# top_actors_by_movie_and_given_year(5, 2010)
# top_actors_by_movie_in_given_genre(5,'Action')

# d
# top_movies_by_genre_and_imdb(5)

# Theatre Analysis

# a
# top_cities_by_theatres(5)
# b
top_cities_by_coordinates(37.7749, -122.4194)
