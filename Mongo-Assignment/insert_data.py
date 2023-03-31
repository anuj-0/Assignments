from bson.son import SON
from pymongo import MongoClient
import json
from load_data import load_data

"""Created a connection using pymongo.MongoClient to connect with MongoDB."""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]


def insert_comment(comment):
    comments = db["comments"]
    comments.insert_one(comment)


def insert_movie(movie):
    movies = db["movies"]
    movies.insert_one(movie)


def insert_theatre(theatre):
    theatres = db["theatres"]
    theatres.insert_one(theatre)


def insert_user(user):
    users = db["users"]
    users.insert_one(user)
