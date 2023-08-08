import sqlite3
from aiogram.types import InlineKeyboardMarkup, KeyboardButton, WebAppInfo
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import json
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram import types

bot = Bot(token='1672438859:AAEVf_aKog8XvhYrERzcXdQ7WljolArQ7sc')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def send_message(message: types.Message):
    reply_markup = InlineKeyboardMarkup().add(InlineKeyboardButton(text="test",
                                                                   web_app=WebAppInfo(url="https://marsel3.github.io/webapp/")))

    await message.answer(text='Давай познакомимся', reply_markup=reply_markup)


@dp.message_handler(commands=['admin'])
async def send_message(message: types.Message):
    reply_markup = ReplyKeyboardMarkup().add(KeyboardButton(text="Указать ФИ без О",
                                                            web_app=WebAppInfo(url="https://marsel3.github.io/webapp/")))
    await message.answer(text='Давай познакомимся', reply_markup=reply_markup)


@dp.message_handler(content_types="web_app_data") #получаем отправленные данные
async def answer(message: types.Message):
    data = json.loads(message.web_app_data.data)
    await message.answer(f"Иди нахуй {data['name']} {data['surname']}!!!")



if __name__ == "__main__":
    executor.start_polling(dp)
