from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
#from aiogram.types import ReplyKeyboardRemove


#@dp.message_handler(commands=['start','help'])
async def command_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС. Напишите ему.') 	

#@dp.message_handler(commands=['Режим_работы'])  #Кажется команда должна быть без пробела иначе не воспринимается ТГ
async def pizza_open_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'Пн-Пт с 9:00 до 20:00, Сб-Вс с 10:00 до 17:00')		

#@dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message : types.Message):
	await bot.send_message(message.from_user.id, 'ул. Пушкина, дом Колотушкина')#, reply_markup=ReplyKeyboardRemove()) #если надо  удалить клавиатуру по кнопке но надо убрать запись в client_kb об олноразовости

def register_handlers_client(dp:Dispatcher):
	dp.register_message_handler(command_start, commands=['start','help'])
	dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
	dp.register_message_handler(pizza_place_command, commands=['Расположение'])