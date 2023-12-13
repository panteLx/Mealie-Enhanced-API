import os
import json

CONFIG_DIR = "config"

# Ensure directories exist
os.makedirs(CONFIG_DIR, exist_ok=True)


# Function to save authentication input to a file
def save_auth_input_to_file(
    token, api_url, file_path=os.path.join(CONFIG_DIR, "auth.json")
):
    with open(file_path, "w") as file:
        # Write authentication information as JSON to the file
        json.dump({"token": token, "api_url": api_url}, file)


# Function to load authentication input from a file


def load_auth_input_from_file(file_path=os.path.join(CONFIG_DIR, "auth.json")):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            # Load JSON from the file
            data = json.load(file)
        return data.get("token"), data.get("api_url")
    return None, None
