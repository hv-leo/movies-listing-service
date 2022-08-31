from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
                                                                    "password": os.getenv('MONGODB_PWD'),
                                                                    "username": os.getenv('MONGODB_USERNAME')
                                                                }))

else:
    container.persist_movie_info.override(providers.Factory(JsonMovieDAO,
                                                            json_location=os.getenv('JSON_LOCATION')))


app = FastAPI(docs_url=os.getenv('SERVER_ROOT_PATH') + '/docs',
              openapi_url=os.getenv('SERVER_ROOT_PATH') + '/openapi.json')


@app.get(os.getenv('SERVER_ROOT_PATH'))
async def root():
    return {"message": "Welcome to the movies recomendation system!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins="http://localhost:3000/server/movies",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.container = container
app.include_router(movie_api.router)

