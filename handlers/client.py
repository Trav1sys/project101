from aiogram import types, Dispatcher

from handlers.files.app import display_menu as dm
from create_bot import dp, bot
from handlers.files.app.display_menu import current_menu
from handlers import database as db


from aiogram.dispatcher import FSMContext

from handlers.files.app.insert import MyStates


@dp.message_handler(commands=['start'],state='menuuu')
async def commands_start(message: types.Message):

    await db.db_start()
    await db.cmd_start_db(message.from_user.id)
    menu_key = 'menu_main'
    menu_message = await bot.send_message(message.chat.id, "Выберите один из пунктов меню:")
    current_menu[message.chat.id] = {
        'menu_key': menu_key,
        'message_id': menu_message.message_id
    }
    await dm.display_menu(message.chat.id, menu_key)


# Обработчик нажатия на кнопки меню
@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery, state: FSMContext):
    menu_key = callback_query.data
    chat_id = callback_query.message.chat.id
    print("menu_key:",menu_key)
    if menu_key == 'back':
        # Получаем предыдущее меню из словаря current_menu
        previous_menu = current_menu[chat_id]['previous_menu']
        if previous_menu:
            # Обновляем текущее меню
            current_menu[chat_id]['menu_key'] = previous_menu
            # Отображаем предыдущее меню
            await dm.display_menu(chat_id, previous_menu)
    # if menu_key == 'menu_main':
    #     try:
    #         message = await bot.send_chat_action(chat_id, "typing")
    #         if message:
    #             await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id']+1)
    #         else:
    #             print("Сообщение не найдено")
    #     except Exception as e:
    #         print("Ошибка при получении сообщения:", e)
    #
    #     await dm.display_menu(chat_id, menu_key)


    elif menu_key == 'menu_support':
        await bot.send_message(chat_id, "Введите ваш вопрос:")
        await state.set_state('support')




    elif menu_key == 'IKTSS_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id'] + 1)
        await state.update_data(menu_key=menu_key, institut='VO')

        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()


    elif menu_key == 'IVT_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id'] + 1)
        await state.update_data(menu_key=menu_key, institut='VO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'ISSS_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id'] + 1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await state.update_data(menu_key=menu_key)
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'MTOREPU_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id'] + 1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'OIBAS_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id'] + 1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'SSA_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id']+1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'ISP_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id']+1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'PS_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id']+1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()

    elif menu_key == 'EBU_db':
        await bot.delete_message(chat_id=chat_id, message_id=current_menu[chat_id]['message_id']+1)
        await state.update_data(menu_key=menu_key, institut='SPO')
        await bot.send_message(callback_query.from_user.id, text='Введите Фамилию Имя Отчество:')
        await MyStates.STATE1.set()


    else:
        # Обновляем текущее меню для данного пользователя
        current_menu[chat_id]['previous_menu'] = current_menu[chat_id]['menu_key']
        current_menu[chat_id]['menu_key'] = menu_key
        print("current_menu[chat_id]['previous_menu']:", current_menu[chat_id]['previous_menu'])

        # Отображаем следующее меню
        await dm.display_menu(chat_id, menu_key)


@dp.message_handler(state='support')
async def handle_support_question(message: types.Message, state: FSMContext):
    question = message.text
    user_id = message.from_user.id
    user = await bot.get_chat(user_id)
    await bot.send_message(521450050, f"Новый вопрос от пользователя @{user.username}:\n\n{question}")
    await bot.send_message(message.chat.id, "Спасибо за ваш вопрос! Мы постараемся ответить вам как можно скорее.")
    await state.finish()


# @dp.message_handler()
# async def echo_send(message: types.Message):
#     await bot.send_message(message.from_user.id, message.text)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['start'])
