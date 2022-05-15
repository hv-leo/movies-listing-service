from typing import List

from app.daos.movie_dao import MovieDAO
from app.models.movie_model import Movie, MovieDetailsUpdate


class MovieService:
    @staticmethod
    def save(movies: List[Movie]):
        MovieDAO().insert_many(movies)

    @staticmethod
    def get_all():
        return MovieDAO().find_all()

    @staticmethod
    def delete_all():
        MovieDAO().delete_all()

    @staticmethod
    def delete_one(movie_name: str):
        MovieDAO().delete_one(movie_name)

    @staticmethod
    def update_one(movie_name: str, details: MovieDetailsUpdate):
        MovieDAO().update_one(movie_name, details)
