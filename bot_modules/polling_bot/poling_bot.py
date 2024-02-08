import aiogram
import bot_modules.create_bot.create_bot as m_bot
import bot_modules.create_dispatcher.create_dispatcher as m_dispatcher

async def main():
    await m_dispatcher.dispatcher.start_polling(m_bot.bot)