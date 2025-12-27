import sys
import subprocess

from scrapping.draftkings_betting_data import betting_data

from database.connection import connect_to_db

conn = connect_to_db()
print("Successfully connected to database")
myCursor = conn.cursor()

query_get_teamID = """SELECT teamID FROM teams WHERE team_name = %s"""
query_get_gameID = """SELECT gameID FROM games WHERE home_teamID = %s AND away_teamID = %s"""
query_input = """INSERT INTO odds (gameID, date_gathered, over_under, over_odds, under_odds, home_spread, away_spread, home_spread_odds, away_spread_odds, home_moneyline, away_moneyline)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

team_name_dict = {
    "LA Rams": "LAR Rams",
    "LA Chargers": "LAC Chargers",
    "NY Giants": "NYG Giants",
    "NY Jets": "NYJ Jets",
    "WAS Commanders": "WSH Commanders",
}
print("retreiving data from draftkings")
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
    
    over_odds = over_odds.replace("−", "-")
    under_odds = under_odds.replace("−", "-")
    home_spread = str(home_spread).replace("−", "-")
    away_spread = str(away_spread).replace("−", "-")
    home_spread_odds = home_spread_odds.replace("−", "-")
    away_spread_odds = away_spread_odds.replace("−", "-")
    away_moneyline = away_moneyline.replace("−", "-")
    home_moneyline = home_moneyline.replace("−", "-")

    if home_team in team_name_dict:
        home_team = team_name_dict[home_team]
    if away_team in team_name_dict:
        away_team = team_name_dict[away_team]

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
    else:
        print(f"No gameID found for {away_team} and {home_team}. Run fill_game_initial file")
        print("exiting script: fill_odds. Please rerun")
        sys.exit()
    myCursor.execute(query_input, (gameID, date_gathered, over_under, over_odds, under_odds, home_spread, away_spread, home_spread_odds, away_spread_odds, home_moneyline, away_moneyline))

conn.commit()
print("Successfully added to database")

if myCursor:
    myCursor.close()

if conn:
    conn.close()