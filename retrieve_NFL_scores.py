from handle_status_code import log_request

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = log_request(url)

team_name_dict = {
    "LAR Rams" : "LA Rams",
    "LAC Chargers" : "LA Chargers",
    "NYG Giants" : "NY Giants",
    "NYJ Jets" : "NY Jets",
    "WSH Commanders" : "WAS Commanders",
}

if response is not None: 
    games_outcome_list = []

    events = response.json()['events']
    year = response.json()['season']['year']

    weekOfSeason = events[0]["week"]['number']

    #loops through all the teams that played in the week
    for event in events:
        for game in event["competitions"]:
            date_of_game = game['date'][:10]
            away_team = None
            home_team = None
            away_team_score = None
            home_team_score = None

            for index, team in enumerate(game['competitors']):
                game_outcome_dict = {}
                if team['homeAway'] == "home":
                    #team_location: home
                    home_team = team['team']['abbreviation'] + " " + team['team']['name']
                    if home_team in team_name_dict:
                        home_team = team_name_dict[home_team]
                    home_team_score = int(team['score'])
                elif team['homeAway'] == "away":
                    #team_location: away
                    away_team = team['team']['abbreviation'] + " " + team['team']['name']
                    if away_team in team_name_dict:
                        away_team = team_name_dict[away_team]
                    away_team_score = int(team['score'])

                    #Assign all collected info to the dict as K:V
                    game_outcome_dict["home_team_score"] = home_team_score
                    game_outcome_dict["away_team_score"] = away_team_score
                    game_outcome_dict["home_team"] = home_team
                    game_outcome_dict["away_team"] = away_team
                    game_outcome_dict["date_of_game"] = date_of_game
                    game_outcome_dict["season_week"] = weekOfSeason

                    games_outcome_list.append(game_outcome_dict)


"""game_outcome_dict data: 
Key: away_team
Value: string

Key: home_team 
Value: string

Key: away_team_score 
Value: int

Key: home_team_score 
Value: int

Key: date_of_game
Value: string

Key: weekOfSeason
Value: int

Key: seasonYear
Value: int
"""
