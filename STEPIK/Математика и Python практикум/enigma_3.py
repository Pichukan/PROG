
#h, m = map(int, input().split(':'))

'''
h = input()
m = input()
print('Hello,',h)
print('Hello,',m)
'''

#print(f"Hello, {input()}",f"Hello, {input()}",sep="\n")

'''
a=int(input())
b=int(input())
print(a+b)
'''

'''
from math import e, sin, exp, log, pow 
b=(pow(2,(pow(3,2)))-log((exp(2)),e)-10)/100
print(b)
'''

'''
import math
a=map(int,input().split(', '))
b=list(a)
otkl=[]
#print(b[0])
s=0
for i in b:
	s=s+i
mo=s/len(b)
print(mo)
#d=0
for i in b:
	otkl.append(pow((i-mo),2))
	#d=d+pow((mo-i),2)
	
print(otkl)
print(len(otkl),'length')
print(sum(otkl),'summa otklon')


disp=sum(otkl)/(len(otkl)-1)
print(disp)
sco=math.sqrt(disp)
print(sco)
'''
'''
a,b=int(input()),int(input())
#print(a,b)
print(a+b)
print(a-b)
print(b-a)
print(a*b)
print(a/b)
print(b-(b//a)*a)
print(a**b)
'''

'''
a,b=int(input()),int(input())
print(a//b)
'''

'''
import math
a,b,c=int(input()),int(input()),int(input())
p=a+b+c
pp=p/2
print(p)
print(math.sqrt(pp*(pp-a)*(pp-b)*(pp-c)))
'''

'''
a,b=float(input()),float(input())
s=(a*b)/2
print(int(s))
print(round(s,1))
print(s)
'''
'''
import math
a=int(input())
k=math.sqrt(3)/4
s=((a*3)**2)*k+2*((a**2)*k)
print(round(s))
'''
'''
import math
a=int(input())
s1=3*math.sqrt(3)/2*(a**2)
s2=3*(a**2)
k=math.sqrt(3)/4
s3=(((a/2)**2)*k)*6
print(round(s1+s2+s3))
'''

'''
import math
a=int(input())
s=round(3*a**2*math.sqrt(5*(5+2*math.sqrt(5))),2)
v=round(a**3/4*(15+7*math.sqrt(5)),2)
print(s,v,sep='\n')
'''


'''
l,v1,v2,vm=int(input()),int(input()),int(input()),int(input())
t=l/(v1+v2)
lm=t*vm
print(lm)
'''
'''
a=list(map(int,input().split()))
#print(type(a[0]))
print(*a)
a = [str(i) for i in a]
print('---'.join(a))
'''

'''
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sa=0
for i in a:
	sa=sa+int(i)
sb=0
for i in b:
	sb=sb+int(i)
print(f"{sa}#{sb}")
'''	   

'''
# put your python code here
a = input().split()
b = input().split()
a = sum([int(i) for i in a])
b = sum([int(i) for i in b])
c = [str(a), str(b)]
print("#".join(c))
'''
'''
a=input().split('&')
#print(type(a))
b=set(a)
print(*b)
'''

'''
a=input().split()
#print(type(a))
c=a[::-1]
b=a[1:3]+c[1:2]
print(*b)
'''

'''
a=['www','rr','qqq']
b='-'.join(a)
print(b)
'''

'''
a=input().split()
b='-$-'.join(a[::-1])
#print(type(b))
print(b)
'''

'''
a=input().split()
print(len(a),a.count('one'))
'''
'''
a=map(int,input().split())
print(sum(a))
'''



#print('\a')


'''
a=input()
print(a)
'''
'''
a,b=input(),input()
print(a,b,sep='$')
'''
'''
a='wnsndjudjdjfnfcn'
b=a[1:-2]
print(b)
'''
'''
a="['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']"
L=list(map(str,a.split(', ')))
#print(b)
#Готовим списки для будущих срезов
c=[]
d=[]
for i in L:      #Цикл по удалению квадратных скобок
	pos=i.find('[')
	if pos != -1:
		c.append(i[1::])
		continue
	pos=i.find(']')
	if pos != -1:
		c.append(i[:-1:])
		continue
	c.append(i)	
#print(c)

for i in c:    #Цикл по удалению кавычек
	#print(i,i[1:-1])
	d.append(i[1:-1])
L=d		
#print(*L)       #Итоговый список очищенный
'''


#L = input()[1:][:-1].replace("'", "").split(', ')
'''
a = input()
a = a[1:-1]
a = a.replace("'","")
L = a.split(', ')
'''
'''
# your code
str = input()
str=str[1:-1]
str=str.replace("'", '')
str=str.replace(",",'')
str=str.split(' ')
L=str
'''

'''
v = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
a=int(input())
print(v[a])
'''

'''
a=int(input())
if a!=0:
	b=int(input())
	print(round(b/a,1))
else:
	print('Division by zero!')
'''
'''
a=input()
d=True
if a=='int':
	d=False
	b=int(input())
	c=int(input())
	if (b==c) and (b==0):
		print('Empty Ints')
	else:
		print(b+c)
if a=='str':
	d=False
	b=input()
	if b=='':
		print('Empty String')
	else:
		print(b)
if a=='list':
	d=False
	b=input().split()
	if len(b)==0:
		print('Empty List')
	else:
		print(b[-1])
if d==True:
	print('Unknown type')
'''

'''
a=int(input())
i=0
while i<(a+1):
	print(i)
	i=i+1
'''

'''
a=int(input())

for i in range(0,a,2):
	print(i**2)
'''
	

'''
s=0
for i in range(1,11):
	#print(i**2)
	s=s+i
print(s/10)
'''
'''
s=0
while True:
	a=input()
	if a=='The End':
		break
	else:
		s=s+int(a)
print(s)
'''

'''
a=list(map(str,input().split()))
#print(a[0][0])
for i in a:
	#print(i[0][0])
	if i[0][0]=='*':
		continue
	print(i)
'''

'''
a=int(input())

for i in range (2,int(a/2)+1):
	if a//i==a/i:
		print(i)
		break
'''
'''
a=int(input())
for i in range(1,abs(a)):
	print(i**3)
'''


#print([n for n in range(1, 100) if n % 2 == 0])


'''	
def newfunc(n):
    print('n',n)
    def myfunc(x):
        print('x',x)
        print('n',n)
        return x + n
    #print(myfunc)
    
    return myfunc
new = newfunc(100)# new - это функция
new(300)
new(200)
'''

'''
def sum2(a,b):
	return(a+b)
'''

'''
def Hello(a='%UserName%'):
	
	print('Hello, '+a+'!')
#a=input()
#Hello()
'''

'''
def dfactorial(n):	
	if n%2 == 0:
		if n==0:
			return 1
		else:
			return n*dfactorial(n-2)
	if n%2 != 0:
		if (n == 0) or (n < 0):
			return 1
		else:
			return n*dfactorial(n-2)
b=int(input())
print(dfactorial(b))
'''
'''			
def dfactorial(n):
	
	if (n == 0) or (n < 0):
		 return 1
	else:
		return n*dfactorial(n-2)
b=int(input())
print(dfactorial(b))
'''

'''
def Kfactorial(n,k=1):
	if (n == 0) or (n < 0):
		return 1
	else:
		#print('n',n,'k',k)
		return n*Kfactorial(n-k,k)
#b=int(input())
#print(Kfactorial(10,1))
'''
'''
def convert(L):
	K=[]
	for i in L:
		#print(i)
		i=int(i)
		K.append(i)
	return K
		
L=[1, 2, '3', '4', '5', 6]
print(convert(L))
'''
'''
def translate(d, n=2, i=[]):	
	k=d%n
	if k == d:		
		i.append(k)		
		i.reverse()		
		h=''.join([str(elem) for elem in i])
		#print(h)
		return h
	else:
		k=d%n
		i.append(k)		
		return translate(d//n,n,i)
s=translate(19,7)
print(s)
'''


'''
def factorial(n):
	
	if (n == 0) or (n < 0):
		 return 1
	else:
		return n*factorial(n-1)
#b=int(input())
#print(factorial(b))

def sf(n):
	if (n == 0) or (n < 0):
		return 1
	else:
		return factorial(n)*sf(n-1)

#c=int(input())
#print(sf(c))
'''


		
'''		
	
def convert(L):
	K=[]
	for i in L:
		#print(i)
		i=int(i)
		K.append(i)
	return K




L=list(map(str,input().split()))
#L=input()		
#L=[1, 2, '3', '4', '5', 6]
#print(convert(L))
print(L)
'''

#a="['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']"
#a=['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
#L=map(str,input.split(', '))
#L=list(map(str,input().split()))
#print(L)

'''
	#[1, 2, '42', '3', '4', '5', 6, 13]
	#['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
def clear_convert_list(L):	
	c=[]
	d=[]
	for i in L:      #Цикл по удалению квадратных скобок с двух крайних сторон
		pos=i.find('[')
		if pos != -1:
			c.append(i[1::])
			continue
		pos=i.find(']')
		if pos != -1:
			c.append(i[:-1:])
			continue
		c.append(i)			
	for i in c:    #Цикл по удалению кавычек	
		try:                    #если в int переводится значит тут число
			n=int(i)            #и кавычки не убираем
			d.append(i)
		except:                  #если в int не переводится значит тут str
			d.append(i[1:-1])    #и кавычки убираем
	L=d		
	return(L)

def maxId(L):
	K=[]
	for i in L:
		K.append(str(i))
	L=K		
	D=clear_convert_list(L)	
	maxx=D[0]	
	for i in D:
		if int(i)>int(maxx):
			maxx=i
	ind=D.index(maxx)
	print(ind)
	return ind
	
L = [1, 2, '42', '3', '4', '5', 6, 13]
maxld(L)
'''

'''
#your code
def convert(L):
	return [int(i) for i in L]
def maxId(L):
	return convert(L).index(max(convert(L)))
'''
'''
#your code
def maxId(L):
	return L.index(max(L, key=int))
'''
'''
#your code
def maxId(L):
	L = list(map(int, L))
	return L.index(max(L))
'''
'''
#your code
def maxId(a):
	return max(zip(map(int, a), range(len(a))))[1]
'''

'''
with open('biba.txt') as a:
	text=a.readlines()[::-1]
	stroka=text[1:2]
	#print(type(stroka))
	print(stroka[0])
'''

'''
#with open('sheet1.txt','r',encoding='utf-8') as s:
sheet = "sheet1.txt"    #это мля ввод будет
mean = "mean1.txt"
with open(sheet,'r',encoding='utf-8') as s:
	text=s.read().split()	
	summ=0
	k=0
	sch=0
	for i in text:
		'''
'''
		match i:
			case '(экзамен)':
				summ=summ+int(text[k-1])
				sch=sch+1
			case '(автомат)':
				summ=summ+int(text[k-1])
				sch=sch+1	
'''
'''
		if i == '(экзамен)':
			summ=summ+int(text[k-1])
			sch=sch+1
		elif i == '(автомат)':
			summ=summ+int(text[k-1])
			sch=sch+1	
		k=k+1		
	ball=summ/sch
with open(mean) as b:
	sr_ball=float(b.read())	
	if ball == sr_ball:
		print('OK')
	else:
		print('ERROR')
'''

'''
with open(sheet, encoding='utf-8') as f1, open(mean, encoding='utf-8') as f2:
	nums = [int(i) for i in f1.read() if i.isdecimal()]
	s = sum(nums) / len(nums)
	m = float(f2.read().strip())
print(['ERROR', 'OK'][s == m])
'''

'''
import os.path
p=input()
if os.path.exists(p):
	if os.path.isfile(p):
		#print('peace')
		with open(p, encoding='utf-8') as f:
			text=f.read()
			print('CONTENT:',text,sep='\n')
	else:
		print('ERROR:','Это каталог, а не файл',sep='\n')
else:
	print('ERROR:','Файл не существует',sep='\n')
'''

'''
try:
	with open(input(), mode="r", encoding="utf-8") as file:
		print("CONTENT:")
		print(file.read())
except FileNotFoundError:
	print("ERROR:")
	print("Файл не существует")
except IsADirectoryError:
	print("ERROR:")
	print("Это каталог, а не файл")
'''


'''
import os.path
n = input()

if os.path.isfile(n):
	print("CONTENT:",open(n).read(), sep="\n")
elif os.path.isdir(n):
	print("ERROR:","Это каталог, а не файл", sep="\n" )
elif "dir" not in n:
	print("ERROR:","Файл не существует", sep="\n")	
'''


'''
#your code
text=input()
with open('output.txt','w') as f:
    f.write(text)
'''



'''	
#def first_record(f):
	

import os.path
event='git fetch origin'
file_name='tmp/git.log'

if os.path.isfile(file_name):
	print('file is here')
	with open(file_name, 'r', encoding='utf-8') as f:
		text=f.readlines() #list
		#text=f.read()      #str
		#print(type(text))
		#print(text)
		number=text[0].split()[1]
		print('number',number)
		
		
		print(len(text))
		if (len(text))>0:
			k=str(int(text[0].split()[1])+1)
		else:
			k=str(1)
		print(k)
		
		
	with open(file_name,'w',encoding='utf-8') as f:
		#print('event '+k+' - \''+event+'\''+'\n')
		f.writelines('event '+k+' - \''+event+'\''+'\n')
		f.writelines(text)
	
else:
	with open(file_name,'w',encoding='utf-8') as f:
		f.write('event 1 - \''+event+'\'')
'''



'''
from decimal import *

number = Decimal("3.5648575")
number = number.quantize(Decimal("1.000")) # 3.565 	
'''

'''
# import libraries
from math import atan
from decimal import *
def f(x):
	return 2*atan(x)
	# You code of function
x=int(input())
lim = Decimal(f(x)).quantize(Decimal('1.000'))#Your code of lim
print (lim)
'''

'''
from math import exp
from decimal import *
def def_e(x):
	dx=0.000000001
	lim=(exp(x+dx)-exp(x))/dx
	lim=Decimal(lim).quantize(Decimal('1.000'))
	return lim
	
	
	#pass

#x=float(input())
#print(exp(x))
a=int(input())
print('exp ',Decimal(exp(a)).quantize(Decimal('1.000')))
print('derivative exp ',def_e(a))	
'''

'''
def even_indeces(a):
	b=[]
	for i in range(0,len(a),2):
		#print(a[i])
		b.append(a[i])
	return b
	
	
a=list(input())
print(even_indeces(a))
'''
'''
def even_indeces(l):
	return l[::2]
'''

'''
n=int(input())
res=0
for i in range(n+1):
	#print(i)
	if (i%5==0) and (i%3!=0):
		res=res+i
print(res)
'''

'''
def common(list_a,list_b):
	b=[]
	for i in list_a:
		if i in list_b:
			b.append(i)
	return b
'''

'''
words=['mix', 'extra', '', 'x-files', 'xyz', 'xapple', 'apple']
def front_x(words):
	b=[]
	c=[]
	#b=sorted(words)
	words.sort()
	#print(b)
	#print(words)
	for i in words:
		if i!='' and i[0]=='x':
			#words.remove(i)
			#print(i)
			b.append(i)
		else:
			c.append(i)			
	
	#print(b)
	#print(c)
	words=b+c
	#print(words)
	return(words)
front_x(words)
'''


'''
def fib(n):
	fiba =0
	ch_1=0
	ch_2=1
	if n==1:
		fiba=1
	for i in range(2,n+1):
		#print(i)
		fiba=ch_1+ch_2
		ch_1=ch_2
		ch_2=fiba
	#print(fiba)
	return fiba
		
		
		
		
a=int(input())
fib(a)
'''

'''
def is_prime(n):
	from math import sqrt
	check=True
	for i in range(2,int(sqrt(n))+1):
		if n%i==0:
			check=False
			break
		print(i)
		
	if check==True:
		print(n,' Simple')
	else:
		print(n,' Compound')
		
		
	return check	

a=int(input())
is_prime(a)
'''
'''		
a=int(input())
def donuts(n):
	if n<=9:
		s=str(n)
	else:
		s='много'
	return 'Всего пончиков: '+s
print(donuts(a))
'''

'''
n = int(input())
def donuts(n):
	return f'Всего пончиков: {n}' if n<=9 else 'Всего пончиков: много'

print(donuts(n))
'''

'''
s = input()
def both_ends(s):
	# Your code
	#print(len(s))
	if len(s)>1:		
		a=s[0:2:]
		b=s[:-3:-1][::-1]
		out=a+b
	else:
		out=''
	return out


print (both_ends(s))
'''

'''
def both_ends(s):
	return '' if len(s) < 2 else s[:2] + s[-2:]

print(both_ends(input()))
'''


'''
s=input()
def fix_start(s):
	a=s[0]
	#print(s[1::])
	
	out=s[1::].replace(a,'*')
	return a+out
print(fix_start(s))
'''



'''
def rotor(symbol, n, reverse=False):
	ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
			  1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
			  2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
			  3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
			  4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
			  5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
			  6: 'JPGVOUMFYQBENHZRDKASXLICTW',
			  7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
			  8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
			  'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
			  'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
			  }	
	
	def change(symbol,first_rotor,second_rotor):
		#print((list(ROTORS[first_rotor])).index('A'))
		#b=list(ROTORS[first_rotor])
		#print(b.index('A'))
		text_change=''
		for i in symbol:
			b=(list(ROTORS[first_rotor])).index(i)
			c=ROTORS[second_rotor][b]
			#print(b,c)
			text_change=text_change+c
		return text_change		
		
		#print(ROTORS[0][-1])
	first_rotor=0
	second_rotor=n
	if reverse:
		first_rotor=n
		second_rotor=0
	
	text_change=change(symbol,first_rotor,second_rotor)	
	
	return text_change

#text='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#print(rotor(text,1,0))



def reflector(symbol,n):
	REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
				  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
				  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
				  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
				  }
	
	def change(symbol,reflector):
		#print((list(ROTORS[first_rotor])).index('A'))
		#b=list(ROTORS[first_rotor])
		#print(b.index('A'))
		symbol=symbol.replace(' ','')
		text_change=''
		for i in symbol:
			b=(list(REFLECTORS[0])).index(i)
			c=REFLECTORS[n][b]
			#print(b,c)
			text_change=text_change+c
		return text_change		

		#print(ROTORS[0][-1])	

	text_change=change(symbol,n)	

	return text_change

#text='SOME ENCRYPTED TEXT FOR EXAMPLE'
#disk=1
#print(reflector(text,disk))
'''

'''
def enigma(text,ref,rot1,rot2,rot3):
	
	def rotor(symbol, n, reverse=False):
		ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				  1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
				  2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
				  3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
				  4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
				  5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
				  6: 'JPGVOUMFYQBENHZRDKASXLICTW',
				  7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
				  8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
				  'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
				  'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
				  }	
		symbol=symbol.replace(' ','')
		def change(symbol,first_rotor,second_rotor):
			
			text_change=''
			for i in symbol:
				b=(list(ROTORS[first_rotor])).index(i)
				c=ROTORS[second_rotor][b]				
				text_change=text_change+c
			return text_change				
			
		first_rotor=0
		second_rotor=n
		if reverse:
			first_rotor=n
			second_rotor=0
		
		text_change=change(symbol,first_rotor,second_rotor)	
		
		return text_change
	
	def reflector(symbol,n):
		REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
					  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
					  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
					  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
					  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
					  }
		
		def change(symbol,reflector):			
			symbol=symbol.replace(' ','')
			text_change=''
			for i in symbol:
				b=(list(REFLECTORS[0])).index(i)
				c=REFLECTORS[n][b]				
				text_change=text_change+c
			return text_change			
	
		text_change=change(symbol,n)	
		return text_change	
	
	text=text.upper()
	tumbajumba=[ref,rot1,rot2,rot3]	
	way_flag=False
	for i in range(3,-4,-1):		
		if i!=0:
			if i<0:
				way_flag=True
			text=rotor(text,tumbajumba[abs(i)],way_flag)			
		else:
			text=reflector(text,ref)
			
	return text

text='Some encripted text'
ref=1
rot1=1
rot2=2
rot3=3
#text=text.upper()
print(enigma(text,ref,rot1,rot2,rot3))
'''

def enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3):
		
	def rotor(symbol, n, puksamuksa, reverse=False):
		ROTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
				  1: 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
				  2: 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
				  3: 'BDFHJLCPRTXVZNYEIWGAKMUSQO',
				  4: 'ESOVPZJAYQUIRHXLNFTGKDCMWB',
				  5: 'VZBRGITYUPSDNHLXAWMJQOFECK',
				  6: 'JPGVOUMFYQBENHZRDKASXLICTW',
				  7: 'NZJHGRCXMYSWBOUFAIVLPEKQDT', 
				  8: 'FKQHTLXOCBJSPDZRAMEWNIUYGV',
				  'beta': 'LEYJVCNIXWPBQMDRTAKZGFUHOS',
				  'gamma': 'FSOKANUERHMBTIYCWLQPZXVGJD'
				  }	
		symbol=symbol.replace(' ','')
		def change(symbol,first_rotor,second_rotor,puksamuksa):
			
			text_change=''
			for i in symbol:
				r=i
				if reverse:
					s=(ROTORS[second_rotor]).index(i)+puksamuksa
					#print('s',s)
					k=0
					if s>25:
						#k=-1
						s=s%26
					elif s<0:
						#k=26
						s=s+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s
					#print(ROTORS[second_rotor][b],b)
					r=ROTORS[second_rotor][b]
					b=(list(ROTORS[first_rotor])).index(r)
					c=ROTORS[second_rotor][b]
					text_change=text_change+c
				else:
					
					b=(list(ROTORS[first_rotor])).index(r)
					b=b+puksamuksa
					#print('b',b)
					s=b
					if s>25:
						#k=-1
						s=s%26
					elif s<0:
						#k=26
						s=s+26
					#b=((ROTORS[second_rotor]).index(i)+puksamuksa)//26+k
					b=s					
					
					c=ROTORS[second_rotor][b]				
					text_change=text_change+c
			return text_change				
			
		first_rotor=0
		second_rotor=n
		if reverse:
			first_rotor=n
			second_rotor=0
		
		text_change=change(symbol,first_rotor,second_rotor,puksamuksa)	
		
		return text_change
	
	def reflector(symbol,n,puksamuksa):
		REFLECTORS = {0: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',					  
					  1: 'YRUHQSLDPXNGOKMIEBFZCWVJAT',
					  2: 'FVPJIAOYEDRZXWGCTKUQSBNMHL',
					  3: 'ENKQAUYWJICOPBLMDXZVFTHRGS',
					  4: 'RDOBJNTKVEHMLFCWZAXGYIPSUQ',
					  }
		
		def change(symbol,reflector,puksamuksa):			
			symbol=symbol.replace(' ','')
			text_change=''
			for i in symbol:
				b=(list(REFLECTORS[0])).index(i)
				b=b+puksamuksa
				c=REFLECTORS[n][b]				
				text_change=text_change+c
			return text_change			
	
		text_change=change(symbol,n,puksamuksa)	
		return text_change		
	
	#---------------------------------------------------------------
	
	rel_shift3=shift3
	rel_shift2=shift2-rel_shift3
	rel_shift1=shift1-shift2
	#rel_shift1=shift1-rel_shift2    	
	shift_ref=shift1*(-1)
	puksamuksa=[rel_shift3,rel_shift2,rel_shift1,shift_ref]
	#print(puksamuksa,'1')
	prom=[]
	for i in reversed(puksamuksa):
		#print('2')
		#print(i)
		#prom.append(puksamuksa[i]*(-1))
		prom.append(i*(-1))
	#print(prom)
	puksamuksa=puksamuksa+prom
	#puksamuksa=[-1,3,-3,0,0,-3,3,-1]
	#print(puksamuksa)
	
	#----------------------------------------------------------
	def rotate_rotor(puksamuksa,tumbajumba,k,shift):
		ROTORS_ROTATE = {0: 5, 1: 17, 2: 5, 3: 22, 4: 10, 5: 0, 6: 0, 
						 7: 0, 8: 0, 'beta': 0, 'gamma': 0}			
		#k=k+1
		#puksamuksa_bias=puksamuksa.copy()
		print(puksamuksa)
		d2=0
		d3=0
		rel_shift3=shift[2]+1
		
		if rel_shift3%ROTORS_ROTATE[tumbajumba[3]] == 0:
			d2=1
			
		rel_shift2=puksamuksa[1]	
		if (rel_shift2+1)%ROTORS_ROTATE[tumbajumba[2]] == 0:
			d2=1
			d3=1
		rel_shift2=shift[1]-rel_shift3+d2
		
		rel_shift1=shift[0]-shift[1]+d3
		
		#rel_shift1=shift1-rel_shift2    	
		shift_ref=shift1*(-1)		
		puksamuksa_bias=[rel_shift3,rel_shift2,rel_shift1,shift_ref]
		print(puksamuksa_bias)
		for i in reversed(range(1,len(tumbajumba))):
			#print('i',i)
			
			pass
		
		return k

		
		
	
	
	shift0=0
	shift=[shift0,shift1,shift2,shift3]
	shift_rel=[]
	text=text.upper()	
	tumbajumba=[ref,rot1,rot2,rot3]		
	text_out=''	
	n=0
	print(rotate_rotor(puksamuksa,tumbajumba,n,shift))
	
	for text_symbol in text:
		#n=0     #proba
		#n=rotate_rotor(puksamuksa,tumbajumba,n)
		way_flag=False	
		k=0		
		for i in range(3,-4,-1):
			if i!=0:
				if i<0:
					way_flag=True
				text_symbol=rotor(text_symbol,tumbajumba[abs(i)],puksamuksa[k],way_flag)		
			else:
				text_symbol=reflector(text_symbol,ref,puksamuksa[k])
			k=k+1
			
			#n=rotate_rotor(puksamuksa,tumbajumba,n)
			
		#------------------------------------------------------------
								
		a='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		b=a.index(text_symbol)+puksamuksa[7]
		#print(b)		
		if b>25:
			#k=-1
			b=b%26
		elif b<0:
			#k=26
			b=b+26				
		text_symbol=a[b]		
		text_out=text_out+text_symbol
	
	#-----------------------------------------------------------
	#print(n)    #proba
	return text_out

text='AYIQQLXZMFHQUHQCH'
ref=1
rot1=1
shift1=-1
rot2=2
shift2=2
rot3=3
shift3=-1
#text=text.upper()
print(enigma(text,ref,rot1,shift1,rot2,shift2,rot3,shift3))
