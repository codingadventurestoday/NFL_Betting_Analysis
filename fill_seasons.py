from retrieveSeasonData import yearInformation

import mysql.connector

conn = mysql.connector.connect(
    host='35.237.41.191',
    port= 3307,
    user='root',
    password='51M@yo54Hightower83Welker',
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