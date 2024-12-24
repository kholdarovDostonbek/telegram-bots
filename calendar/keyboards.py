from aiogram.utils.keyboard import InlineKeyboardBuilder
from calendar import Calendar
inlineBuilder = InlineKeyboardBuilder()


kalendar  = Calendar().itermonthdays2(2007, 5)

for i in ["Du", "Se", "Chor", "Pay", "Ju", "Shan", "Yak"]:
    inlineBuilder.button(text=i, callback_data=i)


for i in kalendar:
    if i[0]: inlineBuilder.button(text=f"{i[0]: 02}", callback_data=f"{i[0]: 02}")
    else: inlineBuilder.button(text="  ", callback_data="null")
inlineBuilder.button(text="Ok", callback_data='ok')
inlineBuilder.adjust(7, repeat=True)
inlineBuilder = inlineBuilder.as_markup()







