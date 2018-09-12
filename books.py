from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Author, Book, User

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

author1 = Author(firstName = "J.K.", lastName = "Rolling")

book1 = Book(author_id = 1, 
title = "Harry Potter and the Sorcerer's Stone", 
genre = "Fantasy", 
ISBN = "0747532699", 
year = "1997", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51HSkTKlauL._SX346_BO1,204,203,200_.jpg")
session.add(book1)

book2 = Book(author_id = 1, 
title = "Harry Potter and the Chamber of Secrets", 
genre = "Fantasy", 
ISBN = "0747538492", 
year = "1998", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51jNORv6nQL._SX340_BO1,204,203,200_.jpg")
session.add(book2)

book3 = Book(author_id = 1, 
title = "Harry Potter and the Prisoner of Azkaban", 
genre = "Fantasy", 
ISBN = "0747542155", 
year = "1999", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51-rbiAIiRL._SX341_BO1,204,203,200_.jpg")
session.add(book3)

book4 = Book(author_id = 1, 
title = "Harry Potter and the Goblet of Fire", 
genre = "Fantasy", 
ISBN = "07475462410", 
year = "2000", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51gR-u2VnlL.jpg")
session.add(book4)

book5 = Book(author_id = 1, 
title = "Harry Potter and the Order of the Phoenix", 
genre = "Fantasy", 
ISBN = "0747551006", 
year = "2003", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51XDBEZFD1L._SX322_BO1,204,203,200_.jpg")
session.add(book5)

book6 = Book(author_id = 1, 
title = "Harry Potter and the Half-Blood Prince", 
genre = "Fantasy", 
ISBN = "0747581088", 
year = "2005", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51uO1pQc5oL._SX329_BO1,204,203,200_.jpg")
session.add(book6)

book7 = Book(author_id = 1, 
title = "Harry Potter and the Deathly Hallows", 
genre = "Fantasy", 
ISBN = "0545010225", 
year = "2007", 
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/51E7NvVLO9L._SX346_BO1,204,203,200_.jpg")
session.add(book7)

session.commit()

