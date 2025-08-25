import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Access the database password
database_password = os.getenv('DATABASE_PASSWORD')

def connect_to_db():
    conn = mysql.connector.connect(
        user ='root',
        password = database_password,
        database ='historical_application_data',
    )

    return conn