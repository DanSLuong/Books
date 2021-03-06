from flask import (Flask, render_template, request, redirect, jsonify, url_for, flash, g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Author, Book
from flask import session as login_session
import httplib2
import json
from flask import make_response
import requests


app = Flask(__name__)

engine = create_engine('sqlite:///books.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    users = session.query(User).all()
    if request.method == 'POST':
        # if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            # error = 'Invalid Credentials. Please try again.'
        for user in users:
            if request.form['username'] != user.username or request.form['password'] != user.password:
                error = 'Invalid Credentials. Please try again.'
            elif request.form['username'] == user.username and request.form['password'] == user.password:
                login_session['logged_in'] = True
                print(login_session)
                return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    login_session['logged_in'] = False
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        newUser = User(username=request.form['username'],
                        password=request.form['password'],
                        email=request.form['email'])
        session.add(newUser)
        session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/')
@app.route('/home/')
def home():
    if 'username' not in login_session:
        return render_template('home.html')
    else:
        return render_template('home.html')


@app.route('/books')
def books():
    # Query for all books in Book table
    books = session.query(Book).all()
    return render_template('booklist.html', books=books)

@app.route('/authors')
def authors():
    # Query for all authors in Author table
    authors = session.query(Author).all()
    return render_template('authors.html', authors=authors)

@app.route('/books/<int:book_id>/')
@app.route('/books/<int:book_id>/info')
def bookInfo(book_id):
    # Query for books.id==book_id
    books = session.query(Book).filter_by(id=book_id).one()
    # Query for author.id==books.author_id
    author = session.query(Author).filter_by(id=books.author_id).one()
    return render_template('bookinfo.html', books=books, author=author)


@app.route('/authors/<int:author_id>/')
def authorInfo(author_id):
    # Query for authors.id==author_id
    authors = session.query(Author).filter_by(id=author_id)
    # Query for books.author_id==author_id
    books = session.query(Book).filter_by(author_id=author_id)
    return render_template('authorinfo.html', authors=authors, books=books)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
