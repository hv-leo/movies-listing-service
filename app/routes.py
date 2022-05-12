from fastapi import APIRouter
from app.apis import movie_api

router = APIRouter()
router.include_router(movie_api.router)
