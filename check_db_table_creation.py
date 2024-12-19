import mysql.connector

conn = mysql.connector.connect(
    host="104.196.45.88",
    port= 3307,
    user="root",
    password="51M@yo54Hightower83Welker",
)

mycursor = conn.cursor()

# Check if database exists
database_name = "historical_application_data"

# Check if table exists in the specified database
def check_db_table(database_name, table_name):
    table_name = "your_table_name"
    mycursor.execute(f"""
        SELECT TABLE_NAME 
        FROM information_schema.TABLES 
        WHERE TABLE_SCHEMA = '{database_name}' 
        AND TABLE_NAME = '{table_name}'
    """)
    table_exists = mycursor.fetchone()

    if table_exists:
        print(f"Table '{table_name}' exists in database '{database_name}'.")
    else:
        print(f"Table '{table_name}' does not exist in database '{database_name}'.")

odds_table = check_db_table(database_name, "odds")
print("")
season_table = check_db_table(database_name, "season")
print("")
games_table = check_db_table(database_name, "games")
print("")
teams_table = check_db_table(database_name, "teams")


# Close the cursor and connection
mycursor.close()
conn.close()