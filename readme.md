# Mealie API Custom Scripts

Custom Python Scripts using the Mealie API

## Features

create_recipe_bulk_with_tags:

- Bulk creation of new recipes
- Specify if you want to import original keywords as tags
- Saved auth variables (otherwise you have to input `MEALIE_API_TOKEN` and `http://MEALIE_API_URL:PORT` every time)

## Installation

> Python is required in order to use the scripts.

Clone the project

```bash
  git clone https://github.com/panteLx/mealie_api_custom_scripts
```

Go to the project directory

```bash
  cd mealie_api_custom_scripts
```

Install required dependencies

```bash
  pip install requests
```

## Usage

Run the Script with the following command

```
python SCRIPT_NAME.py
```

### Example for create_recipe_bulk_with_tags

Run `python create_recipe_bulk_with_tags.py`

Output:

```
Do you want to import original keywords as tags? (true, false): true

Enter your API-Token: MEALIE_API_TOKEN

Enter your API-URL (without path - e.g. http://mealie.dev:9925): http://MEALIE_API_URL:PORT

Enter URLs separated by commas: http://BEST_CAKES_DOMAIN_1, http://BEST_CAKES_DOMAIN_2

URL: https://BEST_CAKES_DOMAIN_1, Include Tags: true, Status Code: 201, Response: "best_cake_on_the_planet_1"
URL: https://BEST_CAKES_DOMAIN_2, Include Tags: true, Status Code: 201, Response: "best_cake_on_the_planet_2"
```

The Script will save your `MEALIE_API_TOKEN` and `http://MEALIE_API_URL:PORT` in the `config/auth.json` file.

## Roadmap

- Add more scripts that uses the Mealie API

- Enhance exisiting scripts

## Feedback & Support

Feel free to open up an Issue if you have questions or experienced any bugs/errors.

## Contributing

Contributions are always welcome!

Just open up a new pull request.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
