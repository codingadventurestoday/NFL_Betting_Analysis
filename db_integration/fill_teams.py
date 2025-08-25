import mysql.connector

from connection import connect_to_db
from ..data_extraction.teamInformation import teamNames

conn = connect_to_db()

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