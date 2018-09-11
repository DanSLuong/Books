from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Author, Book, User

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

author1 = Author(firstName="J.K.", lastName="Rolling")
book1=Book(author_id=1,title="Harry Potter and the Sorcerer's Stone",genre="Fantasy",ISBN="0747532699")
session.add(book1)
session.commit()

