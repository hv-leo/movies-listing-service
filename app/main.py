from fastapi import FastAPI
from dependency_injector import providers
from decouple import config

from app.containers import Container
from app.apis import movie_api
from app.daos.mongo_movie_dao import MongoMovieDAO


container = Container()
if config('PERSISTANCE_CLIENT') == 'MongoDB':
    container.persist_movie_info.override(providers.Factory(MongoMovieDAO,
                                                            config={
                                                                    "db": config('DB'),
                                                                    "collection": config('COLLECTION'),
                                                                    "password": config('MONGDDB_PWD')
                                                                }))

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the movies recomendation system!"}


app.container = container
app.include_router(movie_api.router)

