from flask import request
import requests
import json
import random


URL = 'https://api.telegram.org/1666792495:AAGiLEJHfILirO4oLnLfipH2avv4aa9rTv0'


def parsing_data() -> dict:
    """Function to parse a data from user to get a chat id and define text
    """
    message_info = request.get_json()
    message = message_info['message']
    chat_info = message['chat']
    chat_id = chat_info['chat_id']
    if 'text' in message:
        text = message['text']
        data = {'chat_id': chat_id, 'text': text}
        return data
    text = 'Я этого не понимаю'
    send_message(chat_id=chat_id, text=text)


def send_message(chat_id: int, text: str) -> None:
    """Function to send a message to the user
    """
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url=URL+'sendMessage', data=data)


def get_a_quote() -> str:
    """Function to get a random quote from a json file
    """
    filename = 'quotes.json'
    with open(filename) as file:
        file_with_quotes = json.load(file)
        number_of_quote = random.randint(1, 7)
        quote = file_with_quotes[number_of_quote]
        return quote
