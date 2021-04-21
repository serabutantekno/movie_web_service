from app import app
from app.controllers.MovieController import MovieController


movies = MovieController()


@app.route("/api/v1/movies", methods=["GET"])
def get_all_movies():
    """Return a list of all movies"""
    return movies.get_all_movies()