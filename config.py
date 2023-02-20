from aiogram import Dispatcher,Bot
from decouple import config
TOKEN = config('TOKEN')
# TOKEN = '6117087222:AAHIS7VCbbcn_6m1aVK1HMwc_EN7TpxTe-M'

bot = Bot(TOKEN)
db = Dispatcher(bot=bot)
