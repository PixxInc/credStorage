import os
import json
import sys

# Define the path for the JSON file
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
    if len(sys.argv) < 2:
        print("Error: Missing action argument. Use 'store' or 'retrieve_all'.")
        sys.exit(1)

    action = sys.argv[1]
    
    if action == "store":
        if len(sys.argv) < 4:
            print("Error: Missing name or credential argument for storing.")
            sys.exit(1)
        name = sys.argv[2]
        credential = sys.argv[3]
        store_credentials(name, credential)
    elif action == "retrieve_all":
        credentials = get_all_credentials()
        print(credentials)
