from data_extraction.handle_status_code import log_request

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

response = log_request(url)

if response is not None: 
    week = response.json()['week']
    events = response.json()['events']

    teamNames = []

    #retrieves all NFL team names and abbreviation on Bye week only weeks 5-14
    # for team in week["teamsOnBye"]:
    #     print(team['name'])
    #     print(team['abbreviation'])

    #retrieves the remaining NFL team names and abbreviation
    for event in events:
        for game in event["competitions"]:
            for team in game['competitors']:
                team_name = str(team['team']['abbreviation']) + " " + str(team['team']['name'])

                teamNames.append(team_name)
    teamNames.sort()


