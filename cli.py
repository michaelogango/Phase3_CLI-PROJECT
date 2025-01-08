import sqlite3
from models.match import Match
from models.team import Team
from models.setup import create_tables
from models.news import News

# Database connection
CONN = sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()



MENU_OPTIONS = [
    "Create a KPL team",
    "Update team points",
    "Check team positions",
    "Update team news",
    "Delete team news",
    "Update team matches",
    "See fixtures",
    "Exit"
]

def display_teams(teams):
    print("Available Teams:")
    for team in teams:
        print(f"ID: {team.id}, Name: {team.name}, Points: {team.points}")

def display_articles(articles):
    print("Available Articles:")
    for article in articles:
        print(f"ID: {article.id}, Title: {article.title}, Author: {article.author_name}")

# Main menu
def show_menu():
    print("Kenyan Premier League (KPL) Match Planner CLI")
    for idx, option in enumerate(MENU_OPTIONS, start=1):
        print(f"{idx}. {option}")

def main():
    create_tables()
    while True:
        show_menu()
        try:
            choice = int(input("Choose an option: "))
            if choice < 1 or choice > len(MENU_OPTIONS):
                raise ValueError("Invalid choice")
        except ValueError as e:
            print("Invalid input. Please choose a valid option.")
            continue

        # Mapping choice to actions
        if choice == 1:  # Create a KPL team
            name = input("Team name: ")
            stadium = input("Stadium name: ")
            coach = input("Coach name: ")
            team = int(input("Number of team members: "))
            team1 = Team(None, name, stadium, coach, team)
            team1.add_team()

        elif choice == 2:  # Update team points
            teams = Team.get_all_teams()
            display_teams(teams)
            try:
                team_id = int(input("Enter team ID to update: "))
                new_points = int(input("Enter new points: "))
                team = next((t for t in teams if t.id == team_id), None)
                if team:
                    team.update_points(new_points)
                else:
                    print("Team not found.")
            except ValueError:
                print("Invalid input. Team ID and points must be integers.")

        elif choice == 3:  # Check team positions
            print("Teams ranked by points (highest to lowest):")
            teams = Team.get_all_teams(order_by_points=True)
            display_teams(teams)

        elif choice == 4:  # Update team news
            teams = Team.get_all_teams()
            display_teams(teams)
            try:
                team_id = int(input("What team (ID): "))
                title = input("Article Title: ")
                content = input("Content: ")
                author_name = input("Author name: ")
                article = News(None, title, content, author_name, team_id)
                article.new_news()
            except ValueError:
                print("Invalid input. Team ID must be an integer.")

        elif choice == 5:  # Delete team news
            articles = News.get_all_articles()
            display_articles(articles)
            try:
                article_id = int(input("Enter Article ID to delete: "))
                News.drop_article(article_id)
            except ValueError:
                print("Invalid input. Article ID must be an integer.")

        elif choice == 6:  # Update team matches
            teams = Team.get_all_teams()
            display_teams(teams)
            try:
                date = input("Enter Date (dd-mm-yyyy): ")
                time = input("Enter Time (24H, HH:MM): ")

                # Choose home team
                home_team_id = int(input("Enter Home Team ID: "))
                home_team = next((t for t in teams if t.id == home_team_id), None)
                if not home_team:
                    print("Home team not found. Please enter a valid Team ID.")
                    continue

                # Choose away team
                away_team_id = int(input("Enter Away Team ID: "))
                away_team = next((t for t in teams if t.id == away_team_id), None)
                if not away_team:
                    print("Away team not found. Please enter a valid Team ID.")
                    continue

                if home_team_id == away_team_id:
                    print("Home and Away teams cannot be the same. Please choose different teams.")
                    continue

                stadium = input("What Stadium will it be played in: ")

                # Add the match
                match = Match(None, date, time, home_team.id, away_team.id, None, None, stadium)
                match.add_match()

            except ValueError:
                print("Invalid input. Team IDs must be integers.")

        elif choice == 7:  # See fixtures
            matches = Match.view_match()
            for match in matches:
                print(match)

        elif choice == 8:  # Exit
            print("Exiting...")
            break

if __name__ == "__main__":
    main()
