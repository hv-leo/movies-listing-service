from abc import ABC


class PersistMovieInfo(ABC):
    def insert_many(self, movies):
        pass

    def find_all(self):
        pass

    def find_one(self, movie_name):
        pass

    def delete_all(self):
        pass

    def delete_one(self, movie_name):
        pass

    def update_one(self, movie_name, details):
        pass
