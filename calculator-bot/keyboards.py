from aiogram.utils.keyboard import InlineKeyboardBuilder




calc_builder = InlineKeyboardBuilder()
for i in "789+456-123*,0/=DC":
    calc_builder.button(text=i, callback_data=i)

calc_builder.adjust(4, repeat=True)
calc_builder.as_markup()