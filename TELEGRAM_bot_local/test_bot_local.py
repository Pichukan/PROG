from aiogram import Bot, types, Dispatcher
from aiogram.utils import executor
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

bot=Bot(os.getenv('TOKEN'))

dp=Dispatcher(bot)

async def on_startup(_):
	print('Online!')
	#print(os.getenv('TOKEN'))

@dp.message_handler()
async def echo_send(message:types.Message):
	await message.reply('Hi!')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
