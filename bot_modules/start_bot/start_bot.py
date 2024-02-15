import aiogram
import bot_modules.create_dispatcher.create_dispatcher as m_dispatcher
import bot_modules.create_keyboard.create_keyboard as m_keyboard
import bot_modules.create_bot.create_bot as m_bot
import aiogram.filters 



admins_count = []

@m_dispatcher.dispatcher.message(aiogram.filters.CommandStart())
async def bot_start(message: aiogram.types.Message):
    await message.answer(text= f'Hi, {message.from_user.first_name}!', reply_markup= m_keyboard.keyboard)
# aiogram.types.
@m_dispatcher.dispatcher.callback_query()
async def send_photo(callback: aiogram.types.CallbackQuery):
    
    if callback.data == "admin":

        
        await callback.message.answer(text='Для продовження вам потрібно авторизуватися', reply_markup=m_keyboard.auth_keyboard)
    
    if callback.data == 'register':
        
        await callback.message.answer(text='Для подальшої реєстрації вам потрібно вказати такі дані як:\n Email, Nickname, Password, Phone Number')
        await aiogram._asyncio.sleep(20)
@m_dispatcher.dispatcher.message()
async def ajhsfdgjhk(message: aiogram.types.Message):

    answer = message.text






        


