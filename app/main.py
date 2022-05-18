from fastapi import FastAPI

from app.containers import Container
from app.apis import movie_api

container = Container()
container.config.override({
    "db": "movie",
    "collection": "info",
    "password": r'*+Ea3`{p6:66K\~U'
})

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the movies recomendation system!"}


app.container = container
app.include_router(movie_api.router)

