from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    name: str
    director: str
    writers: str
    stars: str
    user_reviews: int
    critic_reviews: int
    rating: int


class MovieDetailsUpdate(BaseModel):
    director: Optional[str]
    writers: Optional[str]
    stars: Optional[str]
    user_reviews: Optional[int]
    critic_reviews: Optional[int]
    rating: Optional[int]