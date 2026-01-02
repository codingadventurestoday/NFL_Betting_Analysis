import os
from dotenv import load_dotenv

import mysql.connector


load_dotenv()


database_password = os.getenv("DATABASE_PASSWORD")
database_name = os.getenv("DATABASE_NAME")
database_user = os.getenv("USERNAME")
ip_address = os.getenv("IP_ADDRESS")



def connect_to_db():
    conn = mysql.connector.connect(
        host= ip_address,
        port=3306,
        user = database_user,
        password = database_password,
        database = database_name,
    )

    return conn