import sqlite3
import re

CONN=sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()

class Match():

     def __init__(self, id, date, time, home_team_id, away_team_id,home_team_score=None,away_team_score=None, stadium=None ):
        self.id = id
        self.date = date
        self.time = time
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.home_team_score=home_team_score
        self.away_team_score=away_team_score
        self.stadium=stadium

     def add_match(self):

        if not re.match(r'^\d{2}-\d{2}-\d{4}$', self.date):
            print("Invalid date format. Please use dd-mm-yyyy.")
            return
    
        # Validate time format
        if not re.match(r'^\d{2}:\d{2}$', self.time):
            print("Invalid time format. Please use HH:MM.")
            return
        try:
        # If validations pass, insert into the database
            CURSOR.execute("""
            INSERT INTO match (date, time, home_team_id, away_team_id, stadium)
            VALUES (?, ?, ?, ?, ?)
        """, (self.date, self.time, self.home_team_id, self.away_team_id, self.stadium))
            CONN.commit()
            print("Match added successfully.")
        except Exception as e:
            print("An error occurred:", e)

     def update_match_score(id, home_team_score, away_team_score):
        CURSOR.execute("""
        UPDATE match
        SET home_team_score = ?, away_team_score = ?
        WHERE id = ?
    """, (home_team_score, away_team_score,id))
    
    # Update points based on match result
        CURSOR.execute("SELECT home_team_id, away_team_id FROM match WHERE id = ?", (id,))
        home_team_id, away_team_id = CURSOR.fetchone()

        if home_team_score > away_team_score:
            CURSOR.execute("UPDATE teams SET points = points + 3 WHERE id = ?", (home_team_id,))
        elif home_team_score < away_team_score:
            CURSOR.execute("UPDATE teams SET points = points + 3 WHERE id = ?", (away_team_id,))
        else:
            CURSOR.execute("UPDATE teams SET points = points + 1 WHERE id IN (?, ?)", (home_team_id, away_team_id))
    
        CONN.commit()
        print("Match score updated, and team points adjusted.")

     def view_match():
        CURSOR.execute("""
        SELECT m.id, t1.name AS home_team, t2.name AS away_team, m.date, m.time, m.stadium
        FROM match m
        JOIN teams t1 ON m.home_team_id = t1.id
        JOIN teams t2 ON m.away_team_id = t2.id
    """)
        matches = CURSOR.fetchall()
        print("Matches:")
        for match in matches:
            print(f"ID: {match[0]}, {match[1]} vs {match[2]}, Date: {match[3]}, Time: {match[4]}, Stadium: {match[5]}")

#Match.add_match("22-12-2024","12:00pm",3,2,"Nyayo National Stadium")

# Match.update_match_score(3,1,2)

#print(Match.view_match())


