from typing import List
from fastapi import HTTPException

from app.models.movie_model import Movie, MovieDetailsUpdate
from app.daos.persist_movie_info import PersistMovieInfo


class MongoMovieDAO(PersistMovieInfo):
    def __init__(self, json_location):
        self.json_location = json_location
        self.movies_json = json_location + '\\movies.json'

    def insert_many(self, movies: List[Movie]):
        pass

    def find_all(self):
        pass

    def find_one(self, movie_name: str) -> Movie:
        pass

    def delete_all(self) -> List[Movie]:
        pass

    def delete_one(self, movie_name: str) -> Movie:
        pass

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        pass
