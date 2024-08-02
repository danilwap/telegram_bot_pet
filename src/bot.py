from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from utils.db.storage import DatabaseManager

from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.)