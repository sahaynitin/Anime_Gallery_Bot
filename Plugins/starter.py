from Helper.helper import start_text, help_text
from config import bot
from telethon import events

class start():

    @bot.on(events.NewMessage(pattern=r"^/start$|^/start@tellyanimestorebot"))
    async def event_handler_start(event):
        await bot.send_message(
            event.chat_id,
            start_text,
            file='https://telegra.ph/file/da383dd8c9add824d76f2.jpg'
        )

    @bot.on(events.NewMessage(pattern=r"^/help$|^/help@tellyanimestorebot"))
    async def event_handler_help(event):
        await bot.send_message(
            event.chat_id,
            help_text
            )

    @bot.on(events.NewMessage(pattern="/source"))
    async def event_handler_source(event):
        await bot.send_message(
            event.chat_id,
            '[Source Code](https://t.me/tellybots_digital)\nThis bot was hosted on Heroku'
        )
    
