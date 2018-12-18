import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'username': self.username,
            # 'password': self.password,
            'email': self.email,
            'id': self.id,
        }


class Author(Base):
    __tablename__ = 'author'

    id = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    profilePic = Column(String(250), nullable=True)
    birthday = Column(String(250), nullable=True)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'firstName': self.firstName,
            'lastName': self.lastName,
            'profilePic': self.profilePic,
            'birthday': self.birthday,
            'id': self.id,
        }



class Publisher(Base):
    __tablename__ = 'publisher'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'address': self.address,
            'id': self.id,
        }


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    genre = Column(String(250), nullable=False)
    ISBN = Column(Integer, nullable=False)
    publisher = Column(String(250), nullable=True)
    pages = Column(Integer, nullable=True)
    year = Column(Integer, nullable=False)
    imgUrl = Column(String(250))

    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author, backref=backref('book'), cascade='all, delete')

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'ISBN': self.ISBN,
            'publisher': self.publisher,
            'pages': self.pages,
            'year': self.year,
            'imgUrl': self.imgUrl,
            'id': self.id,
        }
    

"""
class Catalog(Base):
    __tableName__ = 'catalog'

    id = Column(Integer, primary_key=True)
    numCopies = Column(Integer, nullable=False)
    available = Column(Boolean, nullable=False)

    book_id = Column(Integer, ForiengKey('book.id'))
    book = relationship(Book, backref=backref('catalog'), cascade'all, delete')


    @property
    def serialize(self):
        """'Return object data in easily serializeable format'"""
        return {
            'numCopies': self.numCopies,
            'available: self.available,
            'id': self.id,
        }


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