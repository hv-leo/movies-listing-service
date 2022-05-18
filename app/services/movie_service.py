from typing import List

from app.daos.movie_dao import MovieDAO
from app.models.movie_model import Movie, MovieDetailsUpdate


class MovieService:

    def __init__(self, db: MovieDAO):
        self.db = db

    def save(self, movies: List[Movie]) -> List[Movie]:
        return self.db.insert_many(movies)

    def get_all(self):
        return self.db.find_all()

    def get_one(self, movie_name: str) -> Movie:
        return self.db.find_one(movie_name)

    def delete_all(self) -> List[Movie]:
        return self.db.delete_all()

    def delete_one(self, movie_name: str) -> Movie:
        return self.db.delete_one(movie_name)

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        return self.db.update_one(movie_name, details)
