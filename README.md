# Summary
This is a coding challenge for an interview.

# Scope
1. Create an API with a single endpoint which accepts a country’s code in the World Bank’s 3 letter ISO 3166-1 alpha-3 code format, and returns the name and capital of the country.
2. Add an endpoint that accepts four values: a minimum and maximum latitude, and a minimum and maximum longitude. The endpoint should return a list of capital cities located within those coordinates.
3. Build a third endpoint that accepts a list of 4 capital cities and returns the most efficient route between them. The list should include a starting city, an ending city, and 2 cities to visit along the way. Don’t worry about the actual logistics of planes and boats—instead find the shortest total miles traveled as the crow flies.

# Tools and technologies
- Bitcoin addresses and wallet balances provided by [Blockchair](https://blockchair.com).
- [Bootstrap](https://getbootstrap.com) for front-end styling
- Python and [Flask](https://flask.palletsprojects.com/en/2.0.x/) for back-end

# Getting started
1. Clone this repo
2. Run `cd cointracker`
3. Create a virtual environment by running `python3 -m venv coin-env`
4. Activate the virtual environment by running `. coin-env/bin/activate`
5. Install dependecies by running `pip install -r requirements.txt`
6. Start the server by running `flask run`
7. View the application at http://127.0.0.1:5000/
