from handle_status_code import log_request

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = log_request(url)
if response is not None: 
    yearInformation = []

    nfl = response.json()["leagues"][0]

    year = nfl['season']['year']
    startDate = nfl['season']['startDate'][:10]
    endDate = nfl['season']['endDate'][:10]

    yearInformation.append(year)
    yearInformation.append(startDate)
    yearInformation.append(endDate)

"""
year INT
startDate DATE
endDate DATE
"""