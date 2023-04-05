from comments_analysis import *
from theatre_analysis import *
from movies_analysis import *
"""Created a connection using pymongo.MongoClient to connect with MongoDB."""

client = MongoClient("mongodb://127.0.0.1:27017")
db = client["sample_mflix"]

"""Bulk load the JSON files in the individual MongoDB collections. """
# load_data()

"""Python methods and MongoDB queries to insert new comments, 
    movies, theatres, and users into respective MongoDB collections."""
while (True):
    print("""
            1. Analysis for the movies dataset.
            2. Analysis for the movies dataset.
            3. Analysis for the theatres dataset.
            4. Quit
            """)
    print("Enter your choice:")
    choice = int(input())
    if choice == 1:
        # Comment Analysis
        # a
        print(f"Top users by max comments:")
        top_users_by_max_comments()

        # b
        print(f"Top movies by comments:")
        top_movies_by_comments()

        # c
        print(f"Total comments in a given year: ")
        total_comments_by_year(2001)
    elif choice == 2:
        # Movies Analysis
        # a
        print(f"Top movies by imdb rating: ")
        top_movies_by_imdb_rating(5)
        print(f"Top movies by imdb rating in a given year: ")
        top_movies_by_imdb_rating_in_given_year(5, 2010)
        print(f"Top movies by imdb rating and votes: ")
        top_movies_by_imdb_rating_and_votes(5)
        print(f"Movies matching given pattern: ")
        movies_matching_given_pattern('star', 5)

        # b
        print(f"Top directors: ")
        top_directors_by_movies(5)
        print(f"Top directors by movies in a given year: ")
        top_directors_by_movies_in_given_year(5, 2010)
        print(f"Top directors by movie in a given genre:")
        top_directors_by_movie_in_given_genre(5, 'Action')

        # c
        print(f"Top actors by movies: ")
        top_actors_by_movie(5)
        print(f"Top actors by movies in a given year: ")
        top_actors_by_movie_and_given_year(5, 2010)
        print(f"Top actors by movies in a given genre: ")
        top_actors_by_movie_in_given_genre(5, 'Action')
        # d
        print(f"Top movies by genre and imdb rating: ")
        top_movies_by_genre_and_imdb(5)

    elif choice == 3:
        # Theatre Analysis

        # a
        print(f"Top cities by theatres:")
        top_cities_by_theatres(5)
        # b
        print(f"Top cities by coordinates: ")
        top_cities_by_coordinates(47.02, -122.76)
    else:
        print("Quitting!!!")
        break




