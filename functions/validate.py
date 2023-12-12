import sys
from colorama import Fore, Style

# Function to validate user input


def user_input(prompt, valid_options=None, is_url=False, is_token=False):
    # Get user input and remove leading/trailing whitespaces
    user_input = input(prompt).strip()

    # Check if input is a URL and starts with "http://" or "https://://"
    if is_url and not user_input.startswith(("http://", "https://")):
        print(
            f"\n{Fore.RED}Invalid URL: {user_input} (URL should start with 'http://' or 'https://'){Style.RESET_ALL}")
        sys.exit()

    # Check if the input is a token and is not empty
    if is_token and not user_input:
        print(f"\n{Fore.RED}Token must not be empty{Style.RESET_ALL}")
        sys.exit()

    # Check if the input is within the valid options (if provided)
    if valid_options and user_input not in valid_options:
        print(
            f"\n{Fore.RED}Invalid input. Must be one of {valid_options}{Style.RESET_ALL}")
        sys.exit()

    # Return the validated user input
    return user_input
