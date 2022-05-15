from typing import List

from app.daos.movie_dao import MovieDAO
from app.models.movie_model import Movie, MovieDetailsUpdate


class MovieService:
    @staticmethod
    def save(movies: List[Movie]) -> List[Movie]:
        return MovieDAO().insert_many(movies)

    @staticmethod
    def get_all():
        return MovieDAO().find_all()

    @staticmethod
    def get_one(movie_name: str) -> Movie:
        return MovieDAO().find_one(movie_name)

    @staticmethod
    def delete_all() -> List[Movie]:
        return MovieDAO().delete_all()

    @staticmethod
    def delete_one(movie_name: str) -> Movie:
        return MovieDAO().delete_one(movie_name)

    @staticmethod
    def update_one(movie_name: str, details: MovieDetailsUpdate) -> Movie:
        return MovieDAO().update_one(movie_name, details)
