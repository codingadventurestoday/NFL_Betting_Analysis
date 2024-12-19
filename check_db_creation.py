import mysql.connector

conn = mysql.connector.connect(
    host="35.237.41.191",
    port= 3307,
    user="root",
    password="51M@yo54Hightower83Welker",
)

mycursor = conn.cursor()

# Check if database exists
database_name = "historical_application_data"

mycursor.execute(f"""
    SELECT SCHEMA_NAME 
    FROM information_schema.SCHEMATA 
    WHERE SCHEMA_NAME = '{database_name}'
""")
db_exists = mycursor.fetchone()

if db_exists:
    print(f"Database '{database_name}' exists.")
else:
    print(f"Database '{database_name}' does not exist.")

# Close the cursor and connection
mycursor.close()
conn.close()