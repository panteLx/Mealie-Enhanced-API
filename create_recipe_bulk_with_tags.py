#!/usr/bin/env python3

import requests
import json
import os
import sys

CONFIG_DIR = 'config'

# Function to save authentication input to a file


def save_auth_input_to_file(token, api_url, file_path=os.path.join(CONFIG_DIR, 'auth.json')):
    with open(file_path, 'w') as file:
        json.dump({'token': token, 'api_url': api_url}, file)

# Function to load authentication input from a file


def load_auth_input_from_file(file_path=os.path.join(CONFIG_DIR, 'auth.json')):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data.get('token'), data.get('api_url')
    return None, None

# Function to send a POST request to create a URL


def send_post_request(url, include_tags, token, api_url):
    data = {'url': url, 'include_tags': include_tags}
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'}

    response = requests.post(
        api_url+'/api/recipes/create-url', data=json.dumps(data), headers=headers)

    print(f"URL: {url}, Include Tags: {include_tags}, Status Code: {response.status_code}, Response: {response.text}")

    text = response.text.strip('"')
    if text[-1].isdigit():
        user_input_delete = input(
            "Duplicate found! Do you want to delete it? (yes, no or blank): ").strip().lower()
        if user_input_delete == 'yes':
            delete_response = requests.delete(
                api_url+'/api/recipes/'+text, headers=headers)
            print(
                f"Duplicate Deleted - Status Code: {delete_response.status_code}")

# Function to validate user input


def validate_input(prompt, valid_options=None, is_url=False, is_token=False):
    user_input = input(prompt).strip()

    if is_url and not user_input.startswith(("http://", "https://")):
        print(
            f"Invalid URL: {user_input} (URL should start with 'http://' or 'https://')")
        sys.exit()

    if is_token and not user_input:
        print("Token must not be empty")
        sys.exit()

    if valid_options and user_input not in valid_options:
        print(f"Invalid input. Must be one of {valid_options}")
        sys.exit()

    return user_input


# Ensure directories exist
os.makedirs(CONFIG_DIR, exist_ok=True)

# Load Auth-Token and API-URL or prompt for user auth input if not available
token, api_url = load_auth_input_from_file()
if not token:
    # Prompt the user to enter API-Token
    token = validate_input('Enter your API-Token: ', is_token=True).strip()
    save_auth_input_to_file(token, api_url)

if not api_url:
    # Prompt the user to enter API-URL
    api_url = validate_input(
        'Enter your API-URL (without path - e.g. http://mealie.dev:9925): ', is_url=True).strip()
    save_auth_input_to_file(token, api_url)

# Prompt for include tags input
include_tags = validate_input(
    'Do you want to import original keywords as tags? (true, false): ', valid_options=['true', 'false'])

# Prompt the user to input URLs separated by commas
user_input_urls = validate_input(
    'Enter URLs separated by commas: ', is_url=True).strip()

# Split the input into a list of URLs
url_array = user_input_urls.split(',')

for url in url_array:
    # Check if the URL starts with "http://" or "https://"
    if url.strip().startswith(("http://", "https://")):
        # Send a POST request for each URL
        send_post_request(url.strip(), include_tags, token, api_url)
    else:
        print(
            f"Invalid URL: {url} (URL should start with 'http://' or 'https://')")
