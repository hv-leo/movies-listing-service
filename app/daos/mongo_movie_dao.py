from typing import List
from pymongo import MongoClient
from fastapi import HTTPException
import certifi
import urllib.request
import os

from app.models.movie_model import Movie, MovieDetailsUpdate
from app.daos.persist_movie_info import PersistMovieInfo


class MongoMovieDAO(PersistMovieInfo):
    def __init__(self, configuration):
        self._config = configuration
        self.connection_string = os.getenv('CONNECTION_STRING').\
            replace('replace_pwd', urllib.parse.quote(self._config["password"])).\
            replace('replace_db', self._config["db"])

    def _get_collection(self, client):
        return client[self._config["db"]][self._config["collection"]]

    def insert_many(self, movies: List[Movie]):
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            movies_to_insert = []
            duplicated_movie_names = []
            for movie in movies:
                if movie_collection.count_documents({"name": movie.dict()["name"]}) > 0:
                    duplicated_movie_names.append(movie.dict()["name"])
                else:
                    movies_to_insert.append(movie.dict())
            if len(duplicated_movie_names) > 0:
                raise HTTPException(status_code=400, detail="The following movies already exist in the db: " +
                                                            ', '.join(duplicated_movie_names))
            movie_collection.insert_many(movies_to_insert)
        return movies

    def find_all(self):
        movies = []
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            cursor = movie_collection.find()
            for document in cursor:
                document.pop('_id', None)
                movies.append(document)
        return movies

    def find_one(self, movie_name: str) -> Movie:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            movie = movie_collection.find_one({"name": movie_name})
            if movie is None:
                raise HTTPException(status_code=404, detail="Movie not found")
            movie.pop('_id', None)
            return movie

    def delete_all(self) -> List[Movie]:
        all_movies = self.find_all()
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            movie_collection.drop()
        return all_movies

    def delete_one(self, movie_name: str) -> Movie:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            movie = self.find_one(movie_name)
            movie_collection.delete_one({"name": movie_name})
            return movie

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            movie_collection.find_one_and_update({'name': movie_name},
                                                 {'$set': details.dict()})
        return self.find_one(movie_name)
