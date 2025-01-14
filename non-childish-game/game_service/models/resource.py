from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from shared.database import Base

class Resource(Base):
    __tablename__="resources"

    id = Column(Integer, primary_key=True, index=True)
    resource_type = Column(String, nullable=False)  # Камень, Дерево, Железо
    amount = Column(Integer, default=0)

    character_id = Column(Integer, ForeignKey("characters.id"))
    character = relationship("Character", back_populates="resources")