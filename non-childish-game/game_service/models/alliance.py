from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from shared.database import Base

class Alliance(Base):
    __tablename__ = "alliances"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)

    members = relationship("User", secondary="alliance_members")