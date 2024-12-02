from aiogram import Bot
from aiogram.types import Message

async def get_data(message: Message, bot: Bot):

    user  = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    text = (f"{message.from_user.mention_html('User')} info \n\n"
                f"nickname: {message.from_user.full_name} \n"
                f"ID: {message.from_user.id} \n")
    
    if user.bio: text += f"Bio: {user.bio}\n"

    if message.from_user.username: text += f"username: @{message.from_user.username} \n"

    if user_photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption = text, parse_mode='HTML')
    else:
        await message.answer(text, parse_mode='HTML')


async def start_answer(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, text=f"Hi, "
        f"{message.from_user.mention_html(f'{message.from_user.first_name}')}", parse_mode='HTML')


async  def help_answer(message: Message, bot: Bot):

    text = """
        <b>Bot commands: \n </b>
/start - refresh the bot
/help - see all commands
"""

    await bot.send_message(message.from_user.id, text, parse_mode="HTML")
    

    
 