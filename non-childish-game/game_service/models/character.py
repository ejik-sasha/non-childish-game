from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from shared.database import Base

class Character(Base):
    __tablename__="characters"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String(50), nullable=False)
    class_type = Column(String(20), nullable=False) #A, B, C
    level = Column(Integer, default=0)
    inlligence = Column(Integer, default=0)
    agility = Column(Integer, default=0)
    gathering = Column(Integer, default=0)
    health = Column(Integer, default=100)

    user = relationship("User", back_populates="characters")

    resources = relationship("Resource", back_populates="character")