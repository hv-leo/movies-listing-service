from typing import List

from app.daos.persist_movie_info import PersistMovieInfo
from app.models.movie_model import Movie, MovieDetailsUpdate


class MovieService:

    def __init__(self, movie_dao: PersistMovieInfo):
        self.movie_dao = movie_dao

    def save(self, movies: List[Movie]) -> List[Movie]:
        return self.movie_dao.insert_many(movies)

    def get_all(self):
        return self.movie_dao.find_all()

    def get_one(self, movie_name: str) -> Movie:
        return self.movie_dao.find_one(movie_name)

    def delete_all(self) -> List[Movie]:
        return self.movie_dao.delete_all()

    def delete_one(self, movie_name: str) -> Movie:
        return self.movie_dao.delete_one(movie_name)

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        return self.movie_dao.update_one(movie_name, details)
