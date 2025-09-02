from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs

from datetime import datetime, timedelta

from convert_date import convert_date, check_starting_time
from change_sign_values import change_signs
from handle_status_code import log_request

""" Please note that the game times are in CUT time zone"""

betting_data = []

url = 'https://sportsbook.draftkings.com/leagues/football/nfl?category=game-lines&subcategory=game'    

#creates the timestamps for now and in two weeks
now = datetime.now()
two_weeks = timedelta(weeks=2)
cut_off_date = now + two_weeks 

now = str(now)
cut_off_date = str(cut_off_date)

now = now[:10]
cut_off_date = cut_off_date[:10]

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    page.wait_for_selector('div.cms-market-selector-content') 

    html_content = page.content()
    soup = bs(html_content, 'html.parser')
    # finds all the div elements which have games
    day_blocks = soup.findAll("div", class_="cb-static-parlay__wrapper")

    now = str(datetime.now())
    now = now[:10]

    for day_block in day_blocks:
        #gets the date for the current day of games
        game_date_element = day_block.find("span", class_="cb-event-cell__start-time")
        game_date_txt = game_date_element.get_text()

        if isinstance(game_date_txt, str) and len(game_date_txt) > 1:
            game_date_txt = game_date_txt.lower()
            formatted_date = convert_date(game_date_txt[:-7])
            start_time = game_date_txt[12:]
            date_of_game = check_starting_time(start_time, formatted_date)
        
        if cut_off_date < date_of_game:
            break
        
        # finds all the individual games occuring in the day
        game_blocks = day_block.findAll("div", class_="cb-market__template--2-columns")

        for game_block in game_blocks:
            game_data = {}

            game_data["date_collected"] = now
            game_data["date_of_game"] = date_of_game

            # finds the teams' name who are playing in this game
            teams = game_block.findAll("span", class_="cb-market__label-inner")

            away_team = teams[0].get_text()
            home_team = teams[1].get_text()

            game_data["away_team_name"] = away_team
            game_data["home_team_name"] = home_team

            # Finds all the bets related to this game
            bets = game_block.findAll("span", class_="cb-market__button-points")
            home_spread = bets[2].get_text()
            away_spread = bets[0].get_text()  
            over_under = bets[1].get_text()  

            game_data["away_spread"] = float(away_spread)
            game_data["home_spread"] = float(home_spread)
            game_data["over_under"] = float(over_under)
        
            #Finds all the odds related to this game
            odds = game_block.findAll("span", class_="cb-market__button-odds")

            away_spread_moneyline = odds[0].get_text()
            over_moneyline = odds[1].get_text()
            away_win_moneyline = odds[2].get_text()
            home_spread_moneyline = odds[3].get_text()
            under_moneyline = odds[4].get_text()
            home_win_moneyline = odds[5].get_text()

            game_data["away_spread_odds"] = away_spread_moneyline
            game_data["home_spread_odds"] = home_spread_moneyline
            game_data["over_odds"] = over_moneyline
            game_data["under_odds"] = under_moneyline
            game_data["moneyline_home"] = home_win_moneyline
            game_data["moneyline_away"] = away_win_moneyline

            betting_data.append(game_data)





"""
***data                attempted            collected
date_collected                              done
date_of_game           completed            done
away_team_name          away_team           done
away_spread             away_spread         done
home_spread             home_spread         done
home_team_name          home_team           done
over/under              over                done
over_odds               over_moneyline      done
under_odds              under_moneyline     done
home_spread_odds        home_spread_moneyline   done
away_spread_odds        away_spread_moneyline   done
home_moneyline          home_win_moneyline
away_moneyline          away_win_moneyline
"""