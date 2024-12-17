from aiogram import Bot, Dispatcher, F
from asyncio import run
import functions, data, filters



bot = Bot(data.API_TOKEN)
dp = Dispatcher()


async def startup_answer(bot: Bot):
    await bot.send_message(chat_id=5320239407, text="Bot is working!")


async def start():

    dp.startup.register(startup_answer)


    dp.message.register(functions.sub_channel_alert, filters.CheckSubChannel())

    dp.message.register(functions.echo)



    await dp.start_polling(bot)
run(start())