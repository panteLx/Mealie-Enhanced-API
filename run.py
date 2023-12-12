#!/usr/bin/env python

from functions import *
from colorama import Fore, Style

# Load Auth-Token and API-URL or prompt for user auth input if not available
token, api_url = auth.load_auth_input_from_file()
if not token:
    # Prompt the user to enter API-Token
    token = validate.user_input(
        'Enter your API-Token: ', is_token=True).strip()
    auth.save_auth_input_to_file(token, api_url)

if not api_url:
    # Prompt the user to enter API-URL
    api_url = validate.user_input(
        '\nEnter your API-URL (without path - e.g. http://mealie.dev:9925): ', is_url=True).strip()
    auth.save_auth_input_to_file(token, api_url)

# Prompt for script selection input
selected_script = validate.user_input(
    """\nWhich script do you want to run? 
    1 - Bulk Create new recipes from URLs (with/without Tags)
    2 - Crawl custom website and create new recipes based on crawl results (with/without Tags)
    Select your option (1-2): """, valid_options=["1", "2"])

if selected_script == "1":
    # Prompt for include tags input
    include_tags = validate.user_input(
        '\nDo you want to import original keywords as tags? (true, false): ', valid_options=['true', 'false'])

    # Prompt the user to input URLs separated by commas
    user_input_urls = validate.user_input(
        '\nEnter URLs separated by commas: ', is_url=True).strip().split(',')

    # Loop through each URL
    for url in user_input_urls:
        # Check if the URL starts with "http://" or "https://"
        if url.strip().startswith(("http://", "https://")):
            # Send a POST request for each URL
            print(f"{Fore.BLUE}\nChecking {url}{Style.RESET_ALL}")
            requests.post_recipes_create_url(
                url.strip(), include_tags, token, api_url)
        else:
            print(
                f"\n{Fore.RED}Invalid URL: {url} (URL should start with 'http://' or 'https://'){Style.RESET_ALL}")

elif selected_script == "2":
   # Prompt for category input
    category = validate.user_input(
        '\nWhich category should I crawl (fruhstuck, abendessen, mittagessen, dessert): ', valid_options=['fruhstuck', 'abendessen', 'mittagessen', 'dessert'])

    # Prompt for include tags input
    include_tags = validate.user_input(
        '\nDo you want to import original keywords as tags? (true, false): ', valid_options=['true', 'false'])

    base_url = "https://www.kitchenstories.com/de/kategorien/"

    # Extract recipe links
    links = crawler(base_url, category, '/rezepte/')

    # Loop through each URL and create POST
    for link in links:
        post_recipes_create_url(link, include_tags, token, api_url)
