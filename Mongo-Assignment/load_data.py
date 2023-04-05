from pymongo import MongoClient
import json


def load_data():
    """Created a connection using pymongo.MongoClient to connect with MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client["sample_mflix"]

    """Bulk load the JSON files in the individual MongoDB collections. """
    # Define the JSON file paths
    comments_file = "./sample_mflix/comments.json"
    movies_file = "./sample_mflix/movies.json"
    theaters_file = "./sample_mflix/theaters.json"
    users_file = "./sample_mflix/users.json"

    with open(comments_file) as f:
        comments_data = json.load(f)
    db.comments.insert_many(comments_data)

    with open(movies_file) as f:
        movies_data = json.load(f)
    db.movies.insert_many(movies_data)

    with open(theaters_file) as f:
        theaters_data = json.load(f)
    db.theaters.insert_many(theaters_data)

    with open(users_file) as f:
        users_data = json.load(f)
    db.users.insert_many(users_data)

    print("Load Data Successfull!!!")
