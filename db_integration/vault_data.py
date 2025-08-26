import os
import hvac

def get_db_credentials_from_vault():
    """
    Authenticates with Vault using the GCP auth method and retrieves
    the database credentials.
    """
    try:
        # Get the Vault address from an environment variable
        vault_ip_addr = os.getenv('VAULT_IP_ADDR')
        vault_path = os.getenv('VAULT_PATH')
        
        if vault_ip_addr and vault_path:
            # Initialize the hvac client
            client = hvac.Client(url=vault_ip_addr)
        else:
            print("Was not able to retrieve vault address as env var")
            return None

        # Authenticate with the GCP auth method
        client.auth.gcp.login()
        
        if not client.is_authenticated():
            print("Failed to authenticate with Vault during login.")
            return None

        # Retrieve the secret
        read_response = client.secrets.kv.v2.read_secret_version(
            mount_point='secret', 
            path=vault_path
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