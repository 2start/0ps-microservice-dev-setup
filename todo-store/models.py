from sqlalchemy import Column, Integer, Enum, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
