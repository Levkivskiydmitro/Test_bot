import aiogram
import bot_modules.create_button.create_button as m_button

keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [m_button.button_1, m_button.button_2]
    ],
    resize_keyboard=False,
      one_time_keyboard=True

)

auth_keyboard = aiogram.types.ReplyKeyboardMarkup(
    keyboard = [
        [m_button.auth, m_button.register]
    ],
    resize_keyboard=False,
    one_time_keyboard=True

)