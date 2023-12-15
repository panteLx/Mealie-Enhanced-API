#!/usr/bin/env python3

from functions import *
from colorama import Fore, Style

# Load Auth-Token and API-URL or prompt for user auth input if not available
token, api_url = auth.load_auth_input_from_file()
if not token:
    # Prompt the user to enter API-Token
    token = validate.user_input("Enter your API-Token: ", is_text=True).strip()
    auth.save_auth_input_to_file(token, api_url)

if not api_url:
    # Prompt the user to enter API-URL
    api_url = validate.user_input(
        "\nEnter your API-URL (without path - e.g. http://mealie.dev:9925): ",
        is_url=True,
    ).strip()
    auth.save_auth_input_to_file(token, api_url)

# Check connection and auth data
get_user_self(api_url, token)

# Prompt for script selection input
selected_script = validate.user_input(
    f"""\nWhich script do you want to run? 
    1 - Bulk Create new recipes from URLs (with/without Tags)
    2 - {Fore.RED}ALPHA{Style.RESET_ALL} - Crawl custom website and create new recipes based on crawl results (with/without Tags)
    Select your option (1-2): """,
    valid_options=["1", "2"],
)

# Bulk Create new recipes from URLs (with/without Tags)
if selected_script == "1":
    # Prompt for include tags input
    include_tags = validate.user_input(
        "\nDo you want to import original keywords as tags? (true, false): ",
        valid_options=["true", "false"],
    )

    # Prompt the user to input URLs separated by commas
    user_input_urls = (
        validate.user_input("\nEnter URLs separated by commas: ", is_url=True)
        .strip()
        .split(",")
    )

    # Loop through each URL
    for url in user_input_urls:
        # Check if the URL starts with "http://" or "https://"
        if url.strip().startswith(("http://", "https://")):
            # Send a POST request for each URL
            print(f"{Fore.BLUE}\nChecking {url}{Style.RESET_ALL}")
            requests.post_recipes_create_url(url.strip(), include_tags, token, api_url)
        else:
            print(
                f"\n{Fore.RED}Invalid URL: {url} (URL should start with http:// or https://){Style.RESET_ALL}"
            )


# Crawl custom website and create new recipes based on crawl results (with/without Tags)
elif selected_script == "2":
    print(
        f"\n{Fore.RED}ALPHA - Crawler has a moderate chance to find bad URLs that can't be parsed! Mealie API will throw an error (400). However this won't break anything. {Style.RESET_ALL}"
    )

    # Prompt for url input
    url = validate.user_input(
        "\nInput your external recipe URL to crawl (e.g. https://www.kitchenstories.com/en/categories/breakfast): ",
        is_url=True,
    ).strip()

    # Prompt for keyword input
    keyword = validate.user_input(
        '\nEnter crawler keyword - Crawler will search for all results within your external recipe URL containing this keyword (e.g. "recipes"): ',
        is_text=True,
    )

    # Prompt for include tags input
    include_tags = validate.user_input(
        "\nDo you want to import original keywords as tags? (true, false): ",
        valid_options=["true", "false"],
    )

    # Extract recipe links
    links = crawler(url, f"/{keyword}/")

    # Loop through each URL and create POST
    for link in links:
        post_recipes_create_url(link, include_tags, token, api_url)
