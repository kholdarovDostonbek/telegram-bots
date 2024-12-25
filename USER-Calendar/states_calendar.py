from aiogram.fsm.state import State, StatesGroup

class calendar_request(StatesGroup):
    year = State()
    month = State()

    