import requests

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = requests.get(url)
"""
events --> list of games

data points needed:
awayTeam
homeTeam
homeScore
awayScore
weekOfSeason
dateOfGame
seasonYear
"""

events = response.json()['events']

weekOfSeason = events[0]["week"]['number']
date = events[0]["competitions"][0]['date'][:10]


#loops through all the teams that played in the week
for event in events:
    for game in event["competitions"]:
        for index, team in enumerate(game['competitors']):
            if index == 0:
                team_location = "home"
            elif index == 1:
                team_location = "away"
            print(team_location, team['team']['name'])

#loops through all the scores from that week
# for event in events:
#     for game in event["competitions"]:
#         for team in game['competitors']:
#             print(team['score'])

#loops through the dates of each game
# for event in events:
#     for game in event["competitions"]:
#         print(game['date'][:10])
