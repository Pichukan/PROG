from flask import Flask
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv


#app=Flask(__name__)
#TODO
#1. Отсылка сообщений
#2. Прием сообщений
load_dotenv(find_dotenv())

URL='https://api.telegram.org/bot' + os.getenv('TOKEN') + '/'
#URL='https://api.telegram.org/botTOKEN/'   формат 1 части ссылки обращения к ТГ боту

print(URL)
def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)




def get_updates():
	#https://api.telegram.org/bot6959956840:AAEBBC2ejwlL8ggf1zwIoz6oa5jbngvq7ww/getUpdates
	url=URL+'getUpdates'
	r=requests.get(url)
	#write_json(r.json())
	return r.json()
	
def send_message(chat_id, text='bla-bla-bla'):
	url=URL+'sendMessage'
	answer={'chat_id':chat_id, 'text':text}
	r=requests.post(url, json=answer)
	return r.json()



def main():
	#r=requests.get(URL+'getMe')
	#write_json(r.json())
	r=get_updates()   #объект response возвращение
	chat_id=r['result'][-1]['message']['chat']['id']
	print(chat_id)
	send_message(chat_id)




 

if __name__=='__main__':
	main()