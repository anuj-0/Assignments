from pymongo import MongoClient


client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]

"""
    Comments Collection:
        a. Find top 10 users who made the maximum number of comments
        b. Find top 10 movies with most comments
        c. Given a year find the total number of comments created each month in that year
"""


# a
def top_users_by_max_comments():
    top_users = db.comments.aggregate([
        {"$group": {"_id": "$_id", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])

    for user in top_users:
        print("User ID:", user["_id"])
        print("Number of comments:", user["count"])
        print("-----------------------")


# b
def top_movies_by_comments():
    top_movies = db.comments.aggregate([
        {"$group": {"_id": "$movie_id", "count": {"$sum": 1}}},
        {"$lookup": {"from": "movies", "localField": "_id", "foreignField": "_id", "as": "movie"}},
        {"$unwind": "$movie"},
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {"title": "$movie.title", "count": 1}}
    ])

    # Print the results
    for movie in top_movies:
        print("Movie title:", movie["title"])
        print("Number of comments:", movie["count"])
        print("-----------------------")


# c

def total_comments_by_year(year):
    # Find the total number of comments created each month in the specified year
    comment_count_by_month = db.comments.aggregate([
        {"$match": {"$expr": {"$eq": [{"$year": "$date"}, year]}}},
        {"$group": {"_id": {"$month": "$date"}, "count": {"$sum": 1}}},
        {"$sort": {"_id": 1}}
    ])

    for month in comment_count_by_month:
        print("Month:", month["_id"])
        print("Number of comments:", month["count"])
        print("-----------------------")
