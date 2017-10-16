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
(1, "Pham Thi Bich", "SD2", "01_Pham Thi Bich_SD2.jpg", "01_Pham Thi Bich_SD2.jpg", ""),
(2, "Nguyen Thu Phuong", "DP", "02_Nguyen Thu Phuong_Accountant_DP.jpg", "02_Nguyen Thu Phuong_Accountant_DP.jpg", ""),
(3, "Bui Hai Anh", "GA DP", "03_Bui Hai Anh_GA_DP.jpg", "03_Bui Hai Anh_GA_DP.jpg", ""),
(4, "Nguyen Kim Oanh", "VT", "04_Nguyen Kim Oanh_VT.jpg", "04_Nguyen Kim Oanh_VT.jpg", ""),
(5, "Tran Thi Thanh Nga", "VT", "05_Tran Thi Thanh Nga_VT.jpg", "05_Tran Thi Thanh Nga_VT.jpg", ""),
(6, "Khuong Thi Ngoan", "VT", "06_Khuong Thi Ngoan_VT.jpg", "06_Khuong Thi Ngoan_VT.jpg", ""),
(7, "To Thi Ha", "VT", "07_To Thi Ha_VT.jpg", "07_To Thi Ha_VT.jpg", ""),
(8, "Nguyen Minh Quyen", "VT", "08_Nguyen Minh Quyen_VT.jpg", "08_Nguyen Minh Quyen_VT.jpg", ""),
(9, "Nguyen Thi Thanh Quy", "VT", "09_Nguyen Thi Thanh Quy_VT.jpg", "09_Nguyen Thi Thanh Quy_VT.jpg", ""),
(10, "Do Hong Van", "VT", "10_Do Hong Van_VT.jpg", "10_Do Hong Van_VT.jpg", ""),
(11, "Dao Thu Trang", "VT", "11_Dao Thu Trang_VT.jpg", "11_Dao Thu Trang_VT.jpg", ""),
(12, "Hoang Hong Nhung", "VT", "12_Hoang Hong Nhung_VT.jpg", "12_Hoang Hong Nhung_VT.jpg", ""),
(13, "Nguyen Phuong Huyen", "SD1", "13_Nguyen Phuong Huyen_SD1.jpg", "13_Nguyen Phuong Huyen_SD1.jpg", ""),
(14, "Pham Nhu Ngoc", "DP", "14_Pham Nhu Ngoc_DP.jpg", "14_Pham Nhu Ngoc_DP.jpg", ""),
(15, "Than Thi Men", "VT", "15_Than Thi Men_VT.jpg", "15_Than Thi Men_VT.jpg", ""),
(16, "Do Thi Ngan", "VT", "16_Do Thi Ngan_VT.jpg", "16_Do Thi Ngan_VT.jpg", ""),
(17, "Hoang Thi Lan", "VT", "17_Hoang Thi Lan_VT.jpg", "17_Hoang Thi Lan_VT.jpg", ""),
(18, "Dang Thi Ngoc", "VT", "18_Dang Thi Ngoc_VT.jpg", "18_Dang Thi Ngoc_VT.jpg", ""),
(19, "Le Thi Thuy Diu", "VT", "19_Le Thi Thuy Diu_VT.jpg", "19_Le Thi Thuy Diu_VT.jpg", ""),
(20, "Vi Thi Huyen", "VT", "20_Vi Thi Huyen_VT.jpg", "20_Vi Thi Huyen_VT.jpg", ""),
(21, "Nguyen Thi Phuong", "VT", "21_Nguyen Thi Phuong_VT.jpg", "21_Nguyen Thi Phuong_VT.jpg", ""),
(22, "Do Thi Ngoc Bich", "VT", "22_Do Thi Ngoc Bich_VT.jpg", "22_Do Thi Ngoc Bich_VT.jpg", ""),
(23, "Pham Thi Thuy", "VT", "23_Pham Thi Thuy_VT.jpg", "23_Pham Thi Thuy_VT.jpg", ""),
(24, "Duong Thi Ho Hanh", "VT", "24_Duong Thi Ho Hanh_VT.jpg", "24_Duong Thi Ho Hanh_VT.jpg", ""),
(25, "Le Thi Trang", "VT", "25_Le Thi Trang_VT.jpg", "25_Le Thi Trang_VT.jpg", ""),
(26, "Lang Thi Thuy", "VT", "26_Lang Thi Thuy_VT.jpg", "26_Lang Thi Thuy_VT.jpg", ""),
(27, "Phan Thi Hoa", "DP", "27_Phan Thi Hoa_DP.jpg", "27_Phan Thi Hoa_DP.jpg", ""),
(28, "To Thi Van Anh", "VT", "28_To Thi Van Anh_VT.jpg", "28_To Thi Van Anh_VT.jpg", ""),
(29, "Truong Thi Hanh Phuc", "VT", "29_Truong Thi Hanh Phuc_VT.jpg", "29_Truong Thi Hanh Phuc_VT.jpg", ""),
(30, "Giap Thanh Huyen", "VT", "30_Giap Thanh Huyen_VT.jpg", "30_Giap Thanh Huyen_VT.jpg", ""),
(31, "Vu Thi My Dung", "DP", "31_Vu Thi My Dung_DP.jpg", "31_Vu Thi My Dung_DP.jpg", ""),
(32, "Bui Thi Lam", "VT", "32_Bui Thi Lam_VT.jpg", "32_Bui Thi Lam_VT.jpg", ""),
(33, "Nguyen Thi Thanh Na", "VT", "33_Nguyen Thi Thanh Na_VT.jpg", "33_Nguyen Thi Thanh Na_VT.jpg", ""),
(34, "Quach Ngoc Hien", "VT", "34_Quach Ngoc Hien_VT.jpg", "34_Quach Ngoc Hien_VT.jpg", ""),
(35, "Nguyen Van Huong", "VT", "35_Nguyen Van Huong_VT.jpg", "35_Nguyen Van Huong_VT.jpg", ""),
(36, "Phan Hoang Minh Thuy", "DP", "36_Phan Hoang Minh Thuy_DP.jpg", "36_Phan Hoang Minh Thuy_DP.jpg", ""),
(37, "Hoang Thi Luy", "VT", "37_Hoang Thi Luy_VT.jpg", "37_Hoang Thi Luy_VT.jpg", ""),
(38, "Do Thi Ngan", "VT", "38_Do Thi Ngan_VT.jpg", "38_Do Thi Ngan_VT.jpg", ""),
(39, "Pham Thi Phuong Dung", "VT", "39_Pham Thi Phuong Dung_VT.jpg", "39_Pham Thi Phuong Dung_VT.jpg", ""),
(40, "Dinh Thi Cam Le", "DP", "40_Dinh Thi Cam Le_DP.jpg", "40_Dinh Thi Cam Le_DP.jpg", ""),
(41, "Le Hong Thuy", "VT", "41_Le Hong Thuy_VT.jpg", "41_Le Hong Thuy_VT.jpg", ""),
(42, "Tran Thi Cham", "VT", "42_Tran Thi Cham_VT.jpg", "42_Tran Thi Cham_VT.jpg", ""),
(43, "Truong Thi Huyen Trang", "DP", "43_Truong Thi Huyen Trang_DP.jpg", "43_Truong Thi Huyen Trang_DP.jpg", "");''')
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

@app.route('/', methods = ['POST'])
def vote():
    conn = get_db()

    vote_user = request.form['user']
    unvote = request.form['unvote']
    vote_ip = request.environ['REMOTE_ADDR']

    vote_count = query_db("SELECT COUNT(*) from vote where ip=?", [vote_ip], one=False)[0][0]
    vote_left = MAX_VOTE - vote_count
    if unvote == "No" and vote_left > 0:
        conn.cursor().execute("INSERT INTO 'vote' ('ip', 'user') VALUES (?, ?)" , [vote_ip, vote_user])
    else:
        conn.cursor().execute("DELETE FROM 'vote' WHERE user=?" , [vote_user])
    conn.commit()

    return str(vote_left)
