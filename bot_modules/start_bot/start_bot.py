import aiogram
import bot_modules.create_dispatcher.create_dispatcher as m_dispatcher
import bot_modules.create_keyboard.create_keyboard as m_keyboard
import aiogram.filters 
import logging
import aiogram.filters.state
import sqlite3

connect = sqlite3.connect(__file__ + "/../../sqlite/data/data.db")
cursor = connect.cursor()



admins_count = []

@m_dispatcher.dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await message.answer(text= f'Hi, {message.from_user.first_name}!', reply_markup= m_keyboard.keyboard)

@m_dispatcher.dispatcher.message()
async def send_photo(message: aiogram.types.Message):
    
    if message.text == "Адміністратор":

        admins_count.append(message.from_user.username[0])

        print(admins_count)
        cursor.execute(f"INSERT INTO admins (username) VALUES ({message.from_user.username})")
        connect.close()

        print(admins_count)
        
        await message.answer(text='Для продовження вам потрібно авторизуватися:', reply_markup=m_keyboard.auth_keyboard)


        if message.text == 'Регістрація':
            
            await message.answer(text='Ок, введіть свою пошту')

            email = message.text
            print(email)

