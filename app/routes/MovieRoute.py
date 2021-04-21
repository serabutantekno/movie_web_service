from app import app
from app.controllers.MovieController import MovieController


movies = MovieController()


@app.route("/api/v1/movies", methods=["GET"])
def get_all_movies():
    """Return a list of all movies"""
    return movies.get_all_movies()


@app.route("/api/v1/movies", methods=["POST"])
def create_new_movie():
    """Create a new movie"""
    return movies.create()


@app.route("/api/v1/movies/<int:id>", methods=["GET"])
def get(id):
    """Retrieve a movie detail."""
    return movies.get(id)
