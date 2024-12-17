from aiogram.types import Message


async def echo(message: Message):
    await message.copy_to(message.chat.id)

async def sub_channel_alert(message: Message):
    invite_link = "https://t.me/xohlaganlarimdan"
    await message.answer(text=f"Join the channel, and try again. <a href='{invite_link}'>Link</a> ", parse_mode="HTML")