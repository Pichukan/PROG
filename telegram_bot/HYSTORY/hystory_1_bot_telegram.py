from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

@dp.message_handler()
async def echo_send(message:types.Message):
	#await message.answer(message.text)  #отправляет обратно текст сообщения
	#await message.reply(message.text)    #отправляет обратно текст сообщения с указанаием автора
	#await bot.send_message(message.from_user.id, message.text) #отправляет в личку юзеру текст сообщения 




executor.start_polling(dp,skip_updates=True)
