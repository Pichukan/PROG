from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
#b4 = KeyboardButton('Поделиться номером', request_contact=True)
#b5 = KeyboardButton('Отправить где я', request_location=True)


#kb_client = ReplyKeyboardMarkup()     #Просто клавиатура
#kb_client = ReplyKeyboardMarkup(resize_keyboard=True)   #Уменьшенная по размеру клавиатура
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) #Скрывемая клавиатура но открыть можно потом

#kb_client.add(b1).add(b2).add(b3)   #В столбик обычно
#kb_client.add(b1).add(b2).insert(b3) #Вставляет справа в ряду
#kb_client.row(b1,b2,b3)  #Все располагается в строку
kb_client.add(b1).add(b2).add(b3)#.row(b4,b5)  #Компонуем по разному