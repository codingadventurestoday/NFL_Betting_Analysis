from teamInformation import teamNames

import mysql.connector

conn = mysql.connector.connect(
    host = "35.237.41.191",
    user = "root",
    port = 3307,
    password = "51M@yo54Hightower83Welker",
    database = "historical_application_data",
)

myCursor = conn.cursor()

query = f"""INSERT INTO teams (team_name)
VALUES (%s)
"""
for team in teamNames: 
    myCursor.execute(query, (team,))

conn.commit()

if myCursor:
    myCursor.close()

if conn:
    conn.close()