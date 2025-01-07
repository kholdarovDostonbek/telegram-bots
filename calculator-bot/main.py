from aiogram import Bot, Dispatcher
from asyncio import run
import functions
import callback_functions
dp = Dispatcher()
API_TOKEN = "7939080941:AAEY30jxiBH2F3k_VUVJJRaAS1_mMH-tl3c"
bot = Bot(API_TOKEN)

async def startup(bot: Bot):
    await bot.send_message(chat_id=5320239407, text="bot is up and running ✅")

async def start():
    dp.startup.register(startup)
    dp.message.register(functions.open_calc_answer)
    dp.callback_query.register(callback_functions.callback_answer)

    await dp.start_polling(bot)
run(start())