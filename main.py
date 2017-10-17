from flask import Flask
from flask import render_template
from flask import g
from flask import request
import sqlite3

app = Flask(__name__)

MAX_VOTE = 3
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
         name            TEXT    NOT NULL,
         mac             TEXT    NOT NULL,
         user            INT     NOT NULL);''')
    print("Table vote created successfully");

    conn.execute('''CREATE TABLE users
         (id INT PRIMARY KEY     NOT NULL,
         name            TEXT    NOT NULL,
         dep             TEXT    NOT NULL,
         img_thumb       TEXT    NOT NULL,
         imgs            TEXT    NOT NULL,
         info            TEXT    NOT NULL);''')
    print("Table user created successfully");

def seed_user():
    conn = get_db()
    conn.cursor().execute('''INSERT INTO 'users' ('id','name','dep','img_thumb','imgs','info') VALUES
(44, "Pham Vu Tuoi", "VT-TL", "44_Pham Vu Tuoi_VT-TL.jpg", "44_Pham Vu Tuoi_VT-TL.jpg", ""),
(45, "Nguyen Hong Lien", "VT-TL", "45_Nguyen Hong Lien_VT-TL.jpg", "45_Nguyen Hong Lien_VT-TL.jpg", ""),
(46, "Nguyen Thi Ly", "SD1", "46_Nguyen Thi Ly_SD1.jpg", "46_Nguyen Thi Ly_SD1.jpg", ""),
(47, "Nguyen Thuy Nga", "VT", "47_Nguyen Thuy Nga_VT.jpg", "47_Nguyen Thuy Nga_VT.jpg", ""),
(48, "Nguyen Thi Thu Hang", "SD2", "48_Nguyen Thi Thu Hang_SD2.jpg", "48_Nguyen Thi Thu Hang_SD2.jpg", ""),
(49, "Nguyen Diem Hang", "VT1", "49_Nguyen Diem Hang_VT1.jpg", "49_Nguyen Diem Hang_VT1.jpg", ""),
(50, "Bui Thi Phuong", "VT2", "50_Bui Thi Phuong_VT2.jpg", "50_Bui Thi Phuong_VT2.jpg", ""),
(51, "Truong Dieu Linh", "VT1", "51_Truong Dieu Linh_VT1.jpg", "51_Truong Dieu Linh_VT1.jpg", ""),
(52, "Tran Thi Thu Trang", "VT1", "52_Tran Thi Thu Trang_VT1.jpg", "52_Tran Thi Thu Trang_VT1.jpg", ""),
(53, "Le Thi Van Trang", "VT2", "53_Le Thi Van Trang_VT2.jpg", "53_Le Thi Van Trang_VT2.jpg", ""),
(54, "Nguyen Thuy Linh", "VT2", "54_Nguyen Thuy Linh_VT2.jpg", "54_Nguyen Thuy Linh_VT2.jpg", ""),
(55, "Pham Thi Ly", "VT2", "55_Pham Thi Ly_VT2.jpg", "55_Pham Thi Ly_VT2.jpg", ""),
(56, "Phan Phuong Anh", "VT2", "56_Phan Phuong Anh_VT2.jpg", "56_Phan Phuong Anh_VT2.jpg", ""),
(57, "Hoang Thi Thuy Duong", "SD2", "57_Hoang Thi Thuy Duong_SD2.jpg", "57_Hoang Thi Thuy Duong_SD2.jpg", ""),
(58, "Nguyen Thuy Hoa", "VT2", "58_Nguyen Thuy Hoa_VT2.jpg", "58_Nguyen Thuy Hoa_VT2.jpg", ""),
(59, "Tran Thi Phuong Hue", "VT2", "59_Tran Thi Phuong Hue_VT2.jpg", "59_Tran Thi Phuong Hue_VT2.jpg", ""),
(60, "Tran Thi Thuy", "VT2", "60_Tran Thi Thuy_VT2.jpg", "60_Tran Thi Thuy_VT2.jpg", ""),
(61, "Luu Thi Kim Huyen", "SD3", "61_Luu Thi Kim Huyen_SD3.jpg", "61_Luu Thi Kim Huyen_SD3.jpg", ""),
(62, "Do Thi Dung", "Intern SD2", "62_Do Thi Dung_Intern SD2.jpg", "62_Do Thi Dung_Intern SD2.jpg", "");''')
    conn.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    # Only seed one
    # seed_db()
    # seed_user()
    users = query_db('select * from users', [], one=False)
    _ip = request.environ['REMOTE_ADDR']

    voted = query_db("SELECT * from vote where ip=?", [_ip], one=False)
    vote_left = MAX_VOTE - len(voted)
    voted_ids = [user[2] for user in voted]

    if users is None:
        print('No such user')
    # else:
    #     print(users)
    return render_template('index.html', ip=_ip, starLeft=vote_left, users=users, voted=voted_ids)

@app.route("/random")
def random():
    # Only seed one
    # seed_db()
    # seed_user()
    users = query_db('select * from users ORDER BY RANDOM()', [], one=False)
    _ip = request.environ['REMOTE_ADDR']

    voted = query_db("SELECT * from vote where ip=?", [_ip], one=False)
    vote_left = MAX_VOTE - len(voted)
    voted_ids = [user[2] for user in voted]

    if users is None:
        print('No such user')
    # else:
    #     print(users)
    return render_template('index.html', ip=_ip, starLeft=vote_left, users=users, voted=voted_ids)

@app.route("/show_vote")
def show_vote():
    votes = query_db('select * from vote', [], one=False)

    votes_result = []
    votes_result_key = {}
    for v in votes:
        if votes_result_key.has_key(v[2]):
            votes_result_key[v[2]] += 1
        else:
            votes_result_key[v[2]] = 1
    for id in votes_result_key:
        users = query_db('select name from users where id=?', [id], one=True)
        votes_result.append((users[0], votes_result_key[id]))
    print votes_result
    return render_template('showvote.html', votes=votes_result)

@app.route('/', methods = ['POST'])
def vote():
    conn = get_db()

    vote_user = request.form['user']
    unvote = request.form['unvote']
    vote_ip = request.environ['REMOTE_ADDR']

    vote_count = query_db("SELECT COUNT(*) from vote where ip=?", [vote_ip], one=False)[0][0]
    vote_left = MAX_VOTE - vote_count
    if vote_left > 0:
        if unvote == "No":
            conn.cursor().execute("INSERT INTO 'vote' ('ip', 'user') VALUES (?, ?)" , [vote_ip, vote_user])
        elif vote_left > 0:
            conn.cursor().execute("DELETE FROM 'vote' WHERE user=?" , [vote_user])
        conn.commit()
    else:
        return str(vote_left)

    return str(vote_left)
