from aiogram.utils.keyboard import InlineKeyboardBuilder
from calendar import Calendar
from aiogram.fsm.context import FSMContext


inlineBuilder = InlineKeyboardBuilder()
inlineBuilder.button(text="January", callback_data='1')
inlineBuilder.button(text="February", callback_data='2')
inlineBuilder.button(text="March", callback_data='3')
inlineBuilder.button(text="April", callback_data='4')
inlineBuilder.button(text="May", callback_data='5')
inlineBuilder.button(text="June", callback_data='6')
inlineBuilder.button(text="July", callback_data='7')
inlineBuilder.button(text="August", callback_data='8')
inlineBuilder.button(text="September", callback_data='9')
inlineBuilder.button(text="October", callback_data='10')
inlineBuilder.button(text="November", callback_data='11')
inlineBuilder.button(text="December", callback_data='12')

inlineBuilder.adjust(2, repeat=True)
inlineBuilder = inlineBuilder.as_markup()

async def inlineBuilder_month(state: FSMContext):
    data = await state.get_data()
    year = int(data.get('year'))
    month = int(data.get('month'))
    inlineBuilder_month = InlineKeyboardBuilder()
    kalendar  = Calendar().itermonthdays2(year, month)

    for i in ["Mo", "Tu", "Wen", "thur", "fri", "sat", "sun"]:
        inlineBuilder_month.button(text=i, callback_data=i)
    for i in kalendar:
        if i[0]: inlineBuilder_month.button(text=f"{i[0]: 02}", callback_data=f"{i[0]: 02}d")
        else: inlineBuilder_month.button(text="  ", callback_data="null")
    inlineBuilder_month.adjust(7, repeat=True)
    return inlineBuilder_month.as_markup()
