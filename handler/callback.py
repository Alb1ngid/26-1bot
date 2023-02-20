from aiogram import types, Dispatcher
from config import bot, db


async def quiz2(call: types.CallbackQuery):
    ques = 'что это?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    photo = open('media/cambg_6.jpg', 'rb')
    await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='это бетмен ты угадал',
        open_period=15,

    )


def reg_hand_callback(db: Dispatcher):
    db.register_callback_query_handler(quiz2, text='button')