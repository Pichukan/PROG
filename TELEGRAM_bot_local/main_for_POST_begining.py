from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv


app=Flask(__name__)
#TODO
#1. Отсылка сообщений
#2. Прием сообщений
load_dotenv(find_dotenv())

URL='https://api.telegram.org/bot' + os.getenv('TOKEN') + '/'
#URL='https://api.telegram.org/botTOKEN/'   формат 1 части ссылки обращения к ТГ боту
#print(URL)

def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)




def get_updates():
	#https://api.telegram.org/botTOKEN/getUpdates
	url=URL+'getUpdates'
	r=requests.get(url)
	#write_json(r.json())
	return r.json()
	
def send_message(chat_id, text='bla-bla-bla'):
	url=URL+'sendMessage'
	answer={'chat_id':chat_id, 'text':text}
	r=requests.post(url, json=answer)
	return r.json()


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method=='POST':
		r=request.get_json()
		chat_id=r['message']['chat']['id']
		message=r['message']['text']

		if 'bitcoin' in message:
			send_message(chat_id, text='Слишком дорогой')
		#write_json(r)
		return jsonify(r)
	return '<h1>Bot welcomes you</h1>'











def main():
	#r=requests.get(URL+'getMe')
	#write_json(r.json())
	#r=get_updates()   #объект response возвращение
	#chat_id=r['result'][-1]['message']['chat']['id']   #если активностей не было то словарь неполный будет ошибка
	#print(chat_id)
	#send_message(chat_id)
	pass




 

if __name__=='__main__':
	#main()
	app.run()