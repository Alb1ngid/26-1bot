from aiogram import types,Dispatcher
from config import bot,ADMIN

async def ban(massage:types.Message):
    if massage.chat.type !='private':
        if massage.from_user.id not in ADMIN:
            await massage.answer('ты не мой господин')
        elif not massage.reply_to_message:
            await massage.answer('покажи кого банить брат')
        else:
            await bot.kick_chat_member(massage.chat.id,
                                       massage.reply_to_message.from_user.id)
            await massage.answer(f'{massage.from_user.first_name} мой господин забанил'
                                 f'{massage.reply_to_message.from_user.full_name}')
    else:
        await massage.answer('это не группа')

def reg_ban(db:Dispatcher):
    db.register_message_handler(ban,commands=['ban'],commands_prefix='!/')