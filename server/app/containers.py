from dependency_injector import providers, containers

from server.app.daos.persist_movie_info import PersistMovieInfo
from server.app.services.movie_service import MovieService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.apis.movie_api"])

    persist_movie_info = providers.AbstractFactory(PersistMovieInfo)

    movie_service = providers.Factory(MovieService, movie_dao=persist_movie_info)
