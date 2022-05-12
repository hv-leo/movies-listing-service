from fastapi import APIRouter
from typing import List

from app.services.movie_service import MovieService
from app.models.movie_model import Movie, MovieDetailsUpdate

router = APIRouter(
    tags=["Movie"],
    responses={404: {"description": "Not found"}},
)

DB = "movie"
INFO_COLLECTION = "info"


@router.post("/movies")
async def insert_movie(movies: List[Movie]):
    MovieService.save(movies)
    return {"ok": True}


@router.get("/movies")
async def get_all_movies():
    return MovieService.get_all()


@router.delete("/movies")
async def delete_all_movies():
    MovieService.delete_all()
    return {"ok": True}


@router.delete("/movies/{movie_name}")
async def delete_movie(movie_name: str):
    MovieService.delete_one(movie_name)

    return {"ok": True}


@router.patch("/movies/{movie_name}")
async def update_movie_details(movie_name: str, details: MovieDetailsUpdate):
    MovieService.update_one(movie_name, details)
    return {"ok": True}
