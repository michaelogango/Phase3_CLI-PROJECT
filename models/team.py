import sqlite3

CONN=sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()


class Team:
    def __init__(self, id, name, stadium, coach, team, points=0):
        self.id = id
        self.name = name
        self.stadium = stadium
        self.coach = coach
        self.team_number = team
        self.points = points

    def add_team(self):
        # Validate team name
        if not self.name or len(self.name.strip()) < 3:
            print("Team name must be at least 3 characters long and not empty.")
            return

        # Check for duplicate team name (case-insensitive)
        sql_check = "SELECT COUNT(*) FROM teams WHERE LOWER(name) = LOWER(?)"
        CURSOR.execute(sql_check, (self.name,))
        if CURSOR.fetchone()[0] > 0:
            print(f"A team with the name '{self.name}' already exists.")
            return
        
        # Validate coach name
        if not self.coach or len(self.coach.strip()) < 3:
            print("Coach name must be at least 3 characters long and not empty.")
            return

        # Validate team number
        if not isinstance(self.team_number, int) or self.team_number <= 0:
            print("Team number must be a positive integer.")
            return

        # If all validations pass, insert the team into the database
        sql_insert = """
            INSERT INTO teams (name, stadium, coach, team, points)
            VALUES (?, ?, ?, ?, ?)
        """
        CURSOR.execute(sql_insert, (self.name, self.stadium, self.coach, self.team_number, self.points))
        CONN.commit()
        print(f"Successfully created team: {self.name}")

    @classmethod
    def get_all_teams(cls, order_by_points=False):
        if order_by_points:
            rows = CURSOR.execute("SELECT * FROM teams ORDER BY points DESC").fetchall()
        else:
            rows = CURSOR.execute("SELECT * FROM teams").fetchall()
        return [cls(*row) for row in rows]

    def update_points(self, new_points):
        sql = """
            UPDATE teams
            SET points = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (new_points, self.id))
        CONN.commit()
        print(f"Updated points for {self.name} to {new_points}")

    def __repr__(self):
        return f"Team(id={self.id}, name={self.name}, stadium={self.stadium}, coach={self.coach}, team_numbers={self.team_number}, points={self.points})"
