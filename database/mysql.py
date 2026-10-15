import mysql.connector
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


def connect():
    return mysql.connector.connect(
        host=MYSQL_HOST,
        port=MYSQL_PORT,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
        autocommit=True,
    )


def add_memory(session_id, role, content):
    db = connect()
    try:
        cur = db.cursor()
        cur.execute(
            "INSERT INTO memories(session_id, role, content) VALUES (%s, %s, %s)",
            (session_id, role, content),
        )
    finally:
        db.close()


def recent_memory(session_id, limit=12):
    db = connect()
    try:
        cur = db.cursor()
        cur.execute(
            "SELECT role, content FROM memories WHERE session_id=%s "
            "ORDER BY id DESC LIMIT %s",
            (session_id, limit),
        )
        return list(reversed(cur.fetchall()))
    finally:
        db.close()


def lookup_word(word):
    db = connect()
    try:
        cur = db.cursor(dictionary=True)
        cur.execute(
            "SELECT word, definition, part_of_speech, example_sentence "
            "FROM dictionary WHERE word=%s",
            (word.lower(),),
        )
        return cur.fetchone()
    finally:
        db.close()
