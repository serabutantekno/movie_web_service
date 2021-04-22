from flask import request
from app import app
from app.controllers.MovieController import MovieController


movies = MovieController()


@app.route("/api/v1/movies", methods=["GET"])
def get_all_movies():
    """Return a list of all movies or movies determined from query string."""
    if not request.args:
        return movies.get_all_movies()
    else:
        return movies.get_query_string()


@app.route("/api/v1/movies", methods=["POST"])
def create_new_movie():
    """Create a new movie"""
    return movies.create()


@app.route("/api/v1/movies/<int:id>", methods=["GET"])
def get(id):
    """Retrieve a movie detail."""
    return movies.get(id)


@app.route("/api/v1/movies/<int:id>", methods=["PUT"])
def update(id):
    """Update detail of a movie."""
    return movies.update(id)


@app.route("/api/v1/movies/<int:id>", methods=["DELETE"])
def delete(id):
    """Delete a movie."""
    return movies.delete(id)
