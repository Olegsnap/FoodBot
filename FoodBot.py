import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv


load_dotenv()
token = os.getenv('TOKEN')
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s, %(levelname)s, %(message)s',
    )
# Объект бота
bot = Bot(token)
# Диспетчер
dp = Dispatcher()


# Хэндлер на команду /start
@dp.message(commands=['start'])
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text='Узнать условия доставки'),
            types.KeyboardButton(text='Посмотреть меню')
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    await message.answer('Чего желаете?', reply_markup=keyboard)


@dp.message(commands=['done'])
async def cmd_done(message: types.Message):
    await message.answer('Пока')


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
