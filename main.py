from flask import Flask
from flask import render_template
from flask import g
from flask import request
import sqlite3

app = Flask(__name__)

DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def seed_db():
    conn = get_db()
    conn.execute('''CREATE TABLE vote
         (id INT PRIMARY KEY     NOT NULL,
         ip              TEXT    NOT NULL,
         user            INT     NOT NULL);''')
    print("Table vote created successfully");

    conn.execute('''CREATE TABLE users
         (id INT PRIMARY KEY     NOT NULL,
         name            TEXT    NOT NULL,
         img_thumb       TEXT    NOT NULL,
         imgs            TEXT    NOT NULL,
         info            TEXT    NOT NULL);''')
    print("Table user created successfully");

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # Only seed one
    # seed_db()
    user = query_db('select * from users where name = ?', ["test"], one=True)
    print(request.environ['REMOTE_ADDR'])
    if user is None:
        print('No such user')
    else:
        print(the_username, 'has the id', user['user_id'])
    return render_template('index.html')

