import requests
import json
from colorama import Fore, Style

# Function to send a POST request to create a URL


def post_recipes_create_url(url, include_tags, token, api_url):
    # Prepare data and headers for the POST request
    data = {'url': url, 'include_tags': include_tags}
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'}

    # Send a POST request to create a new recipe
    response = requests.post(
        f"{api_url}/api/recipes/create-url", data=json.dumps(data), headers=headers)

    # Print information about the response
    print(
        f"\n{Fore.GREEN}Created recipe - URL: {url}, Include Tags: {include_tags}, Status Code: {response.status_code}, Response: {response.text}{Style.RESET_ALL}")

    # Extract the recipe slug from the response
    slug = response.text.strip('"')

    # Check if the slug is a digit (indicating a duplicate)
    if slug[-1].isdigit():
        # Prompt the user to delete the duplicate recipe
        user_input_delete = input(
            f"\nDuplicate found! Do you want to delete it? (yes, no or blank): ").strip().lower()
        if user_input_delete == 'yes':
            # Call the delete_recipes function to delete the duplicate recipe
            delete_recipes(api_url, headers, slug)

# Function to send a DELETE request to delete a recipe


def delete_recipes(api_url, headers, slug):
    # Send a DELETE request to delete the specified recipe
    response = requests.delete(
        f"{api_url}/api/recipes/{slug}", headers=headers)

    # Print information about the deletion response
    print(
        f"\n{Fore.GREEN}Deleted {slug} - Status Code: {response.status_code}{Style.RESET_ALL}")
