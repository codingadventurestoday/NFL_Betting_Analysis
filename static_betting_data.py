from convert_date import convert_date, check_starting_time
from change_sign_values import change_signs
#from handle_status_code import handle_status_code
from get_text_recursively import get_text_from_span_element

import requests

from bs4 import BeautifulSoup as bs
""" Please note that the game times are in CUT time zone"""

betting_data = []

url = 'https://sportsbook.draftkings.com/leagues/football/nfl'    

headers = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',  # Tells the server not to cache the response
    'Pragma': 'no-cache',         # Legacy header for cache control
    'Expires': '0',               # Ensures the cache is expired immediately
}

response = requests.get(url, headers=headers)
html_content = response.text
soup = bs(html_content, 'html.parser') 

"""use to get the date of the game"""
day_of_game_list = soup.find_all("th", "always-left")

"""use to get the match up and betting information for each game"""
game_day_info_list = soup.find_all("tbody", "sportsbook-table__body")

for index, day in enumerate(day_of_game_list):
    day = day.find("div", "sportsbook-table-header__title")
        #recursively travel the span elements to 
        #get the text from the nested span tags 
    date = get_text_from_span_element(day)

    if isinstance(date, str) and len(date) > 1:
        date = date.lower()
        formatted_date = convert_date(date)

    """Get betting data: home_team_name, away_team_name, over_under, home_spread, away_spread"""
    games = game_day_info_list[index].find_all("tr")

    "a list of the start times; includes any current game being played (if game is playing value is none)"
    start_time_list = game_day_info_list[index].find_all("span", "event-cell__start-time")

    for i in range(0, len(games), 2):
        game_data = {}
        
        start_time = start_time_list[i].get_text()
        date_of_game = check_starting_time(start_time, formatted_date)
        game_data["date_of_game"] = date_of_game

        td_elements_list = games[i].find_all("td", "sportsbook-table__column-row")
    
        away_team_name = games[i].find("div", class_="event-cell__name-text")
        if away_team_name:
            away_team_name = away_team_name.get_text()
            game_data["away_team_name"] = away_team_name
        
        away_spread = td_elements_list[0].find("span", "sportsbook-outcome-cell__line")
        if away_spread:
            away_spread = away_spread.get_text()
            home_spread = change_signs(away_spread)
            game_data["away_spread"] = float(away_spread)
            game_data["home_spread"] = float(home_spread)
    
        home_team_name = games[i+1].find("div", class_="event-cell__name-text")
        if home_team_name:
            home_team_name = home_team_name.get_text()
            game_data["home_team_name"] = home_team_name
    
        over_under = td_elements_list[1].find("span", "sportsbook-outcome-cell__line")
        if over_under:
            over_under = over_under.get_text()
            game_data["over_under"] = float(over_under)
        
        betting_data.append(game_data)

for testing, game in enumerate(betting_data):
    print("")
    print(f"this is game: {testing+1}")
    for k, v in game.items():

        print(f"This is the key: {k}")
        print(f"this is the value: {v}")
    print("")

"""Betting data contains: 
key: date_of_game
value: str [format: yyyy-mm-dd]

key: away_team_name
Value: str

key: away_spread
Value: float

key: home_spread
Value: int

key: home_team_name
Value: float

key: over/under
Value: float
"""