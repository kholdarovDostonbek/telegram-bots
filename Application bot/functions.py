from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext
import states
import main # for getting ADMIN_ID


async def echo(message: Message, bot: Bot):
    user = await bot.get_chat(message.from_user.id)
    user_photos = await message.from_user.get_profile_photos()

    text = (f"{message.from_user.mention_html('User')} info \n \n"
            f"nickname: {message.from_user.full_name} \n"
            f"ID: {message.from_user.id} \n"
            )
    
    if user.bio:
        text += (f"Bio: {user.bio}")
    if message.from_user.username:
        text += (f"Username: {message.from_user.username}")

    if user_photos:
        await message.answer_photo(user_photos.photos[0][-1].file_id, caption = text, parse_mode='HTML')
    else:
        await message.answer(text, parse_mode='HTML')


async def start_command_answer(message: Message, bot: Bot):
    await message.answer("Hello, click '/help' unless you dont know how to use this bot ")


async def help_command_answer(message: Message, bot: Bot):
    matn = """Using Bot:
/application - create a new app.
/stop - cancel a current application
    """
    await message.answer(matn)


async def application_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    await message.answer("Send you name, please!")
    await state.set_state(states.new_application.name)
    name = message.text
    

async def stop_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state == None:
        await message.answer("not found application")
    else:
        await state.clear()
        await message.answer("Application has been canceled")


async def new_app_name_value(message: Message, state: FSMContext):
    name = message.text
    if name.isalpha():
        await state.update_data(name = name)
        await message.answer(f"Your name has been accepted ✅")
        await message.answer("Please, enter your age!")
        await state.set_state(states.new_application.age)

    else:
        await message.answer(" Name can't contain numbers! \nplease, enter again")


async def new_app_age_value(message: Message, state: FSMContext):

    if message.text.isdigit() and int(message.text) > 0:

        await state.update_data(age = message.text)
        await message.answer("Your age also has been accepted")
        await message.answer("Nice! Enter your contact")
        await state.set_state(states.new_application.phone)

    else:
        await message.answer("ERROR")
    

async def new_app_phone_value(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(phone = message.text)
        await message.answer("OK, phone number is correct!")
        await message.answer("noow, you can send your offer, request or complainy")
        await state.set_state(states.new_application.report)
    else:
        await message.answer("Phone number contains only numbers")


async def new_app_report_value(message: Message, state: FSMContext):

    # await message.answer("your application is in process ... ")
    await state.update_data(report = message.text)
    data = await state.get_data()
    Application = (f"Applicant: {data.get('name')}.\n"
                   f" Age: {data.get('age')}.\n" 
                   f" Contact: {data.get('phone')}.\n"
                   f" Report: {data.get('report')}.\n"
                   )
    await message.answer(f"will you confirm application? \n \n {Application} \n \n Ha(h) \n Yoq(y)")
    await state.set_state(states.new_application.verify)


async def new_app_verifing(message: Message, bot: Bot, state: FSMContext):
    if message.text.lower() == "h":

        data = await state.get_data()
        Application = (f"Applicant: {data.get('name')}.\n"
                   f" Age: {data.get('age')}.\n" 
                   f" Contact: {data.get('phone')}.\n"
                   f" Username: @{message.from_user.username}.\n"
                   f" Report: {data.get('report')}.\n")
        
        await bot.send_message(chat_id = main.ADMIN_ID, text = f"New application: \n \n {Application}")
        await message.answer("Your whole application succesfully accepted ✅")

    elif message.text.lower() == "y":
        await state.clear()
        await message.answer("Application has been canceled 🚫")
