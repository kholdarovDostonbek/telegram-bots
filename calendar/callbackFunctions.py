from aiogram.types import CallbackQuery

async def ok_answer(callbackdata: CallbackQuery):
    await callbackdata.message.delete()
    await callbackdata.answer(text="Message has been deleted!", show_alert=True)
