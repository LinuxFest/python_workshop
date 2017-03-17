"""
8th Linux Festival, Python Workshop
By Sina Baharlouie, Sajad Azami
May 2016
"""

# Install Mysql Db:
#   apt-get install python-dev libmysqlclient-dev
#   pip install MySQL-python
import MySQLdb as Mysql
import hashlib
import time
import sys


def get_connection():
    return Mysql.connect('localhost', 'root', 'p', 'python_tutorial_db')


def insert_user(username, email, phone, password):
    # Connect to database
    con = get_connection()
    try:
        current_time = int(time.time())  # unix time
        encrypted_password = hashlib.md5(password).hexdigest()  # password encryption
        data_array = (current_time, username, email, phone, encrypted_password)
        cursor = con.cursor()
        cursor.execute(
            """INSERT INTO `python_user` (created_at, username, email, phone, password)
               VALUES (%s, %s, %s, %s, %s)""", data_array)
        con.commit()
        return cursor.lastrowid

    except Mysql.Error, e:
        con.rollback()
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()


def find_user(user_id):
    # Connect to database
    con = get_connection()
    try:
        cursor = con.cursor()

        cursor.execute("""SELECT * FROM python_user WHERE id = %s""", (user_id,))

        return cursor.fetchone()

    except Mysql.Error, e:
        con.rollback()
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()


def update_username(user_id, username):
    # Connect to database
    con = get_connection()
    try:
        cursor = con.cursor()
        query = """UPDATE python_user SET username = %s WHERE id = %s"""
        data = (username, user_id)
        cursor.execute(query, data)

        con.commit()
        return

    except Mysql.Error, e:
        con.rollback()
        print "Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)

    finally:
        if con:
            con.close()


# insert_user("sina", "sinabaharlouei@yahoo.com", "09127112753", "sina")

print (find_user(1))

update_username(1, "sinabhr")

print (find_user(1))
