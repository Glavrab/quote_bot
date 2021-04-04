from aiogram import (
    Bot,
    Dispatcher,
    types,
    executor)
from library import get_a_quote


WEBHOOK = 'https://d7d97f0d5183.ngrok.io'
API_TOKEN = '1666792495:AAGiLEJHfILirO4oLnLfipH2avv4aa9rTv0'
bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler()
async def send_quote(message: types.Message) -> None:
    """Handle sending a quote to user"""
    quote_to_send = get_a_quote()
    await message.answer(quote_to_send)


if __name__ == '__main__':
    bot.set_webhook(WEBHOOK)
    executor.start_polling(dp, skip_updates=True)
