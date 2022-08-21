import os.path
import os
from typing import List
from fastapi import HTTPException
import json
import logging

from server.app.models.movie_model import Movie, MovieDetailsUpdate
from server.app.daos.persist_movie_info import PersistMovieInfo


class JsonMovieDAO(PersistMovieInfo):
    def __init__(self, json_location):
        self.json_location = json_location
        self.movies_json = json_location + '\\movies.json' if json_location != "current_dir" \
            else os.getcwd() + '/movies.json'
        if not os.path.isfile(self.movies_json):
            self.create_empty_file()

    def create_empty_file(self):
        with open(self.movies_json, 'w') as file:
            json.dump([], file)

    def insert_many(self, movies: List[Movie]) -> List[Movie]:
        with open(self.movies_json) as file:
            all_movies = json.load(file)
        with open(self.movies_json, 'w') as file:
            all_movies += [movie.dict() for movie in movies]
            logging.info('Storing movies in json file')
            try:
                json.dump(all_movies, file)
                logging.info("Movies stored successfully")
            except Exception as e:
                raise Exception(f'The following error occurred when trying to store movies in the json file: {e}')
            return movies

    def find_all(self) -> List[Movie]:
        with open(self.movies_json) as file:
            all_movies = json.load(file)
            if all_movies != [] and type(all_movies[0]) == dict:
                return all_movies
            return [json.loads(movie) for movie in all_movies]

    def find_one(self, movie_name: str) -> Movie:
        with open(self.movies_json) as file:
            all_movies = json.load(file)
        movie = list(filter(lambda m: m["name"] == movie_name, all_movies))
        if movie:
            return movie[0]
        raise HTTPException(status_code=404, detail="Movie not found")

    def delete_all(self) -> List[Movie]:
        all_movies = self.find_all()
        self.create_empty_file()
        return all_movies

    def delete_one(self, movie_name: str) -> Movie:
        with open(self.movies_json) as file:
            all_movies = json.load(file)
        movie = list(filter(lambda m: m["name"] == movie_name, all_movies))
        if movie:
            logging.info(f'Deleting movie {movie[0]["name"]}')
            try:
                all_movies.remove(movie[0])
                with open(self.movies_json, 'w') as file:
                    json.dump(all_movies, file)
                    logging.info(f'Movie {movie[0]["name"]} deleted successfully')
                    return movie[0]
            except Exception as e:
                raise Exception(f'Error while deleting movie {movie[0]["name"]}: {e}')
        raise HTTPException(status_code=404, detail="Movie not found")

    def update_one(self, movie_name: str, details: MovieDetailsUpdate) -> Movie:
        with open(self.movies_json) as file:
            all_movies = json.load(file)
        movie = list(filter(lambda m: m["name"] == movie_name, all_movies))
        if movie:
            logging.info(f'Updating info regarding movie {movie[0]["name"]}')
            try:
                all_movies.remove(movie[0])
                movie[0].update(details.dict())
                all_movies += movie
                with open(self.movies_json, 'w') as file:
                    json.dump(all_movies, file)
                    logging.info(f'Movie {movie[0]["name"]} was successfully updated with new information.')
                    return movie[0]
            except Exception as e:
                raise Exception(f'Error while updating movie {movie[0]["name"]} with new info: {e}')

        raise HTTPException(status_code=404, detail="Movie not found")
