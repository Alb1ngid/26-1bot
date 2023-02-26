from aiogram import Dispatcher, Bot
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

TOKEN = config('TOKEN')

# TOKEN = '6117087222:AAHIS7VCbbcn_6m1aVK1HMwc_EN7TpxTe-M'
ADMIN = (878246291)
bot = Bot(TOKEN)
db = Dispatcher(bot=bot, storage=storage)
