from data_extraction.draftkings_betting_data import betting_data

from db_integration.connection import connect_to_db

conn = connect_to_db()

myCursor = conn.cursor()

query_get_teamID = """SELECT teamID FROM teams WHERE team_name = %s"""
query_get_gameID = """SELECT gameID FROM games WHERE home_teamID = %s AND away_teamID = %s"""
query_input = """INSERT INTO odds (gameID, date_gathered, over_under, over_odds, under_odds, home_spread, away_spread, home_spread_odds, away_spread_odds, home_moneyline, away_moneyline)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

for game in betting_data: 
    #not storted in db; used to get gameID
    away_team = game["away_team_name"]
    home_team = game["home_team_name"]

    date_gathered = game["date_collected"]
    over_under = game["over_under"]
    over_odds = game["over_odds"]
    under_odds = game["under_odds"]
    home_spread = game["home_spread"]
    away_spread = game["away_spread"]
    home_spread_odds = game["home_spread_odds"]
    away_spread_odds = game["away_spread_odds"]
    away_moneyline = game["moneyline_away"]
    home_moneyline = game["moneyline_home"]

    myCursor.execute(query_get_teamID, (away_team,))
    away_teamID = myCursor.fetchall()
    if away_teamID:
        away_teamID = away_teamID[0][0]

    myCursor.execute(query_get_teamID, (home_team,))
    home_teamID = myCursor.fetchall()
    if home_teamID:
        home_teamID = home_teamID[0][0]

    myCursor.execute(query_get_gameID, (home_teamID, away_teamID))
    gameID = myCursor.fetchall()
    if gameID: 
        gameID = gameID[0][0]

    myCursor.execute(query_input, (gameID, date_gathered, over_under, over_odds, under_odds, home_spread, away_spread, home_spread_odds, away_spread_odds, home_moneyline, away_moneyline))

conn.commit()

if myCursor:
    myCursor.close()

if conn:
    conn.close()