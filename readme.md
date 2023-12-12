# Mealie API Custom Scripts

## Overview

This set of custom Python scripts is designed to interact with the Mealie API, providing additional functionality for managing recipes and more. Check it out!

## Prerequisites for all scripts

- Python 3.x
- [Requests](https://docs.python-requests.org/en/latest/) library (`pip install requests`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/panteLx/mealie_api_custom_scripts.git
   ```

2. Navigate to the project directory:

   ```bash
   cd mealie_api_custom_scripts
   ```

3. Make the script executable:

   ```bash
   chmod +x script_name.py
   ```

4. Install dependencies (if not already installed):

   ```bash
   pip install -r requirements/script_name.txt
   ```

## Script: create_recipe_bulk_with_tags.py

### Usage

1. **Authentication Setup**

   - The script uses an authentication token and API URL. If not already set, the script prompts the user to enter these details.
   - The authentication details are saved in a configuration file (`config/auth.json`) for future use.

2. **Create URLs**

   - The user is prompted to input a list of URLs separated by commas.
   - For each URL, a POST request is sent to the API to create a corresponding recipe URL.
   - If a duplicate is found, the user is prompted to delete it.

3. **Include Tags**

   - The user is prompted to specify whether to import original keywords as tags for the recipes.

### How to Run

1. Make the script executable:

   ```bash
   chmod +x create_recipe_bulk_with_tags.py
   ```

2. Run the script:

   ```bash
   ./create_recipe_bulk_with_tags.py
   ```

### Configuration

- Authentication details are stored in the `config/auth.json` file.

### Acknowledgments

- The script uses the [Requests](https://docs.python-requests.org/en/latest/) library for handling HTTP requests.

## License

This repository is licensed under the [GNU General Public License v3.0](LICENSE). Feel free to use, modify, and distribute it. If you encounter any issues or have suggestions, please create an issue in the [GitHub repository](https://github.com/panteLx/mealie_api_custom_scripts).
