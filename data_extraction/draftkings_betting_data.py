from convert_date import convert_date, check_starting_time
from change_sign_values import change_signs
from handle_status_code import log_request
from get_text_recursively import get_text_from_span_element

from datetime import datetime

from bs4 import BeautifulSoup as bs
""" Please note that the game times are in CUT time zone"""

betting_data = []

url = 'https://sportsbook.draftkings.com/leagues/football/nfl'    

response = log_request(url)

if response is not None: 
    html_content = response.text
    soup = bs(html_content, 'html.parser') 

    now = str(datetime.now())
    now = now[:10]
    
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

        """Get betting data: home_team_name, away_team_name, over_under, moneyline_over, moneyline_under, 
        home_spread, moneyline_home_spread, away_spread, moneyline_away_spread, home_moneyline, away_moneyline
        """
        games = game_day_info_list[index].find_all("tr")

        "a list of the start times; includes any current game being played (if game is playing value is none)"
        start_time_list = game_day_info_list[index].find_all("span", "event-cell__start-time")

        for i in range(0, len(games), 2):
            game_data = {}
        
            start_time = start_time_list[i].get_text()
            date_of_game = check_starting_time(start_time, formatted_date)
            game_data["date_of_game"] = date_of_game
            game_data["date_collected"] = now

            td_elements_list = games[i].find_all("td", "sportsbook-table__column-row")
            away_odds_list = games[i].find_all("span", "sportsbook-odds")
            home_odds_list = games[i+1].find_all("span", "sportsbook-odds")

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

            away_spread_odds = away_odds_list[0]
            if away_spread_odds:
                away_spread_odds = away_spread_odds.get_text()
                if away_spread_odds.startswith("−"):
                    away_spread_odds = "-" + away_spread_odds[1:]
                game_data["away_spread_odds"] = away_spread_odds
    
            home_team_name = games[i+1].find("div", class_="event-cell__name-text")
            if home_team_name:
                home_team_name = home_team_name.get_text()
                game_data["home_team_name"] = home_team_name

            home_spread_odds = home_odds_list[0]
            if home_spread_odds:
                home_spread_odds = home_spread_odds.get_text()
                if home_spread_odds.startswith("−"):
                    home_spread_odds = "-" + home_spread_odds[1:]
                game_data["home_spread_odds"] = home_spread_odds

            over_under = td_elements_list[1].find("span", "sportsbook-outcome-cell__line")
            if over_under:
                over_under = over_under.get_text()
                game_data["over_under"] = float(over_under)

            over_odds = away_odds_list[1]
            if over_odds:
                over_odds = over_odds.get_text()
                if over_odds.startswith("−"):
                    over_odds = "-" + over_odds[1:]
                game_data["over_odds"] = over_odds

            under_odds = home_odds_list[1]
            if under_odds:
                under_odds = under_odds.get_text()
                if under_odds.startswith("−"):
                    under_odds = "-" + under_odds[1:]
                game_data["under_odds"] = under_odds

            moneyline_home = home_odds_list[2]
            if moneyline_home:
                moneyline_home = moneyline_home.get_text()
                if moneyline_home.startswith("−"):
                    moneyline_home= "-" + moneyline_home[1:]
                game_data["moneyline_home"] = moneyline_home

            moneyline_away = away_odds_list[2]
            if moneyline_away:
                moneyline_away = moneyline_away.get_text()
                if moneyline_away.startswith("−"):
                    moneyline_away = "-" + moneyline_away[1:]
                game_data["moneyline_away"] = moneyline_away

            betting_data.append(game_data)

"""TESTING: Delete after"""
# for testing, game in enumerate(betting_data):
#     print("")
#     print(f"this is game: {testing+1}")
#     for k, v in game.items():

#         print(f"This is the key: {k}")
#         print(f"this is the value: {v}")
#     print("")

"""Betting data contains: 
key: date_collected
value: str [format: yyyy-mm-dd]

key: date_of_game
value: str [format: yyyy-mm-dd]

key: away_team_name
Value: str

key: away_spread
Value: float

key: home_spread
Value: float

key: home_team_name
Value: str

key: over/under
Value: float

key: over_odds
Value: int

key: under_odds
Value: int

key: home_spread_odds
Value: int

key: away_spread_odds
Value: int

key: home_moneyline
Value: int

key: away_moneyline
Value: int
"""