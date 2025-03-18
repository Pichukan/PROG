'''
print('Я')
print()
print('будущий')
print()
print('Python-разработчик!')


print('Привет','мне','нравится','программирование',sep=';')
print()
print('но писать код что-то не очень.Может поможешь?')


print('hello',end='\n\n\n')
print('world')


#print('красный','оранжевый','желтый','зеленый',sep='\t')

print('Иван сказал: \"Ты зачем выделил все свои слова одинарными кавычками?\".')
print('Антон ответил: \"\'Если\' \'бы\' \'я\' \'знал\'\".')

'''



#print(type('python'))
'''
a=input()
b=input()
print(a,b)
'''

'''
name=input('Ваше имя:')
age=input('Ваш возраст:')
print(name,age)
'''


'''
ch=input()
stro=input()
print('Это число:', ch)
print('Это строка:', stro)
'''
'''
a=int(input())
b=int(input())
c=int(input())
d=(a**c+b**c)**(a*b)
print(d)
'''

'''
m=int(input())
ch=m//60
ost=m%60
print(ch,ost)
'''
'''
time_mins=int(input())
start_hours=int(input())
start_mins=int(input())
start=start_hours*60+start_mins
time_sum=start+time_mins
time_sum=time_sum%(60*24)
end_hours=time_sum//60
end_mins=time_sum%60
print(end_hours,end_mins)
'''

'''
a=int(input())
b=int(input())
n=int(input())
d=a*60+b
summ=d*n
vch=summ//(60*60)
vm=(summ-vch*60*60)//60
vs=(summ-vch*60*60)%60
print(vch,vm,vs)
'''
'''
a=int(input())
y=int(input())
x=int(input())
b=int(input())
ost1=int((a-x-b)*(1+y/100))
ost2=int((ost1-b)*(1+y/100))
ost3=int((ost2-b)*(1+y/100))
print(ost1)
print(ost2)
print(ost3)
'''
'''
a=float(input())
b=float(input())
c=float(input())

print((a**3+b**(1/2))/c)
'''

'''
x=float(input())
x=((abs(x)*100)%10)
print(int(x//1))
'''

'''
a=float(input())
b=float(input())
a*=100
b*=100
c=a+b
#c*=100
nak=0

r1=c*0.1
r1c=int(r1//1)
r1d=r1%1
nak=nak+r1d
print('Отпуск:',r1c//100,'руб.',r1c%100,'коп.')

r2=c*0.3
r2c=int(r2//1)
r2d=r2%1
nak=nak+r2d
print('Пропитание и еда:',r2c//100,'руб.',r2c%100,'коп.')

r3=c*0.05
r3c=int(r3//1)
r3d=r3%1
nak=nak+r3d
print('Коммунальные платежи:',r3c//100,'руб.',r3c%100,'коп.')

r4=c*0.15
r4c=int(r4//1)
r4d=r4%1
nak=nak+r4d
print('Досуг:',r4c//100,'руб.',r4c%100,'коп.')

r5=c*0.4+nak
r5c=int(r5//1)
r5d=int(r5%1)
nak=nak+r5d
print('Накопления:',r5c//100,'руб.',r5c%100,'коп.')
'''

'''
from decimal import Decimal, getcontext
getcontext().prec=60
a=Decimal(input())
b=Decimal(input())
d=a.sqrt()+b
print(d)
#c=Decimal(a**(1/2)+b)
#print(c)
'''


'''
from decimal import Decimal
import time

a, b, x = 0.1, 0.2, 0.3
start = time.time()
for _ in range(1_000_000):
	x += x * a - b

float_time = time.time() - start

a, b, x = Decimal("0.1"), Decimal("0.2"), Decimal("0.3")
start = time.time()
for _ in range(1_000_000):
	x += x * a - b

decimal_time = time.time() - start

print(round(decimal_time / float_time, 3))
'''


'''
import math
a=float(input())
b=float(input())
c=float(input())
print(math.ceil(a))
print(math.ceil(b))
print(math.ceil(c))
'''

'''
a=int(input())
print(bin(a))
print(oct(a))
print(hex(a))
'''



'''
x=int(input(),6)
print(hex(x))
'''
'''
x=int(input())
a=x//8
b=x%8
print(a,b,sep='')
'''


'''
a=int(input())
x=2**(8*a)
#print(x)
minn=int(-(x/2))
maxx=int(x+minn-1)
print(minn,maxx)
'''

'''
n=int(input())

min_number=-2**(8*(n)-1)
max_number=2**(8*(n)-1)-1

print(min_number)
print(max_number)
'''

'''
x=int(input())
k=47
print(int(x^k))
'''
'''
n=int(input())

print(((n>=5)and(n<10)) or ((n>101)and(n<=200)))
'''
'''
n=int(input())
print(n%2==0)
print(n>0)
print((n>=-5)and(n<=5))
print(((n%3==0)and(n%4==0))and(n%7!=0))
#print(((abs(n//100)>1 or n==100 or n==-100)) and (abs(n//100)<10))
print((-999<=n<=-100)or(999>=n>=100))
'''


'''
a=input()
b=input()
la=len(a)
lb=len(b)
print((la>4) and (lb>8) and (a!=b))
'''

'''
Например программу, преобразующую число в положительное можно написать так:

n = int(input())
print(n * (-1 + 2 * (n > 0)))
'''
'''
n=int(input())
#k=(2-((n%2)+1))  -  (2+((n%2)-2))
print(n+((2-((n%2)+1))  -  (2+((n%2)-2)))*10)

#n=n+10   *    (2-((n%2)+1))    (2+((n%2)-2))
#print(n)
'''
'''
a=int(input())
b=int(input())
if a<b:
	print(a)
else:
	print(b)
'''
'''
n=int(input())
d=int(n%7)
#print(d)
match d:
	case 0:
		print('пн')
	case 1:
		print('вт')
	case 2:
		print('ср')
	case 3:
		print('чт')
	case 4:
		print('пт')
	case 5:
		print('сб')
	case 6:
		print('вс')
'''

'''
n=int(input())
d=int(n%7)
#print(d)
if d==0:
	print('пн')
elif d== 1:
	print('вт')
elif d== 2:
	print('ср')
elif d== 3:
	print('чт')
elif d== 4:
	print('пт')
elif d== 5:
	print('сб')
elif d== 6:
	print('вс')
'''
'''
n1=0
n2=0
n3=0
n4=0
print(not(n1==0))
print((n1==n2)!=0)
print((n1==n2==n3==n4)!=0)
print(((n1==n2==n3==n4) != (0 or 255)))
if 0<=n1<=255 and\
   0<=n2<=255 and\
   0<=n3<=255 and\
   0<=n4<=255 and\
   (not(n1==n2==n3==n4==0) and not(n1==n2==n3==n4==255)):
	print('True')
else:
	print('False')
'''
'''
a=input()
b=input()
c=input()
al=int(len(a))
bl=int(len(b))
cl=int(len(c))
if al<bl and al<cl:
	k=a
elif bl<al and bl<cl:
	k=b
elif cl<al and cl<bl:
	k=c
elif bl==al and al<cl:
	k=b
elif bl==cl and bl<al:
	k=c
elif al==cl and cl<bl:
	k=c
elif al==cl==bl:
	k=c
	
print(k)
'''

'''
match a:=input():
	case 'Привет':
		print('Привет!')
	case 'Как дела?':
		print('Все классно!')
	case 'Пока':
		print('До скорой встречи!')
	case _:
		print('Прости, я еще не знаю таких фраз :(')
'''

'''
s=input()
if s=='Flask' or s=='Django' or s=='Fast-API':
	print('Python(',s,'),Backend-dev',sep='')
elif s=='Angular' or s=='React' or s=='Vue':
	print('JavaScript/TypeScript(',s,'),Frontend-dev',sep='')
elif s=='Flutter' or s=='React Native':
	print('JavaScript(',s,'),Cross-Mobile-dev',sep='')
elif s=='Pandas' or s=='skit-learn' or s=='keras':
	print('Python(',s,'),Data-Scientist',sep='')
else:
	print('модель еще не обучена')
'''
'''
a = [int(i) for i in input().split()] # [1,2,3,4]
for i in a:
	print(i)
'''
'''
values=input().split()
for i in values:
	print(i+'!')
'''


#range(5, 0, -1)
'''
a=int(input())
b=int(input())
k=1
for i in range(a,b+1):
	print(k*i)
	k*=-1
'''
'''
factorial
a=int(input())
f=1
for i in range(1,a+1):
	f*=i
print(f)
'''

'''
for i in range(1, 10):
	# 9 раз выполни код ниже
	for j in range(1, 10):
		# 9 раз выполни команду ниже
		print(i*j, end='\t')
	print()  # Это нужно, чтобы перевести каретку на новую строку
'''
'''
a=int(input())
if a==0:
	print(a)
for i in range(1,a+1):
	j=i
	for k in range(a,-1+j,-1):
		print(k,end=' ')
	print()
'''
'''
a=int(input())

for i in range(1,a+1):
	if i%2!=0:
		start=1
		end=a+1
		step=1
	else:
		start=a
		end=0
		step=-1
	for k in range(start,end,step):
		print(k,end=' ')
	print()
'''

'''
a=int(input())

for i in range(1,a+1):
	if i%2!=0:
		start=1
		end=a+1-(i-1)
		step=1
	else:
		start=a
		end=0+(i-1)
		step=-1
	for k in range(start,end,step):
		print(k,end=' ')
	print()	
'''
'''
sh=1
s=1
while True:
	a=int(input())
	if a==0 and sh==1:
		s=1
		break
	elif a==0:
		break
	s*=a
	sh+=1
	
print(s)
'''

'''
b=input()
n=int(b)
ch=''
flag=True
if n<0:
	flag=False
while flag:
	p=n%10
	ch=ch+str(p)
	if p==n:
		flag=False
	n=n//10
if ch==b:
	print('True')
else:
	print('False')
'''

'''
n1, n2, n3, n4 = [int(i) for i in input().split('.')]
# ваш код ниже (используйте переменные n1-n4)
correct_list = ['0.0.0.0', '128.0.0.0', '192.0.0.0', '224.0.0.0', '240.0.0.0', '248.0.0.0', '252.0.0.0', '254.0.0.0', '255.0.0.0', '255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0', '255.252.0.0', '255.254.0.0', '255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0', '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248', '255.255.255.252', '255.255.255.254', '255.255.255.255']

allstroce = (f"{n1}.{n2}.{n3}.{n4}")

if (allstroce in correct_list):
	print("True")
else:
	print("False")

# binary_mask = f"{n1:08b}{n2:08b}{n3:08b}{n4:08b}"	
'''	
	
'''
n1, n2, n3, n4 = [int(i) for i in input().split('.')]
m1, m2, m3, m4 = [int(i) for i in input().split('.')]

if 0<=n1<=255 and\
   0<=n2<=255 and\
   0<=n3<=255 and\
   0<=n4<=255 and\
   (not(n1==n2==n3==n4==0) and not(n1==n2==n3==n4==255)):
	IP=True
	#print('IP True')	
else:
	#print('IP False')
	IP=False

correct_list = ['0.0.0.0', '128.0.0.0', '192.0.0.0', '224.0.0.0', '240.0.0.0', '248.0.0.0', '252.0.0.0', '254.0.0.0', '255.0.0.0', '255.128.0.0', '255.192.0.0', '255.224.0.0', '255.240.0.0', '255.248.0.0', '255.252.0.0', '255.254.0.0', '255.255.0.0', '255.255.128.0', '255.255.192.0', '255.255.224.0', '255.255.240.0', '255.255.248.0', '255.255.252.0', '255.255.254.0', '255.255.255.0', '255.255.255.128', '255.255.255.192', '255.255.255.224', '255.255.255.240', '255.255.255.248', '255.255.255.252', '255.255.255.254', '255.255.255.255']

allstroce = (f"{m1}.{m2}.{m3}.{m4}")

if (allstroce in correct_list):
	#print("mask IP True")
	mask_IP=True
else:
	#print("mask IP False")
	mask_IP=False


N=n1,n2,n3,n4
M=m1,m2,m3,m4
PB=''
PD=''
for j in range(4):
	
	nb=(str(format(N[j],'b'))).zfill(8)
	#print(nb,'nb')
	mb=(str(format(M[j],'b'))).zfill(8)
	#print(mb,'mb')
	pb=''
	for i in range(8):
		#print(nb[i],mb[i])
		if (nb[i] == mb[i]) and (nb[i] == '1'):
			pb+='1'
		else:
			pb+='0'
	#print(pb,'pb')
	PB=PB+pb+'.'
	PD=PD + str(int(pb,2)) + '.'
#print(PB[:-1])
if IP and mask_IP:
	print(PD[:-1])
else:
	print('Валидация не пройдена')
'''

'''
s = input().split()
if len(s)==1:
	a=s[0]
	print(a)
else:
	a=s[0]
	b=s[1]
	#print(a)
	#print(b)
'''	

'''
flag=True
while flag:	
	
	s = input().split()
	if len(s)==1:
		a=s[0]
		#print(a)
	else:
		a=s[0]
		b=s[1]
		#print(a)
		#print(b)	
	
	match a:
		case 'zero':
			sch=0
		case 'add':
			sch+=int(b)
			#print(sch)
		case 'minus':
			sch-=int(b)
		case 'mul':
			sch*=int(b)
		case 'div':
			sch//=int(b)
		case 'result':
			print(sch)
		case 'exit':
			flag=False
'''

'''
s=input()
if s.isdigit():
	print(int(s)*3)
else:
	print('не число')
'''


'''
s=input()
for i, value in enumerate(s):
	print (value*(i+1))
'''

#s = "backend"
#print(s[-2:1:-1])


'''
s=input()
print(s[-1:0:-1])
'''
'''
s=input()
print(s[1]*4)
print(s[-2:]+'!')
print(s[:-3])
print(s+s[::-1])
print(s[1::2])
print(s[::2])
'''

#print(ord('ъ'))
'''
s=input()
step=int(input())
k=0
for i in s:
	if ((((ord(i)+step)-97)%25) == 0) and ((((ord(i)+step)-97)//25) == 1):
		k=25
	index=(((ord(i)+step)-97)%25    ) +k +97-1*(((ord(i)+step-1)-97)//25)
	#print(index, chr(index))
	print(chr(index),end='')
	k=0
'''
'''
s=input()
step=int(input())
step=26-step
k=0
for i in s:
	
	if ((((ord(i)+step)-97)%25) == 0) and ((((ord(i)+step)-97)//25) == 1):
		k=25
	index=(((ord(i)+step)-97)%25    ) +k +97-1*(((ord(i)+step-1)-97)//25)
	#print(index, chr(index))
	print(chr(index),end='')
	k=0
'''
'''
s=input()
ch=1
maxx=1
ress=len(s)-1
for i in range(1,len(s)):
	if s[i]==s[i-1]:
		ch=ch+1
		if ch>=maxx:
			maxx=ch
			ress=i
	else:
		ch=1
		#res=1
print(s[ress],maxx,sep='\n')
'''

'''
s=input()
print(s.count(' ')+1)
'''

'''
num=float(input())
print(f"{num:.3f}")  # 
'''

'''
a=[int(i) for i in input().split()]
res=[]
for i in range(1, len(a)):
	#print(a[i])
	#res.append(a[i]+a[i-1])
	print(a[i]+a[i-1],end=' ')
#print(res)
'''
'''	
a=[int(i) for i in input().split()]
if a[0] > a[1]:
	second=a[1]
	first=a[0]
else:
	second=a[0]
	first=a[1]
	
	
for i in range (2,len(a)):
	if (a[i] > second) and (a[i] < first):
		second=a[i]
	elif (a[i] > second) and (a[i] > first):
		second=first
		first=a[i]
print(second)
'''

'''
a=[int(i) for i in input().split()]
k=a.count(0)
b=[]
for i in range(len(a)):
	#print(a[i], i, end=' ')
	if a[i] != 0:
		b.append(a[i])
		#pass
		#b.remove(a[i])

#print(b)
for i in range (k):
	b.append(0)
print()
for i in b:
	
	print(i,end=' ')
'''

'''
for i in range(10):
	print(i,end=' ')
	if i == 3:
		i=5
'''

'''
a=[int(i) for i in input().split()]
#k=a.count(0)
b=[]
for i in range(len(a)):
	#print(a[i], i, end=' ')
	if (a[i]%2) == 0:
		b.append(a[i])
		#pass
		#b.remove(a[i])

#print(b)

for i in b:
	
	print(i,end=' ')
'''


'''
a=[int(i) for i in input().split()]
a.sort()
#print(a)
if (len(a))%2 == 0:
	k=int(len(a)//2)
	med=(a[k-1]+a[k])/2
	
	if int(med)==med:
		print(int(med))
	else:
		print(f"{med:.1f}")
	#print(med)
else:
	k=int(len(a)/2)
	print(a[k])
'''
'''
a=set()
while True:
	b=int(input())
	a.add(b)
	if b == 0:
		break
print(len(a))
'''
'''
a = {int(i) for i in input().split()}
sumka=0
for i in a:
	#print(i)
	sumka+=i**2
	#print(sumka)
print(sumka)
'''
'''
print(
	len(
		{
			i.replace('b','d',1) if i.startswith('b') else i.replace('c','') 
			for i in ['aa','bbb','cccc', 'bacbac'] if len(i) > 2
		}
	)
)
'''
'''
c={1,2,3,4,5
   }
a={1,2,4}
b={3,4}
print((a|b)==c)
'''


'''
required  = {i for i in input().split()}
optional  = {i for i in input().split()}
user_data = {i for i in input().split()}

print((required.issubset(user_data)) & (user_data-required).issubset(optional))
#print((user_data-required).issubset(optional))
'''



			

'''		
b=input().split()
b.sort()
#print(b)
a=set(b)
#print(type(a))
c = {i:b.count(i) for i in a}
#print(c)
cc=dict(sorted(c.items()))
#print(cc)

for key, value in cc.items():
	print(key, value)
'''



'''
users = [
	{
		"id": 1,
		"name": "Anton",
		"position": {
			"name": "Backend",
			"lang": "Python"
		}
		},
	{
		"id": 1,
		"name": "Ivan",
		"position": {
			"name": "Frontend",
			"lang": "JS"
		}
		},
]


print(users[1]["name"], users[0]["position"]["name"])
'''

'''
import json
d = json.loads(input())
#print(type(d))
#print(len(d))
#a=dict((d[0]))
#print(type(a))
#print(a)
#print(a['age'])
#print(a['chief'])
#c=dict(a['chief'])
#print(type(c))
#print(c['age'])

maxx=int(dict((d[0]))['age'])
for i in range(len(d)):
	a=dict(d[i])
	#print(a)
	a1=int(a['age'])
	c=dict(a['chief'])
	a2=int(c['age'])
	#print(a1,a2)
	if a1 > maxx:
		maxx=a1
	if a2 > maxx:
		maxx=a2
print(maxx)
'''



'''
n=input()
print(n)
print(type(n))
c=list(n.split())
print(c[1])
#print(type(n))
'''
'''
from collections import Counter
n=input().split()
#print(type(n))
adress = []
code = []
while n[0] != 'end':
	
	adress.append(n[0])
	code.append(n[1])
	n=input().split()


coladr=list(set(adress))
coladr.sort()

colcod=list(set(code))
colcod.sort()

a=Counter(adress)
c=Counter(code)

for i in colcod:
	print(i,c[i])

for i in coladr:
	print(i,a[i])

#print(adress[0])
#print(a[adress[0]])
#print(c)
'''


'''
n=[]
while True:
	a=input()
	if a == '-1':
		break
	n.append(a)
	
#print(len(n))	
	
for i in range(len(n),0,-1):
	print(n[i-1])
'''

'''
a = []
while (i := input()) != "-1":
	a.append(i)
for i in range(len(a)):
	print(a.pop())
'''
'''
a=[]
flag = True
while flag:
	n=input().split()
	#print(n)
	#print(type(n))
	m=str(n[0])
	match m:
		case 'add':
			a.append(n[1])
		case 'close':
			break
		case 'pop':
			print(a.pop()) #удаляет и возвращает обьект
		case 'head':
			l=len(a)-1
			print(a[l])

#print(a)
'''

'''
flag=True
n=[]
while flag:	

	s = input().split()
	if len(s)==1:
		a=s[0]
		#print(a)
	else:
		a=s[0]
		b=s[1]
		#print(a)
		#print(b)	

	match a:
		case 'add':
			n.append(b)
		case 'pop':
			print(n.pop()) #удаляет и возвращает обьект
		case 'head':
			l=len(n)-1
			print(n[l])
		case 'close':
			flag=False
'''
'''
from collections import deque

queue = deque()

queue.appendleft(1)
queue.appendleft(2)
print(queue) # deque([2, 1])

f = queue.pop()

print(f) # 1
print(type(queue))
'''


'''
from collections import deque
flag=True
queue=deque()

while flag:	
	s = input().split()
	a=s[0]	
	match a:
		case 'add':
			queue.appendleft(s[1])
		case 'pop':
			print(queue.pop()) #удаляет и возвращает обьект 
		case 'head':
			f=queue.pop()
			print(f)
			queue.append(f)			
		case 'close':
			flag=False
'''


'''
from heapq import heappush, heappop

heap = []

heappush(heap, -12)
heappush(heap, -7)
heappush(heap, 24)
heappush(heap, 11)
heappush(heap, 50)
heappush(heap, 6)

print(heap) # [6, 11, 7, 12, 50, 24]
print(heappop(heap)) # 6
print(heappop(heap)) # 7
print(heappop(heap)) # 11
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)	
'''
'''
from heapq import *
a=[12,7,24,11,50,6]
print(a)
heapify(a)
print(a)
'''

'''	
def multip_num(listt, num):
	new_list = list()
	for i in listt:
		new_list.append(int(i) * num)
	return new_list

from heapq import *

flag=True
heap=[]
s=input().split()
heap=(multip_num(s,-1))
heapify(heap)

while flag:	
	s = input().split()
	a=s[0]	
	match a:
		case 'insert':
			heappush(heap, (int(s[1]))*(-1))
		case 'pop':
			print((heappop(heap))*(-1)) #удаляет и возвращает обьект 
		case 'end':
			flag=False
'''
'''
def multip_num(listt, num):
	new_list = list()
	for i in listt:
		new_list.append(int(i) * num)
	return new_list

from heapq import *

flag=True
heap=[]

while flag:	
	s = input().split()
	a=s[0]	
	match a:
		case 'task':
			b=s[1].split(',')
			d=multip_num(b,-1)
			d.reverse()
			c=tuple(d)
			heappush(heap, c)			
		case 'take':			
			a=heappop(heap)			
			print(f'Задача {int(a[1])*(-1)} с приоритетом {int(a[0])*(-1)}')			 
		case 'end':
			flag=False
'''
'''
d = {}
for i, j in [input().split() for string in range(int(input()))]:
	d.setdefault(j, []).append(i)

print(*['\n'.join([f'{k} {v}' for v in sorted(vs)]) for k, vs in sorted(d.items())], sep='\n<->\n')

'''

'''
d = {}

for _ in range(int(input())):
	city, country = input().split()
	d.setdefault(country, []).append(city)

res = ['\n'.join(f'{co} {ct}' for ct in sorted(d[co])) for co in sorted(d)]
print(*res, sep='\n<->\n')   
'''

'''
# put your python code here
from collections import OrderedDict

sp = []

for i in range(int(input())):
	sp.append(input())

#print(sp)
#exit()

res = dict()
for i in range(len(sp)):
	city, country = sp[i].split(' ')
	if country in res.keys():
		res[country].append(city)
	else:
		res[country] = [city]

token = ''


od = OrderedDict(sorted(res.items()))
for country, cities in od.items():
	s = token
	token = '<->\n'
	for city in sorted(cities):
		s += country + ' ' + city + '\n'
	print(s[:-1])
'''

'''
import bisect
a = []
while (i := input()) != "change":
	a.append(int(i))
a.sort()
while (i := input()) != "close":
	
	i=int(i)
	r=bisect.bisect_right(a,i)
	l=bisect.bisect_left(a,i)
	if (r-1) == l:
		print(l)
	else:
		print(r-1)
	
	#print(bisect.bisect_left(a,i))
'''

'''
d = {'a': '1', 'b': '2', 'c': '3'}
s = 'abacaba'
table = s.maketrans(d)
print(s.translate(table))
'''

'''
a=['Anton', 'Andrey']
print(type(a))
b=['+79000000000','+79000000001']
mobile = dict(zip(a, b))
print(mobile)
'''

'''
ru = list("йцукенгшщзхъфывапролджэячсмитьбюё")
#print(ord(ru[0]))
#print(ord(ru[-1]))
en = list("qwertyuiop[]asdfghjkl;'zxcvbnm,.`")
#print(type(ru))
sl_ru_eng=dict(zip(ru,en))
sl_eng_ru=dict(zip(en,ru))
sl_all={'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']', 'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h', 'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n', 'ь': 'm', 'б': ',', 'ю': '.', 'ё': '`', 'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '`': 'ё'}
s=input()
#print(s[0])

if (ord(s[0]) >= 96) and (ord(s[0]) <= 113):
	table=s.maketrans(sl_eng_ru)
	print(s.translate(table))
	
#print(ord(s[0]))
if (ord(s[0]) >= 1081) and (ord(s[0]) <= 1105):
	#print('Hi')
	table=s.maketrans(sl_ru_eng)
	print(s.translate(table))


table=s.maketrans(sl_all)
print(s.translate(table))

'''

'''
import requests

host = "https://httpbin.org"
r = requests.get(host + "/get")

print(r) # <Response [200]>
print(r.status_code) # 200
print(r.json()) # {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', ...
'''

'''
import requests

host = "https://httpbin.org"
r = requests.get(host + "/get2") # ошибка в пути
r.raise_for_status()  # requests.exceptions.HTTPError
'''


'''
import requests

host = "https://httpbin.org"

for url in [host+'/get', host+'/get_incorrect']:
	try:
		r = requests.get(url)
		r.raise_for_status()
	except requests.HTTPError as e:
		print("HTTPError:", e)
	except Exception as e:
		print("Something went wrong with request:", e)
	else:
		print(r.status_code)
		print(r.json())
'''

'''
import requests

host = "https://cataas.com"
url = host + "/api/cats"

try:
	r = requests.get(url, params={"limit": 1})  # добавили параметр limit к запросу, чтобы получить 10 котиков
	r.raise_for_status()
except requests.HTTPError as e:
	print("HTTPError:", e)
except Exception as e:
	print("Something went wrong with request:", e)
else:
	print(r.url)  # https://cataas.com/api/cats?limit=10
	print(r.status_code)  # 200
	print(r.json())  # [{'_id': 'pHI5uPNXG66s7LqF', 'mimetype': 'image/jpeg', 'size': 25607, 'tags': ['cat', 'laying']}, ...
'''


#https://api.agify.io?name=elena

'''
import requests

url = "https://api.punkapi.com/v2/beers"
params = {
	"beer_name": "ipa",
	"brewed_before": "01-2008"
}

response = requests.get(url, params=params).json()
print(response[0]['id'])
'''

'''
import requests

response = requests.get(
	"https://api.spaceflightnewsapi.net/v4/articles/").json()
print(response["results"])
'''

'''
https://api.thedogapi.com/v1/images/search?limit=10&breed_ids=258&api_key=live_I8NTa3lxINYWCO7InbhPdoEIQ1uCYDVcfN0Oo4UCdI3PUNAkKtKGjUNJ2yAzwWJq
'''

'''
from collections import OrderedDict
administration = OrderedDict({'Owner':'Дмитрий', 'Editor':'Михаил', 'PR manager':'Оксана'})

print(administration.items()[0])
list(administration.items())[-1]
'''

'''
with open('file.txt', mode='r', encoding='utf-8') as f:
	a=f.read()
'''

'''
from datetime import date
import calendar
d1 = input()
d2 = input()
dd1=date.fromisoformat(d1)
dd2=date.fromisoformat(d2)

#	#print('Hi')

year=dd1.year
try:
	dd1=dd1.replace(dd2.year)
	dd2=dd2.replace(year)
	print(dd1,dd2,sep='\n')
except:
	print('Год изменить невозможно')
'''

'''
import calendar
from datetime import date

d1 = date.fromisoformat(input())
d2 = date.fromisoformat(input())

if (d1.year != d2.year) or (d1.month != d2.month):
	#print(calendar.monthrange(year=2023, month=3)[1])
	day_month = calendar.monthrange(year=d1.year, month=d1.month)[1]
	print(day_month-int(d1.day)+1)
else:
	print(int(d2.day)-int(d1.day)+1)
'''


'''
from datetime import timedelta
from datetime import date

d1 = date.fromisoformat(input()+'-01-01')
d2 = date.fromisoformat(input()+'-01-01')

delta=d2-d1
print(abs(delta.days))
'''


'''
from datetime import timedelta
from datetime import time


t1 = time.fromisoformat(input())
t2 = time.fromisoformat(input())

dt1=timedelta(hours=t1.hour,minutes=t1.minute,seconds=t1.second)
dt2=timedelta(hours=t2.hour,minutes=t2.minute,seconds=t2.second)




if dt2 > dt1:
	print(str(abs(dt2-dt1)).zfill(8))
else:
	print(dt1-dt2)

#delta = timedelta(t2) - timedelta(t1)
#print(delta)
'''
'''
import datetime

dt1=datetime.datetime.fromisoformat(input())
dt2=datetime.datetime.fromisoformat(input())
dt=dt2-dt1
seconds=int(dt.days)*24*60*60


print(abs(seconds+int(dt.seconds)))
#print(dt.days)
'''
import zoneinfo
from zoneinfo import ZoneInfo
from datetime import datetime, timezone, timedelta
print(zoneinfo.available_timezones())
tz1 = timezone(offset=-timedelta(hours=3, minutes=46))
tz2 = ZoneInfo("Europe/Moscow")

d = datetime.fromisoformat(input())

print(d.astimezone(tz1).isoformat())
print(d.astimezone(tz2).isoformat())