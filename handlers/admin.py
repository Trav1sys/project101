import sqlite3
from aiogram import types, Dispatcher

from handlers.database import cur

from create_bot import dp, bot
from aiogram.dispatcher import FSMContext
from handlers import database as db
from handlers import client

cur.execute("CREATE TABLE IF NOT EXISTS admins ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"
            "user_id INTEGER,"
            "username TEXT)")

admin_ids = cur.execute("SELECT user_id FROM admins").fetchall()
admin_ids = [row[0] for row in admin_ids]

conn = sqlite3.connect('Chat-bot.db')


@dp.message_handler(state='start')
async def commands_start(message: types.Message, state: FSMContext):
    # Ваш код обработки команды /start
    print('start')

    # Перенаправляем сообщение в класс client.py
    await state.set_state('menuuu')

@dp.message_handler(commands=['admin'],state="admin")
async def admin_menu(message: types.Message,  state: FSMContext):
    # Проверяем, является ли отправитель администратором
    if not is_admin(message.from_user.id):
        await message.reply("У вас нет прав доступа для выполнения этой команды.")
        return

    # Создаем клавиатуру с пунктами меню
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Просмотр базы данных"))
    keyboard.add(types.KeyboardButton("Добавить администратора"))
    keyboard.add(types.KeyboardButton("Просмотреть администраторов"))

    # Отправляем сообщение с меню пользователю
    await message.reply("Меню администратора", reply_markup=keyboard)

    # Устанавливаем состояние пользователя в меню администратора
    await state.set_state("admin_menu")


# Обработчик сообщений в состоянии "admin_menu"
@dp.message_handler(state="admin_menu")
async def process_admin_menu(message: types.Message, state: FSMContext):
    if message.text == "Просмотр базы данных":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(types.KeyboardButton("Высшее образование"))
        keyboard.add(types.KeyboardButton("Среднее профессиональное образование"))

        await message.reply("Выберите уровень образование для просмотра специальностей", reply_markup=keyboard)

        await state.set_state("select_base")
    elif message.text == "Добавить администратора":
        await message.reply("Введите ID пользователя:")
        # Устанавливаем состояние пользователя в режим добавления администратора
        await state.set_state("add_admin")

    elif message.text == "Просмотреть администраторов":
        try:
            cur.execute(f"Select user_id, username FROM Admins")
            admin_list = cur.fetchall()
            if admin_list:
                response = 'Список администраторов\n'
                for admin in admin_list:
                    user_id = admin[0]
                    username = admin[1]
                    response += f"ID: {user_id}, Username: {username}\n"
            else:
                response = 'Нет зарегистрированных администраторов'
            await message.reply(response)
        except sqlite3.Error as e:
            await message.reply("Ошибка при выполнении запроса к базе данных: " + str(e))
        # finally:
        #     # Закрытие соединения с базой данных




@dp.message_handler(state="select_base")
async def process_select_base(message: types.Message, state: FSMContext):
    if message.text == "Высшее образование":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(
            types.KeyboardButton("ИКТСС"),
            types.KeyboardButton("ИВТ"))
        await message.reply("Выберите специальность для просмотра данных", reply_markup=keyboard)
        await state.set_state("select_table")
    elif message.text == "Среднее профессиональное образование":
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        keyboard.add(
            types.KeyboardButton("ИСиП"),
            types.KeyboardButton("ИСиСС"),
            types.KeyboardButton("МТОиРЭПиУ"),
            types.KeyboardButton("ОИБАС"),
            types.KeyboardButton("ПС"),
            types.KeyboardButton("СиСА"),
            types.KeyboardButton("ЭиБУ")
        )
        await message.reply("Выберите специальность для просмотра данных", reply_markup=keyboard)
        await state.set_state("select_table")

    elif message.text == '/admin':
        await state.set_state()
    elif message.text == '/start':
        await state.set_state('menuuu')





@dp.message_handler(state="select_table")
async def process_select_table(message: types.Message, state: FSMContext):
    table_name = message.text
    if table_name:
        await export_bd(table_name, message)
    await state.set_state("select_base")


# def get_admins() -> list:
#     admin_ids = cur.execute("SELECT user_id FROM admins").fetchall()
#     admin_ids = [row[0] for row in admin_ids]
#     return admin_ids




@dp.message_handler(state="add_admin")
async def process_add_admin(message: types.Message, state: FSMContext):
    user_id = int(message.text)
    user = await bot.get_chat(user_id)
    if user_id and user_id not in admin_ids:
        username = user.username
        # Добавляем нового администратора в список
        await db.zapolnenieAdmins(user_id,username)
        await message.reply("Новый администратор добавлен.")
    else:
        await message.reply("Некорректный идентификатор пользователя.")
        return
    await state.reset_state()


@dp.message_handler(state="export_bd")
async def export_bd(table_name:str, message: types.Message):
    try:
        cur.execute(f"Select * FROM {table_name}")
        await message.answer('ФИО,Возраст,Адрес,Контакты,Баллы/оценки,Образование,Форма Обучения')
        data = cur.fetchall()
        for row in data:
            await message.answer(str(row))
    except sqlite3.Error as e:
        await message.reply("Ошибка при выполнении запроса к базе данных: " + str(e))



def is_admin(user_id: int) -> bool:
    result = cur.execute("SELECT user_id FROM admins WHERE user_id = ?", (user_id,)).fetchone()

    return result is not None

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(admin_menu, commands=['admin'])
    dp.register_message_handler(commands_start, commands=['start'])