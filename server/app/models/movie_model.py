from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    name: str
    genres = str
    director: str
    writers: str
    stars: str
    rating: int
    votes: int
    cover_image: str


class MovieDetailsUpdate(BaseModel):
    director: Optional[str]
    writers: Optional[str]
    stars: Optional[str]
    user_reviews: Optional[int]
    critic_reviews: Optional[int]
    rating: Optional[int]