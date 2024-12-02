from aiogram import Bot, Dispatcher, types
from asyncio import run


API_TOKEN = "7555966596:AAFsB94d6ERkoLCjnIKIojvLUUHxsH6Nnls"
bot = Bot(API_TOKEN)
dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(chat_id = 5320239407, text = "Bot ishga tushdi")

async def echo(message: types.Message, bot = Bot):
    await message.copy_to(chat_id=message.chat.id)

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(echo)
    await dp.start_polling(bot, polling_timeout=1)

run(start())
