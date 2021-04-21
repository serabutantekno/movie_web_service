from flask import request
from app import db
from app.models import MovieModel


class MovieController:
    """Movie Controller"""

    def get_all_movies(self):
        all_movies_obj = MovieModel.Movie.query.all()
        list_all_movies_obj = [movie.data_to_json() for movie in all_movies_obj]
        return {
            "message": "retrieving all movies success",
            "data": list_all_movies_obj
        }


    def create(self):
        form = request.form
        if form:
            data = form.to_dict()
            post = MovieModel.Movie(**data)
            db.session.add(post)
            db.session.commit()
            return MovieModel.Movie.data_to_json(post)
