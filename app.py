from flask import (Flask, render_template, request, redirect, jsonify, url_for, flash, g)
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Author, Book
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
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            login_session['logged_in'] = True
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
        return redirect(url_for('login.html'))
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
    books = session.query(Book).all()
    # authors = session.query(Author).all()
    # books = session.query(Book).filter_by(author_id=author_id).all()
    return render_template('booklist.html', books=books)

@app.route('/authors')
def authors():
    authors = session.query(Author).all()
    return render_template('authors.html', authors=authors)

@app.route('/books/<int:book_id>/')
@app.route('/books/<int:book_id>/info')
def bookInfo(book_id): # , author_id):
    books = session.query(Book).filter_by(id=book_id)
    # authors = session.query(Author).filter_by(id=author_id).one()
    return render_template('bookinfo.html', books=books)# , authors=authors)


@app.route('/authors/<int:author_id>/')
def authorInfo(author_id):
    authors = session.query(Author).all()
    return render_template('authorinfo.html', authors=authors)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
