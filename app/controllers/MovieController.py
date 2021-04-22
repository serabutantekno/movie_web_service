import csv, io
from flask import request
from werkzeug.wrappers import Response
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


    def get_query_string(self):
        try:
            look_for = request.args.get("search")
            result = MovieModel.Movie.query.filter(
                MovieModel.Movie.judul.like(f"%{look_for}%") |\
                MovieModel.Movie.tahun_rilis.like(f"%{look_for}%")|\
                MovieModel.Movie.sutradara.like(f"%{look_for}%")|\
                MovieModel.Movie.pemain.like(f"%{look_for}%")|\
                MovieModel.Movie.rating.like(f"%{look_for}%")
            )
            return self.RESPONSE.base_response(
                message=f"searched words found in {result.count()} movie(s)",
                data=[movie.data_to_json() for movie in result]
            )
        except Exception as error:
            print(error)
            self.RESPONSE.error()


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


    def delete(self, id):
        try:
            movie = MovieModel.Movie.query.get(id)
            db.session.delete(movie)
            db.session.commit()
            return self.RESPONSE.base_response(
                message=f"{movie.judul} deleted successfully",
                data=[MovieModel.Movie.data_to_json(movie)]
            )
        except Exception as error:
            print(error)
            return self.RESPONSE.error()


    def generate_csv(self):

        def generate():
            csv_columns = [
                "id",
                "judul",
                "tahun_rilis",
                "sutradara",
                "pemain",
                "rating"
            ]
            data = io.StringIO()
            writer = csv.writer(data)
            writer.writerow(csv_columns)  # write csv headers
            yield data.getvalue()
            data.seek(0)
            data.truncate(0)

            list_movies = [movie for movie in MovieModel.Movie.query.all()]
            for movie in list_movies:  # write each movie items
                line = [movie.id, movie.judul, movie.tahun_rilis, movie.sutradara, movie.pemain, movie.rating]
                writer.writerow(line)
                yield data.getvalue()
                data.seek(0)
                data.truncate(0)

        # stream the response as the data is generated
        response = Response(generate(), mimetype="text/csv")
        response.headers.set("Content-Disposition", "attachment", filename="movies.csv")
        return response
