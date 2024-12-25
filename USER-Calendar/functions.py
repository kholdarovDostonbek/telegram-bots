from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
import states_calendar
import keyboards

async def start_answer(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text=f"Hi, "
        f"{message.from_user.mention_html(f'{message.from_user.first_name}')} \n"
        f"this is a calenar bot, if you want to see month grid in a year which you want, push on /calendar", parse_mode='HTML')


async def calendar_answer(message: Message, state: FSMContext):
    await message.reply(text="Oook, What year do you want to know?")
    await state.set_state(states_calendar.calendar_request.year)


async def year_wanted(message: Message, state: FSMContext):
    year = message.text

    if year.isdigit():
        await state.update_data(year = year)
        await message.answer(
        text="Okay, and which month?", 
        reply_markup=keyboards.inlineBuilder
        )
        await state.set_state(states_calendar.calendar_request.month)
    else:
        await message.answer("Please, check your message, \nSomething went wrong!")
