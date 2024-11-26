import requests

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = requests.get(url)

week = response.json()['week']
events = response.json()['events']



#retrieves all NFL team names and abbreviation on Bye week
for team in week["teamsOnBye"]:
    print(team['name'])
    print(team['abbreviation'])

#retrieves the remaining NFL team names and abbreviation
for event in events:
    for game in event["competitions"]:
        for team in game['competitors']:
            print(team['team']['name'])
            print(team['team']['abbreviation'])
        break
# print(type(competitions))
"""teamName
teamAbb"""