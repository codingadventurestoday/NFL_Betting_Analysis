import mysql.connector


secret_db_password = "mikeVr@bel12"
secret_db_name = "draftKings_evaul"



def connect_to_db():
    conn = mysql.connector.connect(
        host='35.184.18.235',
        port=3306,
        user ='jeremyPhillips',
        password = secret_db_password,
        database = secret_db_name,
    )

    return conn