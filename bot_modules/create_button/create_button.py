import aiogram

button_1 = aiogram.types.InlineKeyboardButton(text = "Адміністратор",callback_data='admin') 
button_2 = aiogram.types.InlineKeyboardButton(text = "Клієнт", callback_data='client')

auth = aiogram.types.InlineKeyboardButton(text = "Авторизація", callback_data='auth') 
register = aiogram.types.InlineKeyboardButton(text = "Реєстрація", callback_data='register')

accept =  aiogram.types.InlineKeyboardButton(text='1', callback_data='accept') 
decline = aiogram.types.InlineKeyboardButton(text='1', callback_data='decline')