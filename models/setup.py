import sqlite3

CONN=sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()

def create_tables():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS teams (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            stadium TEXT NOT NULL,
            coach TEXT NOT NULL,
            team_numbers INTEGER,
            points INTEGER DEFAULT 0
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS matches (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            home_team_id INTEGER NOT NULL,
            away_team_id INTEGER NOT NULL,
            home_team_score INTEGER,
            away_team_score INTEGER,
            stadium TEXT,
            FOREIGN KEY(home_team_id) REFERENCES teams(id),
            FOREIGN KEY(away_team_id) REFERENCES teams(id)
        )
    ''')
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_name TEXT,
            team_id INTEGER,
            FOREIGN KEY(team_id) REFERENCES teams(id)
        )
    ''')
    CONN.commit()
