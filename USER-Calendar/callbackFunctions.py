from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
import keyboards

async def make_calendar(callbackdata: CallbackQuery, state: FSMContext):
    month_names = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
}
    await state.update_data(month = callbackdata.data)
    data = await state.get_data()
    year = int(data.get('year'))
    month = int(data.get('month'))
    await callbackdata.message.answer(text=f" Here is the calendar for the month you selected. \n Year: {year} \n Month: {month_names[month]}", reply_markup = await keyboards.inlineBuilder_month(state))
