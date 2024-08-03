from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class Comment(Base):

    __tablename__ = "comments"

    id = Column(Integer, primary_key = True)
    id_movie = Column(Integer, ForeignKey('movies.id'))
    comment = Column(String)