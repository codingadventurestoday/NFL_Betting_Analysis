import mysql.connector

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

database_password = os.getenv('DATABASE_PASSWORD')

# Connection to the remote MySQL server
conn = mysql.connector.connect(
    host="35.237.41.191",
    port= 3307,
    user="root",
    password=database_password,
)

mycursor = conn.cursor()

create_table = "CREATE DATABASE historical_application_data"
# Execute multiple queries
mycursor.execute(create_table)

conn.commit()
mycursor.close()
conn.close()