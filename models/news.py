import sqlite3

CONN = sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()

class News:

    def __init__(self, id, title, content, author_name, team):
        self.id = id
        self.title = title
        self.content = content
        self.author_name = author_name
        self.team = team

    def new_news(self):
        """
        This function adds new articles into the news table.
        """
        sql = """
            INSERT INTO news(title, content, author_name, team)
            VALUES(?,?,?,?)
            """
        CURSOR.execute(sql, (self.title, self.content, self.author_name, self.team))
        CONN.commit()
        print(f"You have successfully created a new article called: {self.title}")

    @staticmethod
    def drop_article(id):
        """
    This function deletes an article from the news table by its ID.
        """
    # Retrieve the title of the article before deleting
        CURSOR.execute("SELECT title FROM news WHERE id = ?", (id,))
        result = CURSOR.fetchone()

        if result is None:
            print(f"No article found with ID {id}.")
            return

        title = result[0]  # Extract the title from the query result

        # Proceed to delete the article
        sql = "DELETE FROM news WHERE id = ?"
        CURSOR.execute(sql, (id,))
        CONN.commit()
        print(f"The article with ID {id}, titled '{title}', has been successfully deleted.")


    @classmethod
    def get_all_teams(cls, order_by_points=False):
        if order_by_points:
            rows = CURSOR.execute("SELECT * FROM news ORDER BY points DESC").fetchall()
        else:
            rows = CURSOR.execute("SELECT * FROM news").fetchall()
        return [cls(*row) for row in rows]
