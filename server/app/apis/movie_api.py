from fastapi import APIRouter, Depends, Response, status, Request
from typing import List
from dependency_injector.wiring import inject, Provide
import os
from dotenv import load_dotenv

from app.services.movie_service import MovieService
from app.security.verify_token import VerifyToken
from app.models.movie_model import Movie, MovieDetailsUpdate
from app.containers import Container

load_dotenv()

router = APIRouter(
    tags=["Movie"],
    responses={404: {"description": "Not found"}},
    prefix=os.getenv('SERVER_ROOT_PATH') + '/movies'
)


@router.post("/")
@inject
async def insert_movie(movies: List[Movie],
                       movie_service: MovieService = Depends(Provide[Container.movie_service])) -> List[Movie]:
    return movie_service.save(movies)


@router.get("/")
@inject
async def get_all_movies(movie_service: MovieService = Depends(Provide[Container.movie_service])):
    return movie_service.get_all()


@router.get("/{genre}")
@inject
async def get_movies_from_genre(genre: str,
                                response: Response,
                                request: Request,
                                movie_service: MovieService = Depends(Provide[Container.movie_service])) -> List[Movie]:
    token = request.headers.get('authorization').replace('Bearer ', '')
    token_results = VerifyToken(token).verify()
    print(token_results)
    if token_results.get("status"):
        print('Here!')
        response.status_code = status.HTTP_400_BAD_REQUEST
        return token_results
    return movie_service.get_movies_from_given_genre(genre)


@router.delete("/")
@inject
async def delete_all_movies(movie_service: MovieService = Depends(Provide[Container.movie_service])) -> List[Movie]:
    return movie_service.delete_all()


@router.delete("/{movie_name}")
@inject
async def delete_movie(movie_name: str,
                       movie_service: MovieService = Depends(Provide[Container.movie_service])) -> Movie:
    return movie_service.delete_one(movie_name)


@router.patch("/{movie_name}")
@inject
async def update_movie_details(movie_name: str,
                               details: MovieDetailsUpdate,
                               movie_service: MovieService = Depends(Provide[Container.movie_service])) -> Movie:
    return movie_service.update_one(movie_name, details)
