from flask import request


def parsing_data():
    """Парсинг сообщения"""
    message_info = request.get_json()
    message = message_info['message']
    chat_info = message['chat']
    chat_id = chat_info['chat_id']
    text = message['text']
    data = {'text': text, 'chat_id': chat_id}
    return data
