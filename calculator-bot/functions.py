from aiogram.types import Message
import keyboards
async def open_calc_answer(message: Message):
    await message.answer("|", reply_markup=keyboards.calc_builder.as_markup())