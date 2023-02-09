from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor  # для запуска бота
import logging
import decouple
from decouple import config

# decouple длятого чтобы скрывать определенную инфу
# logging для выведения расширенной информации

# Bot это токен бота
# Dispatcher это перехватчик смс
# types свои типы данных в aiogram


TOKEN = config('TOKEN')
# TOKEN = '6117087222:AAHIS7VCbbcn_6m1aVK1HMwc_EN7TpxTe-M'

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)





@db.message_handler(commands=['start', 'hello'])
async def start_handler(massage: types.Message):
    await bot.send_message(massage.from_user.id, f'привет {massage.from_user.first_name}')
    await massage.answer('это ансфер')
    await massage.reply(massage.from_user.first_name)

@db.message_handler()
async def echo(massage: types.Message):
    await bot.send_message(massage.from_user.id, massage.text)
    await massage.answer('что-то еще?')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)
