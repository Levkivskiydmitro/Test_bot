import aiogram
import bot_modules.create_button.create_button as m_button

keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard= [[m_button.button_1, m_button.button_2]]

)

auth_keyboard = aiogram.types.InlineKeyboardMarkup(
    inline_keyboard = [[m_button.register, m_button.auth]]

)

# accept_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[m_button.accept, m_button.decline]])