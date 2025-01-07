from aiogram.types import CallbackQuery
import keyboards
async def callback_answer(callback: CallbackQuery):

    if callback.message.text == "|":
        if callback.data in "DC": await callback.answer("Fill the space before cleaning!!", show_alert=True)
        elif callback.data in "-+*/=,":
            await callback.answer(f"You cant begin with {callback.data}", show_alert=True)
        else:
            await callback.message.edit_text(callback.data + callback.message.text, reply_markup=keyboards.calc_builder.as_markup())

    else:
        if callback.data == "D":
            await callback.message.edit_text(callback.message.text[:-2] + "| ", reply_markup=keyboards.calc_builder.as_markup())

        elif callback.data == "C":
            await callback.message.edit_text("|", reply_markup=keyboards.calc_builder.as_markup())

        elif callback.data == "=" and callback.message.text[-2] in "-+/*,":
            await callback.answer("the expression is incomplete", show_alert=True)

        elif callback.data == "=" and ("+" in callback.message.text or "-" in callback.message.text or "/" in callback.message.text or "," in callback.message.text or "*" in callback.message.text):
            phrase = callback.message.text.replace(",", ".")

            try:
                phrase = str(eval(phrase[:-1]))
            except ZeroDivisionError:
                await callback.answer("ZeroDivisionError!", show_alert=True)
                
            await callback.message.edit_text(
                    phrase,
                    reply_markup=keyboards.calc_builder.as_markup()
            )

        elif callback.message.text[-2].isdigit() or callback.data.isdigit():
            await callback.message.edit_text(
                callback.message.text[:-1] + callback.data + callback.message.text[-1],
                reply_markup=keyboards.calc_builder.as_markup()
            )

        elif callback.data in "+-/*=":
            
            await callback.message.edit_text(
                callback.message.text[:-2] + callback.data + "|",
                reply_markup=keyboards.calc_builder.as_markup()
            )

        elif callback.data == ",":
            await callback.answer("Wrong command!", show_alert=True)