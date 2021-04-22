from flask import request
from app import db
from app.controllers.BaseResponseController import BaseResponse
from app.models import MovieModel


class MovieController:
    """Movie Controller"""

    RESPONSE = BaseResponse()

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
            try:
                data = form.to_dict()
                post = MovieModel.Movie(**data)
                db.session.add(post)
                db.session.commit()
                result = MovieModel.Movie.data_to_json(post)
                return self.RESPONSE.base_response(message="a new movie added", data=result, status_code=201)
            except Exception as error:
                print(error)
                return self.RESPONSE.error()


    def get(self, id):
        try:
            return MovieModel.Movie.query.get(id).data_to_json()
        except Exception as error:
            print(error)
            return self.RESPONSE.data_not_found()


    def update(self, id):
        form = request.form
        if form:
            try:
                data = form
                movie = MovieModel.Movie.query.filter_by(id=id)
                movie.update(data)
                db.session.commit()
                return self.RESPONSE.base_response(
                    message="edit movie detail success",
                    data=[MovieModel.Movie.data_to_json(movie) for movie in movie]
                )
            except Exception as error:
                print(error)
                return self.RESPONSE.error()
        else:
            return self.RESPONSE.no_changes()
