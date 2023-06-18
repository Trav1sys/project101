from aiogram import types
from create_bot import bot
from handlers.files.app.menus import menus

# Словарь для отслеживания текущего меню для каждого пользователя
current_menu = {}

# Функция для отображения меню
async def display_menu(chat_id, menu_key):
    menu_data = menus[menu_key]
    menu = types.InlineKeyboardMarkup()
    for button in menu_data['buttons']:
        menu.add(types.InlineKeyboardButton(button['text'], callback_data=button['callback']))
    if 'photo' in menu_data:
        await bot.send_photo(chat_id=chat_id, photo=open(menu_data['photo'], 'rb'), caption=menu_data['message'])
        await bot.edit_message_text(menu_data['title'], chat_id=chat_id, message_id=current_menu[chat_id]['message_id'],
                                    reply_markup=menu)
    else:
        await bot.edit_message_text(menu_data['title'], chat_id=chat_id, message_id=current_menu[chat_id]['message_id'],
                                    reply_markup=menu)

