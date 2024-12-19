import mysql.connector

# Connection to the remote MySQL server
conn = mysql.connector.connect(
    host="35.237.41.191",
    port= 3307,
    user="root",
    password="51M@yo54Hightower83Welker",
)

mycursor = conn.cursor()

create_table = "CREATE DATABASE historical_application_data"
# Execute multiple queries
mycursor.execute(create_table)

conn.commit()
mycursor.close()
conn.close()