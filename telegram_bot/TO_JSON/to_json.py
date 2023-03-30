import json     #этот кодик перехерачивает маты из txt файла в json файл

ar = []  #де факто мне этот список и нахер не нужон

with open('cenz.txt', encoding='utf-8') as r:
	for i in r:
		#n = i.lower().split('\n')[0]   #этот код строки из видео для его задач
		k = i.replace('\'','')  #избавляемся от кавычек в txt файле
		n = k.lower().replace(',','').split(' ')  #избавляемся от запятых  и преобразовываем в список по раздделителю пробел
		if n != '':
			ar.append(n)

with open('cenz.json', 'w', encoding='utf-8') as e:
	json.dump(n, e, ensure_ascii=True)   #Символы в нечитаемом экранированном виде
	#json.dump(n, e, ensure_ascii=False)  #Символы в читаемом нормальном виде
