import logging

from decouple import config
from telethon import TelegramClient


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Start de bot
print('Iniciando...')

api_id = config("APP_ID", cast=int)
api_hash = config("API_HASH")
token = config("TOKEN")
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=token)

async def main():
    me = await bot.get_me()
    print(me)

    async for dialog in bot.iter_dialogs():
        print(dialog.name, 'has ID', dialog.id)

    await bot.send_message(me.id, 'Hola')

    # You can print the message history of any chat:
   # async for message in bot.iter_messages('me'):
    #    print(message.id, message.text)


with bot:
    bot.loop.run_until_complete(main())
