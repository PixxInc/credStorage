import os
import json

# Define the path for the JSON file
CREDENTIALS_FILE_PATH = r"C:\Users\sebas\!!Creds\main.json"

# Ensure the directory exists
os.makedirs(os.path.dirname(CREDENTIALS_FILE_PATH), exist_ok=True)

def store_credentials(name, credential):
    """
    Stores a credential in a JSON file at the predefined location.
    
    Args:
        name (str): The unique name for the credential.
        credential (str): The credential to store.
    """
    try:
        # Load existing credentials
        if os.path.exists(CREDENTIALS_FILE_PATH):
            with open(CREDENTIALS_FILE_PATH, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        # Add or update the credential
        data[name] = credential

        # Save the updated credentials
        with open(CREDENTIALS_FILE_PATH, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Credential '{name}' stored successfully.")

    except Exception as e:
        print(f"Failed to store credential: {str(e)}")

def get_all_credentials():
    """
    Retrieves all credentials from the JSON file.
    
    Returns:
        dict: A dictionary of all stored credentials, or a message if the file is empty or does not exist.
    """
    try:
        if not os.path.exists(CREDENTIALS_FILE_PATH):
            return "No credentials file found at {CREDENTIALS_FILE_PATH}."

        with open(CREDENTIALS_FILE_PATH, 'r') as file:
            data = json.load(file)

        if data:
            return data
        else:
            return "No credentials found."

    except Exception as e:
        return f"Failed to retrieve credentials: {str(e)}"
