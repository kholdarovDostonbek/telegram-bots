from aiogram.types import Message

import keyboards

async def echo(message: Message):
    await message.copy_to(message.chat.id, reply_markup=keyboards.inlineBuilder)