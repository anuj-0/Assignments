from pymongo import MongoClient

"""Created a connection using pymongo.MongoClient to connect with MongoDB."""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]

"""
    Movies Collection:
        a. Find top `N` movies - 
            1. with the highest IMDB rating
            2. with the highest IMDB rating in a given year
            3. with highest IMDB rating with number of votes > 1000
            4. with title matching a given pattern sorted by highest tomatoes ratings

        b. Find top `N` directors -
            1. who created the maximum number of movies
            2. who created the maximum number of movies in a given year
            3. who created the maximum number of movies for a given genre

        c. Find top `N` actors - 
            1. who starred in the maximum number of movies
            2. who starred in the maximum number of movies in a given year
            3. who starred in the maximum number of movies for a given genre

        d. Find top `N` movies for each genre with the highest IMDB rating

"""


# a1

def top_movies_by_imdb_rating(n):
    # Find the top N movies with the highest IMDB rating
    top_movies = db.movies.find().sort([("imdb.rating", -1)]).limit(n)

    # Print the results
    for movie in top_movies:
        print("Movie title:", movie["title"])
        print("IMDB rating:", movie["imdb"]["rating"])
        print("-----------------------")


# a2
def top_movies_by_imdb_rating_in_given_year(n, year):
    # Find the top N movies with the highest IMDB rating in the specified year
    top_movies = db.movies.find({"year": year}).sort([("imdb.rating", -1)]).limit(n)

    # Print the results
    for movie in top_movies:
        print("Movie title:", movie["title"])
        print("IMDB rating:", movie["imdb"]["rating"])
        print("-----------------------")


# a3

def top_movies_by_imdb_rating_and_votes(n):
    # Find the top N movies with the highest IMDB rating and number of votes > 1000
    top_movies = db.movies.find({"imdb.rating": {"$gt": 0}, "imdb.votes": {"$gt": 1000}}).sort(
        [("imdb.rating", -1)]).limit(n)

    # Print the results
    for movie in top_movies:
        print("Movie title:", movie["title"])
        print("IMDB rating:", movie["imdb"]["rating"])
        print("IMDB votes:", movie["imdb"]["votes"])
        print("-----------------------")


# a4

def movies_matching_given_pattern(pattern, n):
    # Find the top N movies with title matching the pattern sorted by highest tomatoes ratings
    top_movies = db.movies.find({"title": {"$regex": pattern}},
                                {"_id": 0, "title": 1,
                                 "tomatoes.viewer.rating": 1}) \
        .sort([("tomatoes.viewer.rating", -1)]).limit(n)

    # Print the results
    for movie in top_movies:
        print("Movie title:", movie["title"])
        print("Tomatoes rating:", movie["tomatoes"]["viewer"]["rating"])
        print("-----------------------")


# b1

def top_directors_by_movies(n):
    # Find the top N directors who created the maximum number of movies
    top_directors = db.movies.aggregate([
        {"$group": {"_id": "$directors", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for director in top_directors:
        print("Director:", director["_id"])
        print("Number of movies:", director["count"])
        print("-----------------------")


# b2

def top_directors_by_movies_in_given_year(n, year):
    # Find the top N directors who created the maximum number of movies in the given year
    top_directors = db.movies.aggregate([
        {"$match": {"year": year}},
        {"$group": {"_id": "$directors", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for director in top_directors:
        print("Director:", director["_id"])
        print("Number of movies in {}: {}".format(year, director["count"]))
        print("-----------------------")


# b3

def top_directors_by_movie_in_given_genre(n, genre):
    # Find the top N directors who created the maximum number of movies in the given genre
    top_directors = db.movies.aggregate([
        {"$unwind": "$genres"},
        {"$match": {"genres": genre}},
        {"$group": {"_id": "$directors", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for director in top_directors:
        print("Director:", director["_id"])
        print("Number of {} movies:".format(genre), director["count"])
        print("-----------------------")


# c1

def top_actors_by_movie(n):
    # Find the top N actors who starred in the maximum number of movies
    top_actors = db.movies.aggregate([
        {"$unwind": "$cast"},
        {"$group": {"_id": "$cast", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for actor in top_actors:
        print("Actor:", actor["_id"])
        print("Number of movies:", actor["count"])
        print("-----------------------")


# c2

def top_actors_by_movie_and_given_year(n, year):
    # Find the top N actors who starred in the maximum number of movies in the given year
    top_actors = db.movies.aggregate([
        {"$match": {"year": year}},
        {"$unwind": "$cast"},
        {"$group": {"_id": "$cast", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for actor in top_actors:
        print("Actor:", actor["_id"])
        print("Number of movies in {}: {}".format(year, actor["count"]))
        print("-----------------------")


# c3
def top_actors_by_movie_in_given_genre(n, genre):
    # Find the top N actors who starred in the maximum number of movies in the given genre
    top_actors = db.movies.aggregate([
        {"$unwind": "$cast"},
        {"$unwind": "$genres"},
        {"$match": {"genres": genre}},
        {"$group": {"_id": "$cast", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": n}
    ])

    # Print the results
    for actor in top_actors:
        print("Actor:", actor["_id"])
        print("Number of {} movies:".format(genre), actor["count"])
        print("-----------------------")


# d
def top_movies_by_genre_and_imdb(n):
    # Find the top N movies for each genre with the highest IMDB rating
    top_movies_by_genre = db.movies.aggregate([
        {"$unwind": "$genres"},
        {"$sort": {"genres": 1, "imdb.rating": -1}},
        {"$group": {"_id": "$genres", "movies": {"$push": "$$ROOT"}}},
        {"$project": {"_id": 0, "genre": "$_id", "top_movies": {"$slice": ["$movies", n]}}},
        {"$limit": n}
    ])

    # Print the results
    for genre in top_movies_by_genre:
        print("Genre:", genre["genre"])
        for movie in genre["top_movies"]:
            print("Title:", movie["title"])
            print("IMDB Rating:", movie["imdb"]["rating"])
            print("-----------------------")
