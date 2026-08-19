import sqlite3


def create_database():

    connect = sqlite3.connect("Data/database.db")
    cursor = connect.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS account(
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback(
        feedback_id INTEGER PRIMARY KEY,
        feedback TEXT,
        username TEXT,
        FOREIGN KEY (username) REFERENCES account(username)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS games(
    code TEXT PRIMARY KEY
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS config(
        question_id INTEGER PRIMARY KEY,
        question TEXT,
        answer TEXT,
        hint TEXT,
        difficulty TEXT CHECK(difficulty IN ("easy", "medium", "hard")),
        code TEXT,
        FOREIGN KEY (code) REFERENCES games(code)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS settings(
        username TEXT PRIMARY KEY,
        resolution TEXT CHECK(resolution IN (
        "720p", "1080p", "1440p", "2160p"
        )),
        fullscreen TEXT CHECK(fullscreen IN ("fullscreen", "windowed")),
        volume INTEGER,
        FOREIGN KEY (username) REFERENCES account(username)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS statistics(
        username TEXT PRIMARY KEY,
        questions_answered INTEGER,
        hints_used INTEGER,
        questions_correct INTEGER,
        FOREIGN KEY (username) REFERENCES account(username)
    )
    """)

    connect.commit()
    connect.close()
