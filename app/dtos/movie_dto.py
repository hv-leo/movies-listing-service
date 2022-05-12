from app.daos.movie_dao import MovieDAO


class MovieDTO:
    @staticmethod
    def insert_many(movies):
        MovieDAO().insert_many(movies)

    @staticmethod
    def find_all():
        return MovieDAO().find_all()

    @staticmethod
    def delete_all():
        MovieDAO().delete_all()

    @staticmethod
    def delete_one(movie_name):
        MovieDAO().delete_one(movie_name)

    @staticmethod
    def update_one(movie_name, details):
        MovieDAO().update_one(movie_name, details)
