from ..data_extraction.retrieveSeasonData import yearInformation

import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the database password
database_password = os.getenv('DATABASE_PASSWORD')

conn = mysql.connector.connect(
    host='35.237.41.191',
    port= 3307,
    user='root',
    password=database_password,
    database='historical_application_data',
)

year = yearInformation[0]
start_of_season = yearInformation[1]
end_of_season = yearInformation[2]

query = f"""
INSERT INTO seasons (year, start_date, end_date)
VALUES (%s, %s, %s);
"""

myCursor = conn.cursor()

myCursor.execute(query, (year, start_of_season, end_of_season))

conn.commit()

myCursor.close()
conn.close()