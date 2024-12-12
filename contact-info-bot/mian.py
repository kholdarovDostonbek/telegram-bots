from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.filters import CommandStart
import functions



API_TOKEN = "7939080941:AAEY30jxiBH2F3k_VUVJJRaAS1_mMH-tl3c"
bot = Bot(API_TOKEN)
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id = 5320239407, text = "Bot ishga tushdi ✅")



async def start():
    dp.startup.register(startup_answer)

    dp.message.register(functions.start_command_answer, CommandStart())
    dp.message.register(functions.get_contact_data, F.contact)
    dp.message.register(functions.get_location_data, F.location)
    
    await dp.start_polling(bot, polling_timeout=1)
run(start())