from retrieve_NFL_scores import games_outcome_list
import mysql.connector

conn = mysql.connector.connect(
    host = "35.237.41.191",
    port = 3307,
    user = "root",
    password = "51M@yo54Hightower83Welker",
    database = "historical_application_data",
)

myCursor = conn.cursor()
"""
Key: away_team
Value: string

Key: home_team 
Value: string

Key: away_team_score 
Value: int

Key: home_team_score 
Value: int
"""

"""
add fields to collumn's score_home and score_away to games that match 
away_team and home team with home_teamID and away_teamID (query to get IDs)
"""
query_team_id = """SELECT teamID FROM teams WHERE team_name = %s;"""
query_update = """UPDATE games
SET score_home = %s, score_away = %s
WHERE home_teamID = %s AND away_teamID = %s;"""

for game in games_outcome_list:
    home_team_name = game["home_team"]
    away_team_name = game["away_team"]
    home_team_score = game["home_team_score"]
    away_team_score = game["away_team_score"]

    myCursor.execute(query_team_id, (home_team_name,))
    home_teamID_tuple = myCursor.fetchone()
    home_teamID = home_teamID_tuple[0]

    myCursor.execute(query_team_id, (away_team_name,))
    away_teamID_tuple = myCursor.fetchone()
    away_teamID = away_teamID_tuple[0]
    
    myCursor.execute(query_update, (home_team_score, away_team_score, home_teamID, away_teamID))

conn.commit()

if myCursor:
    myCursor.close()

if conn:
    conn.close()