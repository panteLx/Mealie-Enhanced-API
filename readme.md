# Mealie Enhanced API

## Overview

This Python script is designed to interact with the Mealie API, providing additional functionality for managing recipes and more. Check it out!

## Prerequisites

- Python 3.x

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/panteLx/Mealie-Enhanced-API.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Mealie-Enhanced-API
   ```

3. Make the script executable:

   ```bash
   chmod +x run.py
   ```

## Usage

1. **Authentication Setup**

   - The script uses an authentication token and API URL. If not already set, the script prompts the user to enter these details.
   - The authentication details are saved in a configuration file (`config/auth.json`) for future use.

2. **Choose Script**

   - The user is prompted to choose which script he want's to run.

---

### 1 - Create a new recipe from URL (bulk or single) with/without Tags

- The user is prompted to input a list of URLs separated by commas.
- For each URL, a POST request is sent to the API to create a corresponding recipe URL.
- If a duplicate is found, the user is prompted to delete it.
- The user is prompted to specify whether to import original keywords as tags for the recipes.

### 2 - Coming soon

- Coming soon...

## How to Run

1. Make the script executable:

   ```bash
   chmod +x run.py
   ```

2. Run the script:

   ```bash
   ./run.py
   ```

### Configuration

- Authentication details are stored in the `config/auth.json` file.

### Acknowledgments

- The script uses the [Requests](https://docs.python-requests.org/en/latest/) library for handling HTTP requests.

## License

This repository is licensed under the [GNU General Public License v3.0](LICENSE). Feel free to use, modify, and distribute it. If you encounter any issues or have suggestions, please create an issue in the [GitHub repository](https://github.com/panteLx/Mealie-Enhanced-API).
