import mysql.connector

from vault_data import get_db_credentials_from_vault

vault_data_tuple = get_db_credentials_from_vault()

if vault_data_tuple:
    secret_db_password = vault_data_tuple[0]
    secret_db_name = vault_data_tuple[1]
else:
    raise ValueError("was not able to retrieve secrets from Vault Server")

# Connection to the remote MySQL server
conn = mysql.connector.connect(
    user="root",
    password= secret_db_password,
)

mycursor = conn.cursor()

create_database = f"CREATE DATABASE {secret_db_name}"

# Execute multiple queries
mycursor.execute(create_database)

conn.commit()
mycursor.close()
conn.close()