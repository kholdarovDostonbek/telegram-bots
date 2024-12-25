from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.types import BotCommand
from aiogram.filters import Command

import functions
import states_calendar
import callbackFunctions

dp = Dispatcher()
API_TOKEN = "7939080941:AAEY30jxiBH2F3k_VUVJJRaAS1_mMH-tl3c"
bot = Bot(API_TOKEN)
async def startup(bot: Bot):
    await bot.send_message(chat_id=5320239407, text="bot is up and running ✅")


async def start():
    dp.startup.register(startup)
    dp.message.register(functions.start_answer, Command("start"))
    dp.message.register(functions.calendar_answer, Command("calendar"))
    dp.message.register(functions.year_wanted, states_calendar.calendar_request.year)
    dp.callback_query.register(callbackFunctions.make_calendar, F.data.func(lambda x: int(x) in range(1, 13)))

    await bot.set_my_commands([
        BotCommand(command="/start", description="🤖🤖🤖"),
        BotCommand(command="/calendar", description="📆📆📆")
    ])
    await dp.start_polling(bot)
run(start()) 