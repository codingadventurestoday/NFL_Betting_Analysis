from ..data_extraction.teamInformation import teamNames

import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the database password
database_password = os.getenv('DATABASE_PASSWORD')

conn = mysql.connector.connect(
    host = "34.74.220.185",
    user = "root",
    port = 3307,
    password = database_password,
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