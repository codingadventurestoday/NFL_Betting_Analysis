import requests

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = requests.get(url)
"""
startDate (of season)
endDate (of season)
"""
nfl = response.json()["leagues"][0]
year = nfl['season']['year']
startDate = nfl['season']['startDate'][:10]
endDate = nfl['season']['endDate'][:10]

