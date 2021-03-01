from flask import request
import requests


url = 'https://api.telegram.org/1666792495:AAGiLEJHfILirO4oLnLfipH2avv4aa9rTv0'


def parsing_data() -> dict:
    """Парсинг сообщения"""
    message_info = request.get_json()
    message = message_info['message']
    chat_info = message['chat']
    chat_id = chat_info['chat_id']
    text = message['text']
    data = {'chat_id': chat_id, 'text': text}
    return data


def send_message(chat_id: int, text: str) -> None:
    """Отправка сообщения"""
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url=url+'sendMessage', data=data)
