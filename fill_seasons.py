from data_extraction.retrieveSeasonData import yearInformation
from db_integration.connection import connect_to_db

conn = connect_to_db()

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