import pymongo
from pymongo import MongoClient


"""Created a connection using pymongo.MongoClient to connect with MongoDB."""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]

"""
    Theatres Collection:
        a. Top 10 cities with the maximum number of theatres
        b. top 10 theatres nearby given coordinates
"""


# a
def top_cities_by_theatres(n):
    top_cities = db.theaters.aggregate([
       {"$group": {"_id": "$location.address.city", "theatre_count": {"$sum": 1}}},
       {"$sort": {"theatre_count": -1}},
       {"$limit": 10}
    ])

    # Print the results
    for city in top_cities:
        print(city["_id"], "-", city["theatre_count"])


# b
def top_cities_by_coordinates(lat, long):
    # Find the top 10 theaters nearby given coordinates
    top_theaters = db.theatres.find({
        "location": {
            "$nearSphere": {
                "$geometry": {
                    "type": "Point",
                    "coordinates": [long, lat]
                },
                "$maxDistance": 10000
            }
        }
    }).sort("location.coordinates", pymongo.ASCENDING).limit(10)

    # Print the results
    for theatre in top_theaters:
        print(theatre["name"], "-", theatre["location"]["coordinates"])
