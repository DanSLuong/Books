from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Author, Book, User

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

author1 = Author(firstName = "J.K.",
                lastName = "Rolling",
                profilePic="https://cdn-images-1.medium.com/max/2000/0*jCMeqyKliSaz_4sl.jpg",
                birthday="July 31, 1965")
session.add(author1)
author2 = Author(firstName = "Mark",
                lastName = "Twain",
                profilePic="http://www.highplainschautauqua.org/Data/Sites/1/mark-twain.jpg",
                birthday="November 30, 1835")
session.add(author2)
author3 = Author(firstName = "Dr.",
                lastName = "Seuss",
                profilePic="https://www.stmuhistorymedia.org/wp-content/uploads/2017/04/Dr-seuss-ew-770x476.jpg",
                birthday="March 2, 1904")
session.add(author3)
author4 = Author(firstName = "Stephen",
                lastName = "King",
                profilePic="https://imagesvc.timeincapp.com/v3/fan/image?url=https%3A%2F%2F1428elm.com%2Ffiles%2F2018%2F01%2FStephen-King-Courtesy-of-BookBub-Blog.jpg&c=sc&w=850&h=560",
                birthday="September 21, 1947")
session.add(author4)
author5 = Author(firstName = "Hernest",
                lastName = "Hemingway",
                profilePic="https://upload.wikimedia.org/wikipedia/commons/2/28/ErnestHemingway.jpg",
                birthday="July 21, 1899")
session.add(author5)
author6 = Author(firstName = "William",
                lastName = "Nicholson",
                profilePic="https://static1.squarespace.com/static/5630b279e4b02e2518b1d533/t/5689022ec647ad510afcd611/1451819587115/",
                birthday="January 12, 1948 ")
session.add(author6)
author7 = Author(firstName = "Makoto", 
                lastName = "Shinkai", 
                profilePic="https://upload.wikimedia.org/wikipedia/commons/3/39/Makoto_Shinkhai_in_Moscow.JPG",
                birthday="February 9, 1973")
session.add(author7)
author8 = Author(firstName = "Nisio",
                lastName = "Isin",
                profilePic="https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg",
                birthday="1981")
session.add(author8)
author9 = Author(firstName = "Yuu",
                lastName = "Kamiya",
                profilePic="https://myanimelist.cdn-dena.com/images/voiceactors/3/5422.jpg",
                birthday="November 10, 1984")
session.add(author9)
author10 = Author(firstName = "Kazuma",
                lastName = "Kamachi",
                profilePic="https://alchetron.com/cdn/kazuma-kamachi-86b703ee-14ac-48a2-b9ee-8e957c84ef3-resize-750.jpeg")
session.add(author10)
author11 = Author(firstName = "Kumo",
                lastName = "Kagyu",
                profilePic="https://t3.ftcdn.net/jpg/00/64/67/52/240_F_64675209_7ve2XQANuzuHjMZXP3aIYIpsDKEbF5dD.jpg",
                birthday="February 9, 1973")
session.add(author11)
session.commit()

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

book8 = Book(author_id = 7, 
title = "Your name", 
genre = "Fantasy", 
ISBN = "0316471860",
pages = 262,
publisher = "Kadokawa Corporation",
year = "2017", 
imgUrl = "http://i.imgur.com/xNPlWgd.jpg")
session.add(book8)

book9 = Book(author_id = 8,
title = "Kizumonogatari",
genre = "Fantasy",
ISBN = "1941220975",
pages = 354,
publisher = "Vertical",
year =  "2015",
imgUrl = "https://images-na.ssl-images-amazon.com/images/I/81NSmZ7NUJL.jpg")
session.add(book9)


session.commit()

