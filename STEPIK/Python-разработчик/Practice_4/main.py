#f = open('ex.txt', 'w', encoding='utf-16');f.write('my text')
#f.close()

with open('ex.txt', mode='r', encoding='utf-16') as f:
	answer=f.read()
	f.close()
with open('ex.txt', mode='a', encoding='utf-16') as f:
	f.write('\nhacked')
	f.close()
#print(answer)