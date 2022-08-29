from typing import List
from pymongo import MongoClient
from fastapi import HTTPException
import certifi
import urllib.request
import os
import logging

from app.models.movie_model import Movie, MovieDetailsUpdate
from app.daos.persist_movie_info import PersistMovieInfo


class MongoMovieDAO(PersistMovieInfo):
    def __init__(self, configuration):
        self._config = configuration
        self.connection_string = os.getenv('CONNECTION_STRING').\
            replace('replace_pwd', urllib.parse.quote(self._config["password"])).\
            replace('replace_username', self._config["username"])

    def _get_collection(self, client):
        return client[self._config["db"]][self._config["collection"]]

    def insert_many(self, movies: List[Movie]) -> List[Movie]:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            movies_to_insert = []
            duplicated_movie_names = []
            logging.info("Verifying which movies are not duplicated...")
            for movie in movies:
                if movie_collection.count_documents({"name": movie.dict()["name"]}) > 0:
                    duplicated_movie_names.append(movie.dict()["name"])
                else:
                    movies_to_insert.append(movie.dict())
            logging.info('Movies duplication verification done.')
            if len(duplicated_movie_names) > 0:
                raise HTTPException(status_code=400, detail="The following movies already exist in the db: " +
                                                            ', '.join(duplicated_movie_names))
            logging.info('Inserting movies in Mongo DB')
            try:
                movie_collection.insert_many(movies_to_insert)
                logging.info('Movies were successfully inserted into Mongo DB')
            except Exception as e:
                raise Exception(f'An error occurred while trying to persiste the movies in the DB: {e}')

        return movies

    def find_all(self) -> List[Movie]:
        movies = []
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            cursor = movie_collection.find()
            for document in cursor:
                document.pop('_id', None)
                movies.append(document)
        return movies

    def find_many(self, genre: str) -> List[Movie]:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            movies = movie_collection.find({"genres": {"$regex" : f".*{genre}.*"}}, {'_id': 0})
            movies_to_return = []
            for movie in movies:
                movies_to_return.append(movie)
            if movies_to_return==[]:
                raise HTTPException(status_code=404, detail=f"Movies not found for genre {genre}")
            return movies_to_return

    def delete_all(self) -> List[Movie]:
        all_movies = self.find_all()
        logging.info('Deleting all the movies')
        try:
            with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
                movie_collection = self._get_collection(client)
                movie_collection.drop()
                logging.info('All movies were deleted successfully')
        except Exception as e:
            raise Exception(f'An error occurred while trying to delete all the movies: {e}')
        return all_movies

    def delete_one(self, movie_name: str) -> Movie:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            logging.info(f'Deleting movie {movie_name}')
            try:
                movie = self.find_one(movie_name)
                movie_collection.delete_one({"name": movie_name})
                logging.info(f'Movie {movie_name} was successfully deleted')
            except Exception as e:
                raise Exception(f'An error occurred while trying to delete movie {movie_name} : {e}')
            return movie

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        with MongoClient(self.connection_string, tlsCAFile=certifi.where()) as client:
            movie_collection = self._get_collection(client)
            if movie_collection.count_documents({"name": movie_name}) == 0:
                raise HTTPException(status_code=404, detail="Movie not found")
            logging.info(f'Updating  movie {movie_name}  with new info')
            try:
                movie_collection.find_one_and_update({'name': movie_name},
                                                     {'$set': details.dict()})
            except Exception as e:
                raise Exception(f'An error occurred while trying to update movie {movie_name} with new info : {e}')
        return self.find_one(movie_name)
