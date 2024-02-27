from flask import Flask
from flask import request
from flask import jsonify
import requests
import json
import os
from dotenv import load_dotenv, find_dotenv


app=Flask(__name__)

load_dotenv(find_dotenv())

URL='https://api.telegram.org/bot' + os.getenv('TOKEN') + '/'


def write_json(data, filename='answer.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2, ensure_ascii=False)

	
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
		else:
			send_message(chat_id, text='Извините, не разобрал...')
			
		#write_json(r)
		return jsonify(r)
	return '<h1>Bot welcomes you</h1>'


 

if __name__=='__main__':
	app.run()