import os
import hvac

def get_db_credentials_from_vault():
    """
    Authenticates with Vault using the GCP auth method and retrieves
    the database credentials.
    """
    try:
        # Get the Vault address from an environment variable
        vault_addr = os.getenv('VAULT_ADDR')
        
        # Initialize the hvac client
        client = hvac.Client(url=vault_addr)

        # Authenticate with the GCP auth method
        # The hvac client automatically detects the instance's identity
        # and uses it to authenticate.
        client.auth.gcp.login()
        
        if not client.is_authenticated():
            print("Failed to authenticate with Vault.")
            return None

        # Retrieve the secret
        read_response = client.secrets.kv.v2.read_secret_version(
            mount_point='secret',  # Or the name of your KV secret engine
            path='my-app/db'
        )
        # mount_point: path where your kv engine is: default is secret
        # remainder of the full path to the specific key you want read

        # Extract the credentials from the response as a dict type
        db_credentials_password = read_response['password']
        db_credentials_db_name = read_response['name']

        db_credentials_tuple = (db_credentials_password, db_credentials_db_name)    
        return db_credentials_tuple

    except Exception as e:
        print(f"An error occurred: {e}")
        return None