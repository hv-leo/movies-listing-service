from fastapi import FastAPI
from dependency_injector import providers
from decouple import config

from app.containers import Container
from app.apis import movie_api
from app.daos.mongo_movie_dao import MongoMovieDAO
from app.daos.json_movie_dao import JsonMovieDAO


container = Container()
if config('PERSISTANCE_CLIENT') == 'MongoDB':
    container.persist_movie_info.override(providers.Factory(MongoMovieDAO,
                                                            configuration={
                                                                    "db": config('DB'),
                                                                    "collection": config('COLLECTION'),
                                                                    "password": config('MONGDDB_PWD')
                                                                }))

elif config('PERSISTANCE_CLIENT') == 'JsonFile':
    container.persist_movie_info.override(providers.Factory(JsonMovieDAO,
                                                            json_location=config('JSON_LOCATION')))


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the movies recomendation system!"}


app.container = container
app.include_router(movie_api.router)

