from aiogram.dispatcher.filters import state
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import dp, bot
from handlers import database as db




class MyStates(state.StatesGroup):
    STATE1 = state.State()
    STATE2 = state.State()
    STATE3 = state.State()
    STATE4 = state.State()
    STATE5 = state.State()
    STATE6 = state.State()
    STATE7 = state.State()


@dp.message_handler(state=MyStates.STATE1)  # Обработка сообщения в состоянии STATE1
async def process_state1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['FIO'] = message.text
    await bot.send_message(message.from_user.id, 'Введите ваш возраст:')
    await MyStates.STATE2.set()  # Переход к состоянию STATE2

@dp.message_handler(state=MyStates.STATE2)  # Обработка сообщения в состоянии STATE2
async def process_state2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
    await bot.send_message(message.from_user.id, 'Укажите свой адрес проживания:')
    await MyStates.STATE3.set()  # Переход к состоянию STATE3

@dp.message_handler(state=MyStates.STATE3)  # Обработка сообщения в состоянии STATE3
async def process_state3(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['adress'] = message.text
    await bot.send_message(message.from_user.id, 'Укажите контактные данные (номер телефона или почту):')
    await MyStates.STATE4.set()  # Переход к состоянию STATE4

@dp.message_handler(state=MyStates.STATE4)  # Обработка сообщения в состоянии STATE4
async def process_state4(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact'] = message.text
        data = await state.get_data()
        institut = data.get('institut')
    if (institut == 'SPO'):
        await bot.send_message(message.from_user.id, 'Укажите средний балл аттестата:')
        await MyStates.STATE5.set()  # Переход к состоянию STATE5
    elif (institut == 'VO'):
        await bot.send_message(message.from_user.id, 'Укажите сумму баллов за 3 предмета:')
        await MyStates.STATE5.set()  # Переход к состоянию STATE5

@dp.message_handler(state=MyStates.STATE5)  # Обработка сообщения в состоянии STATE5
async def process_state5(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['score'] = message.text
        data = await state.get_data()
        institut = data.get('institut')
    if (institut == 'SPO'):
        await bot.send_message(message.from_user.id, 'Укажите базовое образование (9класс, 11класс):')
        await MyStates.STATE6.set()  # Переход к состоянию STATE5
    elif (institut == 'VO'):
        await bot.send_message(message.from_user.id, 'Укажите базовое образование (СПО, 11класс):')
        await MyStates.STATE6.set()  # Переход к состоянию STATE6


@dp.message_handler(state=MyStates.STATE6)  # Обработка сообщения в состоянии STATE6
async def process_state6(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['obrazovanie'] = message.text
    await bot.send_message(message.from_user.id, 'Укажите форму обучения (очная, заочная):')
    await MyStates.STATE7.set()  # Переход к состоянию STATE7

@dp.message_handler(state=MyStates.STATE7)  # Обработка сообщения в состоянии STATE7
async def process_state7(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data = await state.get_data()
        menu_key = data.get('menu_key')
        institut = data.get('institut')
        data['forma_obuch'] = message.text
        await state.finish()
        if (menu_key == 'IKTSS_db'):
            await db.zapolnenieIKTSS(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],data['obrazovanie'],data['forma_obuch'])
        elif (menu_key == 'IVT_db'):
            await db.zapolnenieIVT(data['FIO'], data['age'], data['adress'], data['contact'], data['score'],
                                     data['obrazovanie'], data['forma_obuch'])
        if (menu_key == 'ISSS_db'):
            await db.zapolnenieISSS(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'MTOREPU_db'):
            await db.zapolnenieMTOREBU(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'OIBAS_db'):
            await db.zapolnenieOIBAS(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'SSA_db'):
            await db.zapolnenieSSA(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'ISP_db'):
            await db.zapolnenieISP(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'PS_db'):
            await db.zapolneniePS(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])
        elif (menu_key == 'EBU_db'):
            await db.zapolnenieEBU(data['FIO'], data['age'], data['adress'], data['score'], data['contact'],
                                     data['obrazovanie'], data['forma_obuch'])

    if (institut == 'VO'):
        await bot.send_message(message.from_user.id,text= f"Ваши данные были записаны: \nФИО:{data['FIO']}\nВозраст: {data['age']}\nАдрес проживания: {data['adress']}\nСумма балов за 3 экзамена: {data['score']}\nКонтактные данные: {data['contact']}\nБазовое образование:: {data['obrazovanie']}\nФорма обучение: {data['forma_obuch']}\nЧтобы вернуться, пропишите команду /start")
    if (institut == 'SPO'):
        await bot.send_message(message.from_user.id,text= f"Ваши данные были записаны: \nФИО:{data['FIO']}\nВозраст: {data['age']}\nАдрес проживания: {data['adress']}\nСредний балл за аттестат: {data['score']}\nКонтактные данные: {data['contact']}\nБазовое образование:: {data['obrazovanie']}\nФорма обучение: {data['forma_obuch']}\nЧтобы вернуться, пропишите команду /start")
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(process_state1, state=MyStates.STATE1)
    dp.register_message_handler(process_state2, state=MyStates.STATE2)
    dp.register_message_handler(process_state3, state=MyStates.STATE3)
    dp.register_message_handler(process_state4, state=MyStates.STATE4)