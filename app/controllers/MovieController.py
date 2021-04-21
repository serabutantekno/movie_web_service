from app.models import MovieModel


class MovieController:
    """Movie Controller"""

    def get_all_movies(self):
        all_movies_obj = MovieModel.Movie.query.all()
        list_all_movies_obj = list(all_movies_obj)
        return {
            "message": "retrieving all movies success",
            "data": list_all_movies_obj
        }
