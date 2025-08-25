import mysql.connector

from vault_data import get_db_credentials_from_vault

vault_data_tuple = get_db_credentials_from_vault()

secret_db_password = vault_data_tuple[0]
secret_db_name = vault_data_tuple[1]

"""
Will be replaced by vault data

# Load environment variables from the .env file
load_dotenv()

# Access the database password
database_password = os.getenv('DATABASE_PASSWORD')
"""
def connect_to_db():
    conn = mysql.connector.connect(
        user ='root',
        password = secret_db_password,
        database = secret_db_name,
    )

    return conn