from aiogram.types import Message

from keyboards import buttons

async def start_command_answer(message: Message):
    await message.reply(text="Please chooso one", reply_markup=buttons)

async def get_contact_data(message: Message):
    contact_data = f"""
================= 
full name: {message.contact.first_name} {message.contact.last_name}
=================
user_id: {message.contact.user_id}
=================
phone number: {message.contact.phone_number}
================= 

"""
    await message.answer(f"Your contact has been received \n\n {contact_data}") 


async def get_location_data(message: Message):
    location_info = f"""
kenglik: {message.location.latitude}
uzunlik: {message.location.longitude}

"""
    await message.answer_contact(location_info)