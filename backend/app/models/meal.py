# backend/app/models/meal.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base


class Meal(Base):
    __tablename__ = "meals"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    meal_name = Column(String, nullable=False)
    meal_type = Column(String, nullable=False)  # frukost, lunch, middag, mellanmål
    date_eaten = Column(DateTime, default=datetime.utcnow)
    
    # Relation till användare
    user = relationship("User", back_populates="meals")