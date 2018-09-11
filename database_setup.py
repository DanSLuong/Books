import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from datetime import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'id': self.id,
        }


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250), nullable=False)

    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author, backref=backref('book'), cascade='all, delete')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'id': self.id,
        }
    

"""
class BorrowedBy(Base):
    __tableName__ = 'borrowedBy'

    rentedDate = Column(DateTime, default=datetime.utcnow)
    dueDate = Column(db.DateTime)

    @property
    def serialize(self):
        """'Return object data in easily serializeable format'"""
        return {
            'rentedDate': self.rentedDate,
            'dueDate': self.dueDate,
        }

"""


engine = create_engine('sqlite:///books.db')
Base.metadata.create_all(engine)