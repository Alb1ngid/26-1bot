from aiogram import types, Dispatcher
from config import bot, db


async def echo(massage: types.Message):
    bad_words = ['negr', 'java', 'front', 'javaScript', 'ix', 'css',
                 'html', 'php', 'дурак', 'болван']
    username = f'@{massage.from_user.username}' \
               f'' if massage.from_user.username is not None else \
        massage.from_user.first_name

    for word in bad_words:
        if word in massage.text.lower().replace(' ', ''):
            await bot.delete_message(massage.chat.id, massage.message_id)
            await massage.answer(f'не матерись {username}')
    #     закрепить смс
    if massage.text.startswith('.'):
        await bot.pin_chat_message(massage.chat.id, massage.message_id)
    if massage.text == 'anime':
        a = await bot.send_dice(massage.chat.id)
        print(massage.from_user.id)


def reg_hand_extra(db: Dispatcher):
    db.register_message_handler(echo)
