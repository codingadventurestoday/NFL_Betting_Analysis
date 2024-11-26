import requests

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = requests.get(url)
"""
week --> keys: "number"
events --> list of games
"""

week = response.json()['week']
weekOfSeason = response.json()['week']['number']

events = response.json()['events']



for index, line in enumerate(response.json()['events']):
    if index == 3: 
        print(line['date'][:10])
        break

