import sqlite3
from simplecrypt import encrypt, decrypt
import uuid

#first create the tables if it does not exist
def create_tables():
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS movies (
                        movie_id integer PRIMARY KEY AUTOINCREMENT,
                        name text NOT NULL,
                        run_time int NOT NULL,
                        genre text NOT NULL
                        );""")
        cur.execute("""CREATE TABLE IF NOT EXISTS bookings (
                        booking_id integer PRIMARY KEY AUTOINCREMENT,
                        movie_id integer NOT NULL,
                        date text NOT NULL,
                        time text NOT NULL,
                        row text NOT NULL,
                        seat int NOT NULL,
                        price real NOT NULL,
                        FOREIGN KEY (movie_id)
                            REFERENCES movies (id)
                                ON UPDATE SET NULL
                                ON DELETE SET NULL
                        );""")
    con.close()
    
#add movie to database
def insert_movie(name, run_time, genre):
    with sqlite3.connect('database.db') as con:
        con.execute("INSERT INTO movies (name, run_time, genre) VALUES (?, ?, ?)",
                      (name, run_time, genre))
    con.close()

#get all movies from database
def get_all_movies(order="movie_id"):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM movies ORDER BY {}".format(order))
        except sqlite3.OperationalError:
           cur.execute("SELECT * FROM movies")
        movies = cur.fetchall()
    con.close()
    return movies

#remove a movie from database
def remove_movie(movie_id):
    with sqlite3.connect('database.db') as con:
        con.execute("DELETE FROM movies WHERE movie_id = :id", {'id': movie_id})
    con.close()

#add booking to database
def insert_booking(movie, date, time, row, seat, price):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        cur.execute("SELECT movie_id FROM movies WHERE name=:name", {'name': movie})
        id = cur.fetchone()
        movie_id = id[0]
        cur.execute("""INSERT INTO bookings (movie_id, date, time, row, seat, price)
                        VALUES (?, ?, ?, ?, ?, ?)""", (movie_id, date, time, row, seat, price))
    con.close()

#get all bookings from database
def get_all_bookings(order="booking_id"):
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM bookings ORDER BY {}".format(order))
        except sqlite3.OperationalError:
           cur.execute("SELECT * FROM bookings")
        bookings = cur.fetchall()
    con.close()
    return bookings 

#remove a booking from database
def remove_booking(booking_id):
    with sqlite3.connect('database.db') as con:
        con.execute("DELETE FROM bookings WHERE booking_id=:id", {'id': booking_id})
    con.close()

#login system database
def create_logins_table():
    with sqlite3.connect('logins.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS logins (
                        login_id integer PRIMARY KEY AUTOINCREMENT,
                        username text NOT NULL,
                        password text NOT NULL
                        );""")
    con.close()

#encrypt password and username
def encrypt_pass(password):
    salt = uuid.uuid4().hex
    salted_password = password+salt
    return encrypt('password' , salted_password)

#decrypt password and username
def decrypt_pass(password):
    salted_password = decrypt('password', password).decode('utf8')
    password = salted_password[:-32]
    return password
    
#add login to database
def insert_login(username, password):
##    enc_password = encrypt_pass(password)
##    print(enc_password)
    with sqlite3.connect('logins.db') as con:
        con.execute("INSERT INTO logins (username, password) VALUES (?, ?)",
                      (username, password))
    con.close()

#get specific password from database
def get_password(username):
    with sqlite3.connect('logins.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT password FROM logins
                            WHERE username LIKE :username""", {'username': username})
        tuple_password = cur.fetchone()
    con.close()
    password = tuple_password[0]
    return password

#to check if a username is already taken
def find_username(username):
    with sqlite3.connect('logins.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT username FROM logins
                            WHERE username LIKE :username""", {'username': username})
        result = cur.fetchone()
        if result == None:
            return True
        else:
            return False
    con.close()

#update password in database
def update_password(username, new_password):
    enc_password = encypt_pass(new_password)
    with slqite3.connect('logins.db') as con:
        cur = cursor()
        cur.execute("""UPDATE logins
                            SET password = :password WHERE username = :username""",
                    {'password': enc_password, 'username': username})
    con.close()

#check admin password
def check_admin(username):
    with sqlite3.connect('admin.db') as con:
        cur = con.cursor()
        cur.execute("""SELECT password FROM admin
                            WHERE username LIKE :username""", {'username': username})
        tuple_password = cur.fetchone()
    con.close()
    password = tuple_password[0]
    return password
