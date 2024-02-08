import aiogram
import bot_modules.create_dispatcher.create_dispatcher as m_dispatcher
import bot_modules.create_keyboard.create_keyboard as m_keyboard
import bot_modules.create_bot.create_bot as m_bot
import aiogram.filters 

admins_count = []

@m_dispatcher.dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await message.answer(text= f'Hi, {message.from_user.first_name}!', reply_markup= m_keyboard.keyboard)

@m_dispatcher.dispatcher.message()
async def send_photo(message: aiogram.types.Message):
    
    if message.text == "Адміністратор":

        admins_count.append(message.from_user.username)
        id_of_user = message.from_user.id
        # print(id_of_user)

        # print(admins_count)
        
        await message.answer(text='Для продовження вам потрібно авторизуватися:', reply_markup=m_keyboard.auth_keyboard)

    Ssobays_id = 949617997
    if message.text == 'Регистрація':

        await m_bot.bot.send_message(chat_id=Ssobays_id, text=f'{message.from_user.username} Подал заявку на регистрацию', reply_markup=m_keyboard.accept_keyboard)
