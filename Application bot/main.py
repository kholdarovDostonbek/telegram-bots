from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram.filters import Command
from aiogram.types import Message, BotCommand

import functions
import states

API_TOKEN = "<<< Your token is here >>>"
ADMIN_ID = "<<< Your ID is here >>> "
bot = Bot(API_TOKEN)
dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(chat_id = ADMIN_ID, text="Bot is working!")


async def start():

    dp.startup.register(startup_answer)
    dp.message.register(functions.start_command_answer, Command("start"))
    dp.message.register(functions.help_command_answer, Command("help"))
    dp.message.register(functions.application_answer, Command("application"))
    dp.message.register(functions.stop_answer, Command("stop"))
    dp.message.register(functions.new_app_name_value, states.new_application.name)
    dp.message.register(functions.new_app_age_value, states.new_application.age)
    dp.message.register(functions.new_app_phone_value, states.new_application.phone)
    dp.message.register(functions.new_app_report_value, states.new_application.report)
    dp.message.register(functions.new_app_verifing, states.new_application.verify)

    await bot.set_my_commands([
        BotCommand(command="/application", description="create a new application"),
        BotCommand(command="/stop", description="cancel"),
        BotCommand(command="/help", description="instruction for use this bot")
    ])

    await dp.start_polling(bot)
run(start())