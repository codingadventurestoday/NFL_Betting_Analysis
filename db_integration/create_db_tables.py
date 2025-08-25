import mysql.connector

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the database password
database_password = os.getenv('DATABASE_PASSWORD')

# Establish a connection to the remote MySQL server
conn = mysql.connector.connect(
    host="35.237.41.191",
    port= 3307,
    user="root",
    password=database_password,
    database="historical_application_data",
)

# Create a cursor object to execute SQL queries
mycursor = conn.cursor()

"""
Create table Odds 
Data: from draftkings_betting_data import betting_data
oddsID --> SMALLINT Primary Key
gameID --> SMALLINT Foreign Key
date_gathered --> DATE
over_under --> DECIMAL
over_odds --> SMALLINT
under_odds --> SMALLINT
home_spread --> DECIMAL
away_spread --> DECIMAL
home_spread_odds --> SMALLINT
away_spread_odds --> SMALLINT
home_moneyline --> SMALLINT
away_moneyline --> SMALLINT
"""
create_table_odds = """
CREATE TABLE IF NOT EXISTS odds (
    oddsID SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    gameID SMALLINT UNSIGNED,
    date_gathered DATE,
    over_under DECIMAL(4,1),
    over_odds SMALLINT,
    under_odds SMALLINT,
    home_spread DECIMAL(3,1),
    away_spread DECIMAL(3,1),
    home_spread_odds SMALLINT,
    away_spread_odds SMALLINT,
    home_moneyline SMALLINT,
    away_moneyline SMALLINT
);
"""


"""
Create table: season
Data: from retrieveSeasonData.py import yearInformation
seasonID TINYINT  UNSIGNED PRIMARY KEY
year SMALLINT    (index 0)
end_date DATE   (index 1)
start_date DATE   (index 2)
"""
create_table_season = """
CREATE TABLE IF NOT EXISTS seasons (
    seasonID TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    year SMALLINT UNSIGNED,
    start_date DATE,
    end_date DATE
);
"""


"""
Create table: games
Data: 
gameID SMALLINT primary key
game_date DATE
home_teamID TINYINT foreign key
away_teamID TINYINT foreign key
score_home TINYInt
score_away TINYINT
seasonID TINYINT foreign Key
week TINYINT
"""
create_table_games = """
CREATE TABLE IF NOT EXISTS games (
    gameID SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    game_date DATE,
    home_teamID TINYINT UNSIGNED,
    away_teamID TINYINT UNSIGNED,
    score_home TINYINT UNSIGNED,
    score_away TINYINT UNSIGNED,
    seasonID TINYINT UNSIGNED,
    week TINYINT UNSIGNED,
    FOREIGN KEY (home_teamID) REFERENCES teams(teamID),
    FOREIGN KEY (away_teamID) REFERENCES teams(teamID),
    FOREIGN KEY (seasonID) REFERENCES seasons(seasonID)
);
"""


"""
Create table: teams
Data: from teaminformation import teamNames (list)
teamID --> SMALLINT
team_name --> VARCHAR(15)
"""
create_table_teams = """
CREATE TABLE IF NOT EXISTS teams (
    teamID TINYINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    team_name VARCHAR(15)
);
"""

# Execute multiple queries
mycursor.execute(create_table_teams)
mycursor.execute(create_table_season)
mycursor.execute(create_table_games)
mycursor.execute(create_table_odds)

# Commit changes (not needed for DDL like CREATE, but good practice)
conn.commit()

# Once done, close the cursor and the connection
mycursor.close()
conn.close()