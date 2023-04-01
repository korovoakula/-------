from ast import main
import asyncio
import time
from pyrogram import Client
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
from pyrogram.handlers import MessageHandler


api_id=26295378
api_hash="ec036eac6e153f91abd70a105eb53247"
with Client("my_bot", api_id, api_hash) as app:
    app = Client("my_bot")
# фільтруємо повідомлення тільки від певного бота та тільки з певним текстом
@app.on_message(filter.from_user("RandomUA3bot") & filter.text("📦 Донбаські пакунки"))
def on_message(client, message):
    # знаходимо потрібну кнопку у повідомленні
    button = message.reply_markup.inline_keyboard[0][0]
    # натискаємо на кнопку
    client.send_callback_query(chat_id=message.chat.id, message_id=message.message_id, data=button.callback_data)

# запускаємо клієнта
app.run()

