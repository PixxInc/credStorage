import os
import json

# Path for the JSON file
CREDENTIALS_FILE_PATH = r"C:\Users\sebas\!!Creds\main.json"

# Ensure the directory exists
os.makedirs(os.path.dirname(CREDENTIALS_FILE_PATH), exist_ok=True)

def store_credentials(name, credential):
    """ Stores a credential in a JSON file. """
    try:
        if os.path.exists(CREDENTIALS_FILE_PATH):
            with open(CREDENTIALS_FILE_PATH, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        data[name] = credential

        with open(CREDENTIALS_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Credential '{name}' stored successfully.")
    except Exception as e:
        print(f"Failed to store credential: {str(e)}")

def get_all_credentials():
    """ Retrieves all credentials from the JSON file. """
    try:
        if not os.path.exists(CREDENTIALS_FILE_PATH):
            return "No credentials file found."

        with open(CREDENTIALS_FILE_PATH, 'r') as file:
            data = json.load(file)
        return data if data else "No credentials found."
    except Exception as e:
        return f"Failed to retrieve credentials: {str(e)}"

if __name__ == "__main__":
    action = os.getenv('ACTION')
    name = os.getenv('NAME')
    credential = os.getenv('CREDENTIAL')

    if not action:
        print("Error: Missing 'ACTION' environment variable. Please include 'store' or 'retrieve_all'.")
        sys.exit(1)

    if action == "store":
        if not name or not credential:
            print("Error: 'NAME' and 'CREDENTIAL' environment variables are required for storing.")
            sys.exit(1)
        store_credentials(name, credential)
    elif action == "retrieve_all":
        credentials = get_all_credentials()
        print(credentials)
    else:
        print("Error: Invalid 'ACTION' value. Use 'store' or 'retrieve_all'.")
        sys.exit(1)
