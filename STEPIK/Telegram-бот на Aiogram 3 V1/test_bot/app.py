import asyncio  #Импортируем обязательно "asyncio" для написания асинхронного кода
import os       # Импортируем "os" для чтения переменного окружения
from dotenv import load_dotenv  # За ним же из "dotenv", импортируем "load_dotenv"

load_dotenv()    # Подгружаем из ".env"

from aiogram import Bot,Dispatcher        # Необходимо для запуска и дальнейшей логики бота
from aiogram.types import Message         # Для обработки типа сообщений
from aiogram.filters import CommandStart  # Импортируем, чтобы обработать команду /start
from aiogram.filters import Command       #Импортируем Command
from aiogram.enums import ParseMode       #New import
from aiogram import F                     #магический фильтр
import logging   
import re


bot=Bot(token=os.getenv('TOKEN'))  # Берем токен

dp=Dispatcher()    # Корневой роутер (обработка входящих обновлений)



""" 
#--------------------------------------------------------------------
cat = { # Словарь
    "1": {"title": "Котик №1",
          "description": "Описание котика.",
          "image_url": "https://avatars.dzeninfra.ru/get-zen_doc/8269145/pub_641ec1d0798be415157b4180_641f3d1cd4b1f54fcf2f0a01/scale_1200"},

    "2": {"title": "Котик №2",
          "description": "Описание котика.",
          "image_url": "https://avatars.dzeninfra.ru/get-zen_doc/1716911/pub_650986bb60c6c143ea7a8356_650988b680532d3c5b8aad90/scale_1200"},
}
# Логика понятна, как создаем дальше

@dp.message(CommandStart(deep_link=True, magic=F.args.regexp(re.compile(r'cat(\d+)'))))
async def start_cat(message: Message, command: Command):
    cat_number = command.args[3:]
    cat_info = cat.get(cat_number)
    
    if cat_info:
        await message.answer_photo(
            photo=cat_info["image_url"],
            caption=f"*{cat_info['title']}*\n\n{cat_info['description']}",
            parse_mode="Markdown"
        )        
    else:
        await message.answer("Нет котика с таким номером")
#---------------------------------------------------------------------
"""


TEXT='''Hello, this is a first line,
and this a second
third there

and fourth is here.
'''


@dp.message(CommandStart())   # Роутер, который обрабатывает сообщение /start
async def start(message:Message):  # Принимает объект "message" типа "Message"
    await message.answer('First message')  # Подразумевает ответ бота на /start обычным сообщением, а не ответом на сообщение
    await message.answer('First <b>message</b>', parse_mode=ParseMode.HTML)  #жирный шрифт  
    await message.answer("```Python\nПривет, друг!\n```", parse_mode=ParseMode.MARKDOWN_V2)  #разметка  
    await message.answer("Привет, ||друг\!||", parse_mode=ParseMode.MARKDOWN_V2)  #скрытый текст
    await message.answer(">Привет, друг\\!", parse_mode=ParseMode.MARKDOWN_V2)    #Цитата

    #await message.reply('Hello!')  # ответом отправляет сообщение на наше
    #await asyncio.sleep(5)  # Таймер в секундах  
    #await message.answer('How are you?')
    #await message.answer(TEXT)

"""
    image_url='https://cs14.pikabu.ru/post_img/big/2023/04/20/3/1681956381171584576.jpg'
    text=f'Hello'
    await message.answer_photo(photo=image_url, caption=text, message_effect_id='5104841245755180586', show_caption_above_media=True) #подпись сверху картинки
"""     
    

@dp.message(Command('place'))
async def send_venue(message: Message):
    await message.answer_venue(
        latitude=55.75482,
        longitude=37.62169,
        title="Красная площадь",
        address="Москва, Красная площадь",
        message_effect_id='5107584321108051014'
    )


""" 

"""    

@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID: {message.photo[-1].file_id}\n\n'  # Значение [-1] означает, что мы достаем лучшее качество картинки
                         f'Ваше имя: {message.from_user.first_name}\n'
                         f'Ваш ID: {message.from_user.id}')            



async def main():  # Обязательно асинхронная точка входа 
    await bot.delete_webhook(drop_pending_updates=True) # Тем самым, сообщения, которые были отправлены боту, когда он был выключен, при включении будут игнорироваться
    await dp.start_polling(bot)  # Процесс, при котором бот запрашивает обновления от Telegram`а и обрабатывает новые сообщения, если их нет, то бот непрерывно будет ожидать ответа от Telegram.

if __name__ == '__main__':  # Проверяет, запускается ли файл напрямую или импортируется. Если файл запускается напрямую, код внутри условия выполняется (if).
    logging.basicConfig(level=logging.INFO)  # Подключаем логгирование
    print('Bot started')
    try:
        asyncio.run(main())     # Запускаем асинхронную функцию main(), которая стартует основные процессы бота
    except KeyboardInterrupt:
        print('Bot desactivate')


