# backend/app/schemas/meal.py
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MealBase(BaseModel):
    meal_name: str
    meal_type: str


class MealCreate(MealBase):
    pass


class MealUpdate(BaseModel):
    meal_name: Optional[str] = None
    meal_type: Optional[str] = None


class MealResponse(MealBase):
    id: int
    user_id: int
    date_eaten: datetime
    
    class Config:
        from_attributes = True