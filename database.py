import mysql.connector

db = mysql.connector (
    host = "",
    user = "",
    passwd = "",
    database = "",
)

mycursor = db.cursor()

mycursor.execute()