from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

# Создаем хранилище FSM
storage = MemoryStorage()

bot = Bot(token='6152747755:AAG2Y7o94tQ-kM9ZOUOBw7DAx89kWFcIAlo')
dp = Dispatcher(bot,storage=storage)