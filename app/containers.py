from dependency_injector import providers, containers

from app.daos.movie_dao import MovieDAO
from app.services.movie_service import MovieService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["app.apis.movie_api"])

    config = providers.Configuration('config')

    movie_dao = providers.Singleton(MovieDAO, config)

    movie_service = providers.Factory(MovieService, db=movie_dao)
