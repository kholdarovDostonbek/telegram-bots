from aiogram.fsm.state import State, StatesGroup

class new_application(StatesGroup):
    name = State()
    age = State()
    phone = State()
    report = State()
    verify = State()
    