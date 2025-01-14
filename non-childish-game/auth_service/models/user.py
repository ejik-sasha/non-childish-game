from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from shared.database import Base

class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    balance = Column(Integer, default=0)

    characters = relationship("Character", back_populates="user")