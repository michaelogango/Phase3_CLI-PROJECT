import sqlite3
from models.match import Match
from models.team import Team
from models.setup import create_tables
from models.news import News

# Database connection
CONN = sqlite3.connect("models/database/database.db")
CURSOR = CONN.cursor()


# Main menu
def show_menu():
    print("Kenyan Premier League (KPL) Match Planner CLI")
    print("1. Create a KPL team")
    print("2. Update team points")
    print("3. Check team positions")
    print("4. Update team news")
    print("5. Delete team news")    
    print("6. Update team matches")
    print("7. See fixtures")  
    print("8. Exit")   

def main():
    create_tables()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        #=====================================================================
        if choice == "1":
            name = input("Team name: ")
            stadium = input("Stadium name: ")
            coach = input("Coach name: ")
            team = int(input("Number of team members: "))
            team1 = Team(None, name, stadium, coach, team)
            team1.add_team()
         #==================================================================   
        elif choice == "2":
            teams = Team.get_all_teams()
            for team in teams:
                print(team)
            team_id = int(input("Enter team ID to update: "))
            new_points = int(input("Enter new points: "))
            team = next((t for t in teams if t.id == team_id), None)
            if team:
                team.update_points(new_points)
            else:
                print("Team not found.")
        #=======================================================================
        elif choice == "3":
            print("Teams ranked by points (highest to lowest):")
            teams = Team.get_all_teams(order_by_points=True)
            for team in teams:
                print(team)
        #=============================================================================
        elif choice=="4":
            teams=Team.get_all_teams()
            print("Available Teams:")
            for team in teams:
                print(f"ID: {team.id}, Name: {team.name}")


            team = int(input("What team(id): "))
            title = input("Artical Title: ")
            content = input("Content: ")
            author_name = input("Author name: ")
            artical = News(None,title,content,author_name,team)
            artical.new_news()
           

        elif choice=="5":

            articals=News.get_all_teams()
            print("Available Articals:")
            for artical in articals:
                print(f"ID: {artical.id}, Name: {artical.title}")
            
            id=input("Please put Artical Id:")
            News.drop_article(id)
          

        #================================================================================    
        elif choice == "6":
            teams = Team.get_all_teams()
            print("Available Teams:")
            for team in teams:
                print(f"ID: {team.id}, Name: {team.name}")
    
            date = input("Enter Date (dd-mm-yyyy): ")
            time = input("Enter Time (24H, HH:MM): ")

            try:
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

                    # Prevent selecting the same team as both home and away
                if home_team_id == away_team_id:
                    print("Home and Away teams cannot be the same. Please choose different teams.")
                    continue

                stadium = input("What Stadium will it be played in: ")

                # Add the match
                match = Match(None, date, time, home_team.id, away_team.id, None, None, stadium)
                match.add_match()
    
            except ValueError:
                print("Invalid input. Team IDs must be integers.")
        #================================================================================================
        elif choice=="7":
            Match.view_match()
#=========================================================================================================

        elif choice == "8":
            print("Exiting...")
            break
        else:
            print("Option not implemented yet.")

if __name__ == "__main__":
    main()
