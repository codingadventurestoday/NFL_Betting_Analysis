from convert_date import convert_date
#from handle_status_code import handle_status_code
from get_text_recursively import get_text_from_span_element

import requests

from bs4 import BeautifulSoup as bs

"""
********
1. problem: HTML has some dates/day of game not matching actual day
   i.e sunday night game is listed as monday 
   i.e. monday game might be listed as tuesda
********
"""

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
        formatted_date= convert_date(date)

    """Get betting data: home_team_name, away_team_name, over_under, home_spread, away_spread"""
    games = game_day_info_list[index].find_all("tr")

    for i in range(0, len(games), 2):
        game_data = {}
        game_data["date_of_game"] = formatted_date

        away_team_name = games[i].find("div", class_="event-call__name-text")
        if away_team_name:
            away_team_name = away_team_name.txt
            game_data["away_team_name"] = away_team_name

        away_spread = games[i].find("span", class_="")
        if away_spread:
            away_spread = away_spread.txt
            game_data["away_spread"] = away_spread

        home_team_name = games[i].find("div", class_="event-call__name-text")
        if home_team_name:
            home_team_name = home_team_name.txt
            game_data["home_team_name"] = home_team_name

        over_under = games[i].find("span", class_="")
        if over_under:
            over_under = over_under.txt
            game_data["over_under"] = over_under

        home_spread = games[i+1].find("span", class_="")
        if home_spread:
            home_spread = home_spread.txt
            game_data["home_spread"] = home_spread

        betting_data.append(game_data)

# for team in betting_data:
#     for k,v in team.items():
#         print(f"key: {k}")
#         print(f"value: {v}")
#         print("")
