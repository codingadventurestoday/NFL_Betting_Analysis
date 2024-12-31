from data_extraction.draftkings_betting_data import betting_data
from data_extraction.teamInformation import week
from db_integration.connection import connect_to_db

conn = connect_to_db()

week = week["number"]
next_week = week + 1

myCursor = conn.cursor()

query_insert = """INSERT IGNORE INTO games (game_date, home_teamID, away_teamID, seasonID, week)
VALUES (%s, %s, %s, %s, %s)
"""

query_check_game_exist = """SELECT gameID FROM games WHERE game_date = %s AND home_teamID = %s AND away_teamID = %s"""
query_get_season = """SELECT seasonID FROM seasons WHERE start_date < %s AND end_date > %s;"""
query_get_teamID = """SELECT teamID FROM teams WHERE team_name = %s;"""

""" seasonID = Query into seasons table to retrieve the seasonID where startdate < game_date > enddate"""
game_date = betting_data[0]["date_of_game"]
myCursor.execute(query_get_season, (game_date, game_date))
seasonID = myCursor.fetchone()
seasonID = seasonID[0]

for amount, games in enumerate(betting_data):
    game_date = games["date_of_game"]
    home_team = games["home_team_name"]
    away_team = games["away_team_name"]

    myCursor.execute(query_get_teamID, (away_team,))
    away_teamID = myCursor.fetchone()
    away_teamID = away_teamID[0]

    myCursor.execute(query_get_teamID, (home_team,))
    home_teamID = myCursor.fetchone()
    home_teamID = home_teamID[0]

    if amount > 15:
      week = next_week   

    myCursor.execute(query_check_game_exist, (game_date, home_teamID, away_teamID))
    game_data = myCursor.fetchone()
    if game_data is None:    
        myCursor.execute(query_insert, (game_date, home_teamID, away_teamID, seasonID, week))
    else: 
        continue
    
conn.commit()

if myCursor:
    myCursor.close()

if conn:
    conn.close()