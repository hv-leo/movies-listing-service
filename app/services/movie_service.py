from app.dtos.movie_dto import MovieDTO


class MovieService:
    @staticmethod
    def save(movies):
        MovieDTO.insert_many(movies)

    @staticmethod
    def get_all():
        return MovieDTO.find_all()

    @staticmethod
    def delete_all():
        MovieDTO.delete_all()

    @staticmethod
    def delete_one(movie_name):
        MovieDTO.delete_one(movie_name)

    @staticmethod
    def update_one(movie_name, details):
        MovieDTO.update_one(movie_name, details)
