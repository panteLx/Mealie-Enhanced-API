# Mealie Enhanced API

## Overview

This Python script is designed to interact with the Mealie API, providing additional functionality for managing recipes and more.

It does not include any functions that you can achieve with the standard Mealie API.

Happy cooking with Mealie! 🍲

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

4. Install dependencies (if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Authentication Setup**

   - The script uses an authentication token and API URL. If not already set, the script prompts the user to enter these details.
   - The authentication details are saved in a configuration file (`config/auth.json`) for future use.

2. **Choose Script**

   - You will be prompted to choose which script you want to run.

## Available Scripts

1. **Create a new recipe from URL (bulk or single) with/without Tags**

   - You will be prompted to input a list of URLs separated by commas.
   - For each URL, a POST request is sent to the API to create a corresponding recipe URL.
   - If a duplicate is found, you will be prompted to delete it.
   - You will be prompted to specify whether to import original keywords as tags for the recipes.

2. **Coming soon**

   - Coming soon...

## How to Run

1. Run the script:

   ```bash
   ./run.py
   ```

## Configuration

- Authentication details are stored in the `config/auth.json` file.

## Documentation

- [Mealie API Docs](https://nightly.mealie.io/api/redoc/) check out the API Docs to learn more about the Mealie API
- [Mealie Getting Started](https://nightly.mealie.io/documentation/getting-started/introduction/) learn more about Mealie

## Acknowledgments

- The script uses the [Requests](https://docs.python-requests.org/en/latest/) library (version 2.31.0) for handling HTTP requests.
- [Certifi](https://pypi.org/project/certifi/) (version 2023.11.17) for providing a curated collection of Root Certificates for validating SSL certificates.
- [Charset-normalizer](https://pypi.org/project/charset-normalizer/) (version 3.3.2) for normalizing Unicode strings and character sets.
- [Colorama](https://pypi.org/project/colorama/) (version 0.4.6) for adding colored output to the terminal.
- [Idna](https://pypi.org/project/idna/) (version 3.6) for handling Internationalized Domain Names in Applications.
- [Urllib3](https://pypi.org/project/urllib3/) (version 2.1.0) for handling HTTP requests.

## License

This repository is licensed under the [GNU General Public License v3.0](LICENSE). Feel free to use, modify, and distribute it. If you encounter any issues or have suggestions, please create an issue in the [GitHub repository](https://github.com/panteLx/Mealie-Enhanced-API).
