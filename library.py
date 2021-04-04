import json
import random
import codecs


def get_a_quote() -> str:
    """Get a random quote from a json file"""
    filename = 'quotes.json'
    with open(filename):
        file_with_quotes = json.load(codecs.open(filename, 'r', 'utf-8-sig'))
        number_of_quote = random.randint(0, 6)
        quote = file_with_quotes[number_of_quote]
        return quote
