from fastapi import FastAPI
from dependency_injector import providers
import os
from dotenv import load_dotenv

from app.containers import Container
from app.apis import movie_api
from app.daos.mongo_movie_dao import MongoMovieDAO
from app.daos.json_movie_dao import JsonMovieDAO

# This will look for a file .env in the current directory
# and will add all the variable definitions in it to the os.environ dictionary
load_dotenv()

container = Container()
if "MONGODB_PWD" in os.environ:
    container.persist_movie_info.override(providers.Factory(MongoMovieDAO,
                                                            configuration={
                                                                    "db": os.getenv('DB'),
                                                                    "collection": os.getenv('COLLECTION'),
                                                                    "password": os.getenv('MONGODB_PWD')
                                                                }))

else:
    container.persist_movie_info.override(providers.Factory(JsonMovieDAO,
                                                            json_location=os.getenv('JSON_LOCATION')))


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the movies recomendation system!"}


app.container = container
app.include_router(movie_api.router)

