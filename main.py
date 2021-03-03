from flask import Flask
from library import (parsing_data,
                     send_message,
                     get_a_quote)


app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    if parsing_data():
        data = parsing_data()
        chat_id = data['chat_id']
        text = get_a_quote()
        send_message(chat_id=chat_id, text=text)
    return 'not done'


if __name__ == '__main__':
    app.run(port=443, ssl_context='adhoc')
