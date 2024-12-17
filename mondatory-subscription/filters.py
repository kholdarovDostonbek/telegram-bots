from aiogram.filters import Filter
from aiogram.types import Message
from aiogram import Bot
from data import CHANNEL_ID


class CheckSubChannel(Filter):
    async def __call__(self, message: Message, bot: Bot):
        user_status = await bot.get_chat_member(CHANNEL_ID, message.from_user.id)
        user_status.status
        if user_status.status in ["member", "administrator", "creator"]:
            return False
        return True