from log.handle_status_code import log_request

url = "http://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard"

def teamInfo(url):
    response = log_request(url)

    if response: 

        week = response.json()['week']['number']
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
        return week, teamNames
    else:
        return None, None

week, teamNames = teamInfo(url)
