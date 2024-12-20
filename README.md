# Phase3_CLI-PROJECT
# Kenyan Premier League (KPL) Match Planner CLI

## Purpose of the Application
The Kenyan Premier League (KPL) Match Planner CLI is a command-line application designed to help manage and plan football activities for teams in the Kenyan Premier League. It enables users to:

- Create and manage KPL teams.
- Update team points based on performance.
- View team standings ranked by points.
- Add, update, and delete team news articles.
- Schedule and manage match fixtures.
- View a list of upcoming matches (fixtures).

This tool is ideal for league organizers, football enthusiasts, and team managers who need a straightforward way to handle league operations.

---

## Things to Install

### Prerequisites
Ensure you have the following installed on your system:

1. **Python**: Version 3.7 or higher.
2. **SQLite3**: Built-in with Python but ensure it is properly set up.

### Required Python Libraries
No external libraries are required for this application. However, you must have access to SQLite3 through Python.

### Database Initialization
The database file (`database.db`) and its schema are automatically created when you run the application for the first time using the `create_tables` function in `models/setup.py`.

---

## How to Use the Application

### Step 1: Run the Application
Execute the following command in your terminal:

```bash
python cli.py
```

### Step 2: Navigate the Main Menu
You will see the following menu options:

1. **Create a KPL team**: Add a new team to the league.
2. **Update team points**: Modify the points for an existing team.
3. **Check team positions**: View a ranked list of teams by their points.
4. **Update team news**: Add news articles for a team.
5. **Delete team news**: Remove an existing news article.
6. **Update team matches**: Schedule or modify match details.
7. **See fixtures**: View a list of scheduled matches.
8. **Exit**: Exit the application.

---

## Explanation of Each User Input

### **1. Create a KPL team**
- **Team name**: Name of the football team.
- **Stadium name**: The home stadium for the team.
- **Coach name**: The team's head coach.
- **Number of team members**: Total players on the team.

**Expected Outcome**: A new team is added to the league.
**Validation**: System checks the team name and sees if there is one already, if there is, it will throw an error

### **2. Update team points**
- **Team ID**: Select the team by its unique ID.
- **New points**: Enter the updated points for the team.

**Expected Outcome**: The team's points are updated in the database.

### **3. Check team positions**
- No user input required.

**Expected Outcome**: A ranked list of teams from highest to lowest points is displayed.

### **4. Update team news**
- **Team ID**: Choose a team by its unique ID.
- **Article Title**: Title of the news article.
- **Content**: Main content of the article.
- **Author name**: Name of the article's author.

**Expected Outcome**: A news article is added to the team’s profile.

### **5. Delete team news**
- **Article ID**: ID of the article to delete.

**Expected Outcome**: The selected news article is removed.

### **6. Update team matches**
- **Date**: Match date in `dd-mm-yyyy` format.
- **Time**: Match time in `HH:MM` (24-hour format).
- **Home Team ID**: ID of the home team.
- **Away Team ID**: ID of the away team.
- **Stadium**: The stadium where the match will be played.

**Expected Outcome**: The match details are stored in the database.

### **7. See fixtures**
- No user input required.

**Expected Outcome**: A list of all scheduled matches is displayed.

### **8. Exit**
- No user input required.

**Expected Outcome**: The application closes.

---

## Example Team Setup
Here is an example of a team setup you can use:

- **Team Name**: Gor Mahia
- **Stadium**: Nyayo National Stadium
- **Coach**: Jonathan Njoroge
- **Number of Team Members**: 22

---

## Example News Article
Here is an example news article you can create:

- **Title**: Gor Mahia Wins Big!
- **Content**: Gor Mahia secures a decisive 3-0 victory against AFC Leopards in the weekend derby.
- **Author Name**: John Doe

---

## What to Expect from User Inputs
1. If invalid inputs are provided (e.g., entering a string for team points), the application will prompt you to re-enter the data.
2. When adding matches, you cannot select the same team as both home and away teams.
3. On attempting to delete a non-existent news article, an error message will be displayed.

---

## Additional Notes
1. Ensure that all IDs entered correspond to existing database records.
2. The database is persistent; any data you add will remain even after the application is closed and reopened.
3. If you need the ID's for the different teams the application will show you the IDs and the corrisponding name

---

Enjoy managing your Kenyan Premier League with the KPL Match Planner CLI!

