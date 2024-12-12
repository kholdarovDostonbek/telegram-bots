from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text="Send a phone number", request_contact=True),
            KeyboardButton(text="Share your location", request_location=True)
        ],
    ],
    resize_keyboard=True,
)

