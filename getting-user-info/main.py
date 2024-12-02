from aiogram import Bot, Dispatcher
# from function import get_data
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command

import function


API_TOKEN = "7555966596:AAFsB94d6ERkoLCjnIKIojvLUUHxsH6Nnls"
bot = Bot(API_TOKEN)
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id = 5320239407, text = "Bot ishga tushdi ✅")

async def start():
    dp.startup.register(startup_answer)

    dp.message.register(function.start_answer, Command("start"))
    dp.message.register(function.help_answer, Command("help"))

    dp.message.register(function.get_data)
    await bot.set_my_commands([
        BotCommand(command="/start", description="🤖🤖🤖"),
        BotCommand(command="/help", description="🆘")
    ])
    await dp.start_polling(bot, polling_timeout=1)

run(start())
