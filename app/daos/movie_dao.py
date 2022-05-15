from typing import List
from pymongo import MongoClient
from fastapi import HTTPException

from app.models.movie_model import Movie, MovieDetailsUpdate


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = cls._build_key(args, kwargs)
        if key not in cls._instances:
            cls._instances[key] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[key]

    def _build_key(cls, *args, **kwargs) -> tuple:
        sorted_kwargs = []
        for key in sorted(kwargs):
            sorted_kwargs.append((key, kwargs[key]))
        return cls, str(args), str(sorted_kwargs)


class MovieDAO(metaclass=Singleton):
    def __init__(self):
        self.db = "movie"
        self.collection = "info"

    def _get_collection(self, client):
        return client[self.db][self.collection]

    def insert_many(self, movies: List[Movie]):
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            movie_collection = self._get_collection(client)
            movies_to_insert = [movie.dict() for movie in movies]
            movie_collection.insert_many(movies_to_insert)

    def find_all(self):
        movies = []
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            movie_collection = self._get_collection(client)
            cursor = movie_collection.find()
            for document in cursor:
                document.pop('_id', None)
                movies.append(document)
        return movies

    def delete_all(self):
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            movie_collection = self._get_collection(client)
            movie_collection.drop()

    def delete_one(self, movie_name: str):
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            movie_collection.delete_one({"name": movie_name})

    def update_one(self, movie_name: str, details: MovieDetailsUpdate):
        with MongoClient('mongodb://127.0.0.1:27017') as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            movie_collection.find_one_and_update({'name': movie_name},
                                                 {'$set': details.dict()})
