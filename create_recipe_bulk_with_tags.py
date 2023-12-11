import requests
import json
import os
import sys

# Define directories
config_dir = 'config'

# Ensure directories exist
os.makedirs(config_dir, exist_ok=True)


def save_user_auth_input_to_file(token, api_url, file_path=config_dir+'/auth.json'):
    # Save user auth input to file
    with open(file_path, 'w') as file:
        json.dump({
            'token': token,
            'api_url': api_url
        }, file)


def load_user_auth_input_from_file(file_path=config_dir+'/auth.json'):
    # Check if the file exists
    if os.path.exists(file_path):
        # Load user auth input from file
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get('token'), data.get('api_url')
    else:
        return None, None


def send_post_request(url, include_tags, token, api_url):
    # Data for the POST request
    data = {
        'url': url,
        'include_tags': include_tags
    }

    # Headers for JSON data
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + token
    }

   # Send the POST request
    response = requests.post(
        api_url+'/api/recipes/create-url', data=json.dumps(data), headers=headers)

    # Print the response
    print(f"URL: {url}, Include Tags: {include_tags}, Status Code: {response.status_code}, Response: {response.text}")

    # Check if response.text ends with a number
    text = response.text.replace('"', '')
    if text and text[-1].isdigit():
        # user input delete request
        user_input_delete = input(
            "Duplicate found! Do you want to delete it? (yes, no): ")
        if user_input_delete.strip() != "" and user_input_delete.strip() in ['yes']:
            response = requests.delete(
                api_url+'/api/recipes/'+text, headers=headers)

            # Print the response
            print(
                f"Status Code: {response.status_code}")


# prompt for include tags input
user_input_include_tags = input(
    'Do you want to import original keywords as tags? (true, false): ')
if user_input_include_tags.strip() != "" and user_input_include_tags.strip() in ['true', 'false']:
    include_tags = user_input_include_tags
else:
    print(
        f"Input must not be empty and has to be true or false")
    sys.exit()


# Load Auth-Token and API-URL or prompt for user auth input if not available
token, api_url = load_user_auth_input_from_file()
if token is None:
    token = input('Enter your API-Token: ')
    if token.strip() != "":
        save_user_auth_input_to_file(token, api_url)
    else:
        print(
            f"Token must not be empty")
        sys.exit()

if api_url is None:
    api_url = input(
        'Enter your API-URL (without path - e.g. http://mealie.dev:9925): ')
    # Check if the URL starts with "http://" or "https://"
    if api_url.strip().startswith(("http://", "https://")):
        save_user_auth_input_to_file(token, api_url)
    else:
        print(
            f"Invalid URL: {api_url} (URL should start with 'http://' or 'https://')")
        sys.exit()

# Prompt the user to input URLs separated by commas
user_input_urls = input('Enter URLs separated by commas: ')

# Split the input into a list of URLs
url_array = user_input_urls.split(',')

# Check if url_array is None before iterating through it
if url_array is not None:
    # Iterate through the array and send POST requests
    for url in url_array:
        # Check if the URL starts with "http://" or "https://"
        if url.strip().startswith(("http://", "https://")):
            send_post_request(url.strip(), include_tags, token, api_url)
        else:
            print(
                f"Invalid URL: {url} (URL should start with 'http://' or 'https://')")
else:
    print("No URLs found.")
