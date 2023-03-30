from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json, string

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):   #В аргумент функции передаем _ нижнее подчеркивание!
	print('Бот вышел в онлайн')
'''*************КЛИЕНТСКАЯ ЧАСТЬ****************'''
@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС. Напишите ему.') 	

@dp.message_handler(commands=['Режим_работы'])  #Кажется команда должна быть без пробела иначе не воспринимается ТГ
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 20:00, Сб-Вс с 10:00 до 17:00')		

@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Пушкина, дом Колотушкина')



'''**************АДМИНСКАЯ ЧАСТЬ****************'''

'''****************ОБЩАЯ ЧАСТЬ******************'''



@dp.message_handler()
async def echo_send(message : types.Message):
	if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
		.intersection(set(json.load(open('cenz.json')))) != set():
		await message.reply('Маты запрещены')
		await message.delete() 	
	







executor.start_polling(dp,skip_updates=True, on_startup=on_startup)
