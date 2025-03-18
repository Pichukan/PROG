'''
a=int(input())
if a%2==0:
	print('Число четное')
else:
	print('Число нечетное')
'''
'''
a=input().split('-')
#print(type(a))
if a[0]==a[1]:
	print('Строки равны')
else:
	print('Строки содержат разное количество символов')
'''
'''
a=int(input())
l=False
if a%400==0:
	l=True
elif not(a%100==0) and (a%4==0):
	l=True
if l:
	print('Високосный')
else:
	print('Обычный')
'''

'''
n = int(input())
print(('Это число не 1, 2, 3', 'Один', 'Два', 'Три')[n * (str(n) in '123')])	
'''
'''
a=int(input())
while a<=100:
	if a>10:
		print(a)
	a=int(input())
'''

'''
a=int(input())
while a<=100:
	if a<10:
		a=int(input())
		continue
	if a>100:
		break
	print(a)
	a=int(input())
'''

'''
a=input()

c=len(a)
#print(c)
b=a[::-1]
print(b)
print(a)
print('Число символов в строке:',a,'=',c)
'''

'''
a=int(input())
for i in range(a):
	print(int(i*i), end='.')
'''
'''
a=input()
k=0
for i in a:
	print(f'{k}-{i}',end=' ')
	k=k+1
'''
'''
a,b=map(int,input().split())
s=0
for i in range(a,b+1):
	#print(i)
	if int(i%2)==0:
		s=s+i
print(s)
'''

'''
# Числа Фибоначчи

arr = [1, 1]
print(arr[0])
while True:
	print(arr[-1])
	if arr[-1] == 21:break
	tmp = sum(arr)
	arr.append(tmp)
	del arr[0]
'''

#students = ['Ivan', 'Masha', 'Sasha']

'''

M[1]                        # Получить строку 2: [4, 5, 6]
M[1][2]  # Получить строку 2, а затем элемент 3 в этой строке: 6
М          # возвращает весь список [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
col2 = [row[1] for row in M] # Выбирает элементы второго столбца [2, 5, 8]
col1 = [row[0] for row in M] # Выбирает элементы первого столбца [1, 4, 7	

'''

'''
a=[1,2,3]
b = a
print(b)
a[1]=10
print(b)
b[0]=20
print(a)
print(b is a)
a=[5,6]
print(b)
print(b is a)
'''

'''
a=list(input().split())
for i in a[::-1]:
	print(i,end=' ')
'''
'''
# генератор списка, ввод целых чисел в одной строке через пробел
a=[int(i) for i in input().split()]
# условие: если длина введенной строки больше, чем один элемент (символ)
if len(a)>1:
# цикл, с реализацией перебора элементов по индексу: от первого до числа, равного длине введенной строки
for i in range(len(a)):
# вывод суммы соседних элементов в строку через пробел
print(a[i-1]+a[i+1-len(a)], end = “ “)
# иначе, если условие не выполнено, т.е. введено одно число, вывод этого числа
else:
print(a)
'''



'''
n=int(input())
b=[]
for i in range(n):
	b.append(i**2)
print(b)
c=[]
for i in range(n):
	print(b[i+1-n]+b[i-n],end=' ')
	c.append(b[i+1-n]+b[i-n])
'''

'''
b=int(input())
arr = [1, 1]
print(arr[0],end=', ')
k=0
while True:
	print(arr[-1],end=', ')
	tmp = sum(arr)
	#print(tmp)
	if (b-4)<k:
		print(tmp)
		break
	arr.append(tmp)
	k=k+1
	del arr[0]
'''

'''
a=set(input().split())
b=set(input().split())
print(a&b)
'''

'''	
a = [i for i in input().split()]
print(type(a))
b = set(a)
print(b)
print(*b)   #Здесь оператор * — не просто синтаксический сахар. Без фиксированной длины списка было бы невозможно передать элементы итерируемого объекта как отдельные аргументы, не используя *.
'''



'''
d = {}
d = dict(ключ_1='значение_1', ключ_2='значение_2’)
d = dict([(1, 1), (2, 4)])
d = dict.fromkeys(['a', 'b'], 50)
d = {a: a ** 2 for a in range(7)}
Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Kiev", "Washington"]))
создание пустого словаря с помощью литерала
c помощью функции dict()
внутри списка кортежи из ключей и значений: {1: 1, 2: 4}
с помощью метода fromkeys: {'a': 50, 'b': 50}
с помощью генератора словарей: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
c помощью функции zip(): {'Russia': 'Moscow', 'Ukraine': 'Kiev', 'USA': 'Washington'}
'''



'''
a=int(input())
dict={}
for i in range (a):
	b,b1=input(str()).split()
	dict[b]=b1
	dict[b1]=b
print(dict[input()])
'''

'''
a = list(input().lower().split())  # создание списка всех слов без учета регистра
a_set = set(a)                     # создание множества всех уникальных слов
for i in a_set:                    # цикл по значениям множества всех уникальных слов
	print(i, a.count(i))           # печать уникальных слов и их количества
'''

'''
f = open('family.txt', 'w')
f.write('Кочнов')
f.write('Захар Павлович')
f.close()
f = open('family.txt')
f.read()
'''

'''
with open('family_1.txt', 'w') as f:
	f.write('Кочнов ')
	f.write('Захар Павлович')
	f.close
f = open('family_1.txt')
f .read()
'''

'''
def modify_list(l):
	b = []
	for x in l:
		if x % 2 == 0:
			b.append(x // 2)
		l = b
	return l
lst = [int(i) for i in input().split()]
mod_lst=modify_list(lst)
print(*mod_lst)
'''

'''
# Числа Фибоначчи
def fibo(x):
	arr = [1, 1]
	
	#print(arr[0])
	for i in range(x-1):
		#print(arr[-1])
		#if arr[-1] == x:break
		tmp = sum(arr)
		arr.append(tmp)
		del arr[0]
	return arr[0]
print(fibo(10))
'''


#Комментирование кода

class Shark: #создание класса

	def swim(self): #определение функции
		print("The shark is swimming.") #печать "The shark is swimming."

	def be_predator(self): #определение функции
		print("The shark is a predator.") #печать "The shark is a predator."
a=Shark()
a.swim()
a.be_predator()