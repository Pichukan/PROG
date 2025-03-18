try:
	with open('data.txt', mode='x', encoding='utf-8') as f:
		f.write('Третий фактор')
except:
	
	with open('data.txt', mode='r', encoding='utf-8') as f:
		a=f.read()
		f.close()
	with open('out.txt', mode='w', encoding='utf-8') as f:
		f.write(a)
		f.close()