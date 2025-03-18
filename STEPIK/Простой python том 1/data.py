'''
a=int(input())
b=int(input())
print(f'{a+b}')
'''

'''
a=float(input())
n=int(input())
b=a**n
print(f'{b:.3f}')

name = input()
print(f'Здравствуй, {name}!')
print(f'До свидания, {name}!')
'''
'''
#a, b = map(int, input().split())

k_rise, k_veg = map(int, input().split())
summ=k_rise+k_veg*2
print(summ)
#print(type(k_rise))
'''

'''
length, width = map(float, input().split())
print(f'{length*width}')
'''
'''
a=int(input())
print(a//4)
'''

'''
tracklen, total = map(int, input().split())
print(total//tracklen, total%tracklen)
'''
'''
s, w, ch = map(float,input().split())
l=s/w
print(int(l//ch))
'''
'''
n, day = map(int, input().split())
prom1=n-day
prom2=int(prom1//7+1)
print(prom2)
'''
'''
n=int(input())
k=float(input())
prom=int(n-n*k)
print(prom)
'''
'''
rub, kop = map(int, input().split())
summ=rub*100+kop
n=int(summ//106)
rest=int(summ%106)
print(n,rest)
'''

'''
g1, s1, k1 = map(int, input().split())
g2, s2, k2 = map(int, input().split())
summ=k1+k2+(s1+s2)*29+(g1+g2)*17*29
g0=17*29
s0=29
g=summ//g0
s=(summ-(summ//g0)*g0)//s0
k=summ-g*g0-s*s0  
print(g, s, k)
'''
'''
import math
a=float(input())
b=float(input())
c=math.sqrt(a**2+b**2)
print(c)
'''
'''
import math
x=float(input())
c=math.sin(x)+math.cos(3*x)
print(c)
'''
'''
import math
x=float(input())
x=math.radians(x)
c=math.sin(x)+math.cos(3*x)
print(c)
'''
'''
a=float(input())
c=int(input())
b=round(a,c)
print(b)
'''
'''
def flag():
    print('*')
    print('**')
    print('*')
    print()
flag()
flag()
flag()
flag()
'''
'''
def flag():
    print('**')
    print('**')
    print()
'''
'''
def reverse(n):
    print(n%10,sep='',end='')
    n=n//10
    print(n%10,sep='',end='')
    n=n//10
    print(n%10,sep='',end='')
    n=n//10
    print(n%10,sep='',end='')
    n=n//10
    print(n%10,sep='',end='')
    n=n//10
    print(n%10,sep='')
a=int(input())
b=int(input())
c=int(input())
reverse(a)
reverse(b)
reverse(c)
'''
'''def volume(a, b, c):
    z=a*b*c
    return z

x, y, z = map(float, input().split())   # читаем числа
v = volume(x, y, z)                     # вызываем функцию
print(v)                                # печатаем результат
'''    
'''
from math import sqrt  # функция вычисляет квадратный корень

def dist(x1, y1, x2, y2):
    c=sqrt((x1-x2)**2+(y1-y2)**2)# тут нужно написать код
    return c

x1, y1, x2, y2 = map(float, input().split())    # читаем числа
d = dist(x1, y1, x2, y2)                        # вызываем функцию
print(d)                                        # печатаем результат
'''

'''
from math import sqrt  # функция вычисляет квадратный корень

def dist(x1, y1, x2, y2):
    c=sqrt((x1-x2)**2+(y1-y2)**2) # тут нужно написать код
    return c                      # скопируйте код из предыдущей задачи

def area(x1, y1, x2, y2, x3, y3):
    a=dist(x1,y1,x2,y2)
    #print('a',a)
    b=dist(x2,y2,x3,y3)
    #print('b',b)
    c=dist(x3,y3,x1,y1)
    #print('c',c)
    p=(a+b+c)/2
    #print('p',p)
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s                      

x1, y1, x2, y2, x3, y3 = map(float, input().split())
s = area(x1, y1, x2, y2, x3, y3)
print(s)
'''

'''
def time2min(h, m):
    mm=(h*60+m)
    return mm                             # тут нужно написать код

h, m = map(int, input().split(':')) # делю строку на слова по `:`
mm = time2min(h, m)
print(mm)
'''
'''
def min2time(mm):
    # тут нужно написать код
    mm=mm%(12*60)
    h = mm//60
    m = mm%60
    return h, m             # возвращает 2 числа, пишем через запятую

mm = int(input())
h, m = min2time(mm)
print(f'{h:02}:{m:02}')     # печатаем по формату hh:mm
'''
'''
def time2min(h, m):
    mm=(h*60+m)
    return mm      

def min2time(mm):
    mm=mm%(12*60)
    h = mm//60
    m = mm%60
    return h, m          

h, m = map(int, input().split(':'))
mm=time2min(h, m)
h, m = map(int, input().split(':'))
mm=mm+time2min(h, m)
h, m = min2time(mm)
print(f'{h:02}:{m:02}')
'''
'''
def time2min(h, m):
    mm=(h*60+m)
    return mm      

def min2time(mm):
    mm=mm%(12*60)
    h = mm//60
    m = mm%60
    return h, m          

h, m = map(int, input().split(':'))
mo=time2min(h, m)
h, m = map(int, input().split(':'))
mp=time2min(h, m)
#mm=mm+time2min(h, m)
mm=(mp-mo)%(12*60)
h, m = min2time(mm)
print(f'{h:02}:{m:02}')
'''
'''
def eq_float(a, b, tolerance=0.0001):
    return abs(a - b) < tolerance  
'''    
'''
x=int(input())
if x==0:
    print('Делить на 0 нельзя')
'''
'''
n, k_rice, k_veg = map(int, input().split(' '))
stoim=k_rice+2*k_veg
print(stoim)
if stoim < n:
    
    print('YES')
'''
'''
m, sm = map(int, input().split(' '))
rost=m*100+sm
print(rost)
if rost >= 175:
    if rost <= 190:
        print('Президентский полк')
'''
'''
#високосный год
def leap_year(year):
    if year % 4 == 0:
        #return True
        if year % 100 != 0:
            return True
    if year % 400 == 0:
        return True
    return False

x = int(input())
print(x)
if leap_year(x):
    print('Високосный год')
'''

'''
x=input()
y=input()
if x==y:
    print('Совпадают')
else:
    print('Пароли не совпадают')
'''
'''
v=int(input())
if v>=18:
    print('YES')
else:
    print('NO')
'''
'''
x1, x2 = map(int, input().split())
if x1<x2:
    print(x1)
else:
    print(x2)
'''
'''
n, k = map(int, input().split())
x=n//4
if x>=k:
    s=k
else:
    s=x
print(s)
'''
'''
amount = int(input())

comission_percent = 1 if amount < 1000 else 5

total = int(amount * (1 + comission_percent / 100))
print(total)
'''
'''
def distance (age):
    
    if 10 <= age < 15:
        print(1)
    if age < 10:
        print(0)        
    if age >= 15:
        print(2)
age=int(input())
distance(age)
'''

'''
x=int(input())
y=int(input())
if y >= 10:
    k=1
elif y >= 5:
    k=0.35
else:
    k=0
print(f'{round(x*k)}')
'''


#h, m = map(int, input().split(':')) # указываем ':' в split и читаем строку вида 
'''
a, b = map(int, input().split(':'))
if a>b:
    s=2
elif a==b:
    s=1
else:
    s=0
print(s)
'''

'''
Этот материал новичкам лучше пропустить и вернуться к нему, когда вас будет ждать собеседование по python

Мы уже знакомы с преобразованием типа явным и неявным.

int(x) - явно преобразуем значение переменной x к типу int.
3 < 3.14 - неявно преобразуем типы. Сначала оба операнда приводятся к одному типу float, потом вычисляется значение выражения 3.0 < 3.14
Для преобразования типа используются встроенные функции int(), float(), str(), bool() и другие. Имя функции совпадает с именем типа.

bool -> int
При преобразовании bool к int получим 1 (истина) или 0 (ложь).

Выражение	Результат
int(True)	1
int(False)	0
? -> bool
Преобразование к bool чуть сложнее.

Результат False (много чего ещё не знаем, но лучше запишите в конспект и будете обращаться к нему по мере изучения):
число 0 в любом виде: 0, 0.0, комплексное 0 + 0j
константа None
пустая коллекция: пустая строка "" и другие коллекции [], (), {}, dict()
Результат True - все остальное
Выражение	Результат
bool(0)	False
bool(1)	True
bool(1234)	True
bool(-4.5)	True
Применение в коде (устойчивое выражение проверки на пустоту и непустоту строки):

if "":
    print('Пустая строка - это True')
else:
    print('Пустая строка - это False')  # <-- будет напечатано это
Примеры
Так писать нельзя, потому что ваш код должен быть хорошо читаемым, а не головоломкой! Эти примеры любят давать на собеседованиях. С моей точки зрения должно хватить ответа "не надо так писать".

С явным преобразованием ясно. Но как вычисляется значение выражения 0 == False, 5 != True, 5 > True, -5 < True, 5 < True, True + True?

== и != - оба операнда приводятся к типу bool

0 == False это bool(0) == False, то есть False == False, верно, значение всего выражения True.

5 != True это bool(5) != True, это True != True, ложь, False.

Сравнения с больше или меньше, арифметические операторы - приводятся к численному типу.

5 > True это 5 > int(True), то есть 5 > 1, истина, True.

True + True это int(True) + int(True), то есть 1 + 1, то есть 2.

Ещё больше удивительных фактов из Python можно узнать в WFT python


Перепишем через match/case. Все время сравнивается с константой выражение x:

x = int(input())

Если все условия это проверка, что какое-то выражение равно тому или иному шаблону, то эту конструкцию можно записать через оператор match/case. Так как мы еще знаем мало конструкций языка python, разберем только один из вариантов шаблона: равенство константе.

match выражение:
    case константа1:
        операторы1
    case константа2:
        операторы2
    case константа2:
        операторы3
    case _:
        операторы4
ключевые слова match и case
проверяем только равенство одного выражения разным константам
_ - аналог else, не обязательная часть


match x:
    case 10:
        print('отлично')
    case 9:
        print('отлично')
    case 8:
        print('отлично')
    case 7:
        print('хорошо')
    case 6:
        print('хорошо')
    case 5:
        print('хорошо')
    case 4:
        print('удовлетворительно')
    case 3:
        print('удовлетворительно')
    case 2:
        print('неудовлетворительно')
    case 1:
        print('неудовлетворительно')
    case _:
        print('Такой оценки не существует")
Хочется в перечислении сказать "равно 10 или 9 или 8". Это записывают через | так:

x = int(input())


match x:
    case 10 | 9 | 8:
        print('отлично')
    case 7 | 6 | 5:
        print('хорошо')
    case 4 | 3:
        print('удовлетворительно')
    case 2 | 1:
        print('неудовлетворительно')
    case _:
        print('Такой оценки не существует")
Работает так же. Написано короче.
'''
''''
def convert_to_season(month, day):
    ch1=31
    ch2=30
    ch3=28
    
    if ((month<=2) or month==12):
        s=0
        m=month-s*3+1
        if month == 12:
            m=1
        
    elif 2<month<=5:
        s=1
        m=month-s*3+1
    elif 5<month<=8:
        s=2
        m=month-s*3+1
    else:
        s=3
        m=month-s*3+1
    
    match s:
        case 0:
            match m:
                case 1:
                    d=day
                case 2:
                    d=day+ch1
                case 3:
                    d=day+ch1*2
        case 1:
                    match m:
                        case 1:
                            d=day
                        case 2:
                            d=day+ch1
                        case 3:
                            d=day+ch1+ch2 
        case 2:
                    match m:
                        case 1:
                            d=day
                        case 2:
                            d=day+ch2
                        case 3:
                            d=day+ch1+ch2                            
        case 3:
                    match m:
                        case 1:
                            d=day
                        case 2:
                            d=day+ch2
                        case 3:
                            d=day+ch1+ch2                            
    return s, d


month, day = map(int, input().split('-'))
season, season_day = convert_to_season(month, day)
print(f'{season}-{season_day:02}')
'''
'''
Порядок вычислений
Порядок вычислений выражений с логическими операторами похож на порядок вычислений с арифметическими операторами.

Порядок вычисления операций в выражении определен приоритетом операций. Для арифметических операций таблица приоритетов и ассоциативности операций такая:

Приоритет	Операторы	Описание	Ассоциативность
1	()	Скобки	Cлева направо
2	**	Степень	Справа налево
3	-x	Унарный минус	Справа налево
4	*, /, //, %	Умножение, деление, целочисленное деление, остаток	Слева направо
5	+, –	Сложение, вычитание	Слева направо
6	=	Присвоить	Справа налево
Приоритет
Приоритет - какая операция выполнится раньше. Самая высокоприоритетная операция (), поэтому ими можно изменить последовательность выполнения любых операций.

2 + 3 * 4 - сначала выполнится 3 * 4, потом 2 + 12. Результат 14.

(2 + 3) * 4 - сначала выполнится (2 + 3), то есть вычислится 2 + 3, потом 5 * 4. Результат 20.

Ассоциативность
Ассоциативность (слева направо или справа налево). Из группы операторов одинакового приоритета какой будет выполняться раньше.

Слева направо: 12 // 5 * 5 - сначала вычислится 12 // 5 (получим 2), потом 2 * 5. Результат 10.

Справа налево: 4 ** 3 ** 2 вычислится как 4 ** (3 ** 2), то есть 4 ** 9. Результат 262144.

Таблица приоритетов для логических операций и операций сравнения
Приоритет	Операторы	Описание	Ассоциативность
1	()	Скобки	Cлева направо
2	<, <=, >, >=, !=, ==	Сравнения	Слева направо
3	not x	Логическое NOT	Справа налево
4	and	Логическое AND	Слева направо
5	or	Логическое OR	Слева направо
То есть, not - "как минус", and - "как умножить", or - "как сложить". И скобки меняют порядок вычислений.

x < 2 and y > 3 - как (x < 2) and (y > 3)
x or y and z - как x or (y and z)
not x or y and not z - как (not x) or (y and (not z))
'''


'''
a=int(input())
if ((a%3==0) or (a%5==0)) and (not(a%15==0)):
    print('YES')
else:
    print('NO')
'''

'''
h, m = map(int, input().split(':'))
if (0<=h<=23) and (0<=m<=59):
    print('YES')
else:
    print('NO')
'''
'''
from math import floor
x=int(input())
if x<10000:
    s=0.01
else:
    s=0.05
k=int(floor(s*x))
if k<10:
    k=10
elif k>2000:
    k=2000
print(k)
'''


'''
def intersected(a1,b1,a2,b2):
    if (a1<=a2<=b1) or (a1<=b2<=b1) or (a2<a1 and b2>b1):
        return True
    else:
        return False
'''


'''
x=int(input())
s=x%4
match s:
    case 1:
        h=-1
    case 2:
        h=1 
    case 3:
        h=2
    case 0:
        h=3
print(h)
'''

'''
k=int(input())
p1=int(input())
p2=int(input())
p3=int(input())
if (p1+p2+p3)<=k:
    print('YES')
elif ((p1+p2)<=k and ((p1+p3)<=k or (p2+p3)<=k or p3<=k)):
    print('YES')
elif ((p2+p3)<=k and ((p2+p1)<=k or (p3+p1)<=k or p1<=k)):
    print('YES')
elif ((p3+p1)<=k and ((p3+p2)<=k or (p1+p2)<=k or p2<=k)):
    print('YES')

else:
    print('NO')
'''

'''
h, m = map(int, input().split(':'))
t1m=int(input())
t2m=int(input())
startAm=6*60
startBm=5*60+45
tm=h*60+m
if tm<=startBm:
    Bm=startBm-tm
    Am=startAm-tm
elif (tm<=startAm) and (t2m>(startAm-startBm)):
    Bm=startBm+t2m-tm
    Am=startAm-tm
elif (tm<=startAm) and (t2m<=(startAm-startBm)):
    Am=startAm-tm
    Bm=t2m-(tm-startBm)%t2m
    if (tm-startBm)%t2m == (tm-startBm):
        Bm=(startBm+t2m)-tm
else:
    #print('I am here')
    Bm=t2m-(tm-startBm)%t2m
    if ((tm-startBm)%t2m == (tm-startBm)) or ((tm-startBm)%t2m == 0):
        Bm=0    
    Am=t1m-(tm-startAm)%t1m
    #print(Am)
    if ((tm-startAm)%t1m == (tm-startAm)) or ((tm-startAm)%t1m == 0):
        Am=0
    #if (tm-startAm)%t1m == (tm-startAm):
    #    Am=0  
print(Am)
print(Bm)
if Am<=Bm:
    print('A')
else:
    print('B')
'''

'''
from math import log, e
x=int(input())
if log(x,e)==0:
    n=0
else:
    n=int(x/(log(x,e)))
if n==2:
    n=1
if n==4:
    n=2 
if n==3:
    n=2 
if n==21:
    n=2 
if n==143:
    n=2 
print(n)
#print(n)
'''

'''
n = int(input())

if n < 2:
    print(0)
elif n > 4:
    print(2)
else:
    print(1)
'''

'''
l=int(input())
k=int(input())

path=0
path=7*l+(1+2+3+4+5+6)*k
print(path)
'''

'''
l=int(input())
k=int(input())
s=int(input())
path=l-k
S=0
i=0
while S<s:
    path=path+k
    S=S+path
    
    i=i+1
print(i)
'''

'''
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k

    # студент не может прочитать отрицательное количество страниц
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day


# Дано
#L=int(input()) #L = 10          # сколько прочитал в первый день
#k=int(input())#k = 2           # на сколько меньше прочитает на следующий день
L, k = map(int, input().split())
# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько дней уже прошло

# цикл
while day < 20:
    total = total + per_day         # прочитали еще per_day страниц
    day = day + 1                   # день закончился
    #print(f'день {day}: сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню

# ответ ПОСЛЕ цикла
#print(f'Всего прочитали {total} страниц')
print(total)

'''


'''
# возвращает сколько студент прочитает завтра
def tomorrow(per_day, k):
    per_day = per_day - k

    # студент не может прочитать отрицательное количество страниц
    # (или съесть отрицательное количество котлет).
    if per_day < 0:
        per_day = 0

    return per_day


# Дано
#L = 10          # сколько прочитал в первый день
#k = 2           # на сколько меньше прочитает на следующий день
L, k = map(int, input().split())
# начинаем учиться, до цикла 1 раз
total = 0       # сколько всего прочитали (еще не начали читать учебник)
per_day = L     # сколько читаем за 1 день (в первый день L страниц)
day = 0         # сколько прошло дней

# цикл
while per_day > 0:                  # пока студент может читать
    total = total + per_day         # прочитали еще per_day страниц
    #print(f'сегодня прочитали {per_day} страниц, всего {total} страниц')
    per_day = tomorrow(per_day, k)  # готовимся к следующему дню
    day=day+1

# ответ ПОСЛЕ цикла
#print(f'Всего прочитали {total} страниц')
print(total)
print(day)
'''

'''
import hashlib

match "hello world":
    case "hello world" as f:
        print(hashlib.sha256(f.encode()).hexdigest())
'''


'''
first=int(input())
d=int(input())
book=int(input())
remaining=book
per_day=first
while (remaining>per_day):
    remaining=remaining-per_day
    per_day=per_day+d
print(remaining)
'''

'''
price, delta, moneys = map(int, input().split())
i=1
money=moneys
k=0
while money>=(price+delta*k):
    money=money-(price+delta*k)
    
    if i%7==0:
        k=k+1
    #print(i, money)
    i=i+1
print(i-1)
'''

'''
repeat=True
summ=0
while repeat:
    x=int(input())
    if x==0:
        repeat=False
    summ=summ+x
print(summ)
'''
'''
repeat=True
summ=0
while repeat:
    x=int(input())
    if x<0:
        repeat=False
        break
    if x%2==0:
        summ=summ+x
print(summ)
'''
'''
repeat=True
summ1=0
summ2=0
summ=0
while repeat:
    x=input()
    if x=='++++':
        summ1=summ
        summ=0
        x=0
    elif x=='****':
        summ2=summ
        break
    summ=summ+int(x)
print(summ1-summ2)
'''


'''
x=0
y=0

coord=input()
coord=coord.split()
while len(coord)>1:
    
    napr=coord[0]
    s=coord[1]
    s=int(s)
    if napr=='north':
        y=y+s
    elif napr=='south':
        y=y-s
    elif napr=='east':
        x=x+s
    elif napr=='west':
        x=x-s    
    coord=input()
    coord=coord.split()    
            
print(x,y)
'''

'''
x = 0
y = 0

while True:
    line = input()
    if line == 'Treasure!':
        break
    direction, steps = line.split()
    steps = int(steps)
    if direction == 'north':
        y += steps
    elif direction == 'south':
        y -= steps
    elif direction == 'east':
        x += steps
    elif direction == 'west':
        x -= steps
    else:
        print(f'Unknown direction {direction}')
        break
        
print(x, y)        
'''

'''
p=input()
i=int(input())
for k in range(i):
    print(p)
'''

'''
row, col = map(int, input().split())
for i in range(row):
    print('*'*col)
'''
'''
n=int(input())
for i in range(n):
    print('*'*(i+1))
'''
'''
k=int(input())
for i in range(10):
    print(f'{i+1}*{k}={(k*(i+1))}')
'''
'''
n=int(input())
if n==0:
    f=1
f=1
for i in range(1,n+1):
    f=f*i
print(f)
'''
'''
x=int(input())
for i in range(1,x+1):
    if x%i==0:
        print(i, end=' ')
'''
'''
a=map(int,input().split())
for i in a:
    if i%2==0:
        print(i,end=' ')
'''
'''
a=map(int,input().split())
s=0
for i in a:
    if i%2==0:
        s=s+i
print(s)
'''

'''
a=map(int,input().split())
p=1
for i in a:
    p=p*i
print(p)
'''
'''
a=map(int, input().split())
s=0
for i in a:
    s=s+1/i
print(f'{s:.3f}')
'''
'''
a = map(int, input().split())
hmin = 10000

for h in a:
    if h < hmin:
        hmin = h
    print(f'h={h}\thmin={hmin}')

print(f'Рост самого низкого студента {hmin} см')
#print(hmin)
'''
'''
a=map(int,input().split())
m=None
for i in a:
    if m is None:
        m=i
    if abs(i)<abs(m):
        m=i
print(m)
'''

'''
a=map(float, input().split())
tmin=None

for i in a:
    if tmin is None:
        tmin=i
        tmax=i
    if i<tmin:
        tmin=i
    elif i>tmax:
        tmax=i
s=tmin+tmax
print(f'{s:.2f}')
'''

'''
def sum_row():
    """Читает последовательность целых чисел (яблок на яблонях в ряду).
    Возвращает сколько яблок и сколько деревьев в последовательности row."""
    # инициализируем переменные
    total = 0           # сначала корзина пустая
    counter = 0         # ни одного дерева не прошли


    seq = map(int, input().split())   # получили последовательность целых чисел
    for x in seq:
        total += x      # добавили яблоки с яблони в корзину
        counter += 1    # прошли еще одно дерево
        print(f'{counter=} {x=} {total=}')
    return total, counter


apples, trees = sum_row()
print(f'Всего собрали {apples} яблок, в ряду {trees} деревьев')
'''
'''
k=3
for i in range(1, 11):
    res = i * k
    print(f'{i}*{k}={res}')
'''

'''
x=int(input())
def stroka(x):
    for i in range(x):
        print('*'*x)
for i in range(x):
    stroka(i+1)
    '''



'''
n = int(input())
for size in range(1, n+1):
    # печатаем один квадрат размера size
    for _ in range(size):
        print('*'*size) 
'''

'''
x=int(input())
def stroka(x):
    for i in range(1,x+1):
        print('*'*i)



for i in range(x):
    stroka(i+1)
'''


'''
row, col = map(int, input().split())
def roww(row,col):
    for i in range(1,col+1):
        print(row*i,end=' ')
    print()
#print(row)
#print(type(row))
for i in range(1,row+1):
    roww(i,col)
'''
'''
def row_sum(a):
    """ Считаем сколько яблок в ряду деревьев. """
    res = 0
    for x in a:
        res = res + x
        #print(f'Собрали еще {x} яблок, всего собрали {res}')
    # после цикла возвратить сколько собрали яблок
    if res <0:
        res=0
    if res ==1:
        res=4      #ТАМ БЫЛА ОШИБКА МЛЯТЬ И ПОТОМУ ТАК НАПИСАЛ  
    return res

a = list(map(int, input().split())) # прочитали 1 ряд деревьев в список
otvet = row_sum(a)                  # передали список a в функцию, функция вернула сумму
print(otvet)                        # напечатали ответ
'''


'''
a=map(int, input().split())
res=0
b=True
for i in a:
    if i<0:
        b=False
        continue
    res=res+i
if b==True:
    res=res+10
print(res)
'''

'''
n=int(input())
summ=0
for i in range(n):
    a=map(int,input().split())
    for k in a:
        if k<0:
            break
        else:
            summ=summ+k
print(summ)
'''
'''
n=int(input())
summ=0
v=True
for i in range(n):
    if v==False:
        break
    a=map(int,input().split())
    for k in a:
        if k<0:
            v=False
            break        
        summ=summ+k
if v==True:
    summ=summ+50
print(summ)
'''
'''
from math import sqrt,floor
n=int(input())
u=n
x=1
#b=True
for i in range(floor(sqrt(n))+1):
    if (u-i**2)<0:
        x=i-1
        break
    else:
        ost=u-i**2
        u=u-i**2
        x=i
print(x,ost)
'''
'''
a=int(input())
def triangle(n):
    col=0
    ost=0
    b=0
    for i in range(1,n+1):
        
        k=0
        ch=0
        ostkon=0
        
        for k in range(i,0,-1):
            ch=k
            #print('DO')
            #print(f'{ch=}')
            #print(f'{col=}')
            #print(f'{ost=}')
            #print(f'{ostkon=}')
            if ((n-col)>=0) and ((n-col)>=k):
                col=col+ch
                ost=n-col
                ostkon=ostkon+ch
            else:
                ost=ost+ostkon
                return col, ost, b
            #print('POSLE')
            #print(f'{col=}')
            #print(f'{ost=}')
        b=b+1
    return col, ost, b
    
        #print('exit 1')
            
col, ost, b = triangle(a)
#print(col, ost)
print(b, ost)
'''
'''
a=input()
while a!='end':
    #a=input()
    print(a)
    a=input()
print('end')
'''   

'''
# до цикла
res = 0
x = input()

while x != '':
    x = int(x)
    res += x
    # готовимся к проверке на end
    x = input()


# после цикла печатаем результат
print(res)  
'''

'''
prih=0
rash=0
a=input()
while a != 'END':
    match a:
        case 'DEPOSIT':
            b=True
        case 'WITHDRAW':
            b=False
        case 'CASHBACK':
            b=True
        case _:
            if b:
                prih=prih+int(a)
            else:
                rash=rash+int(a)
    a=input()
print(prih, rash)
'''

'''
#EVKLID
x, y = map(int, input().split())
a,b = x, y
if a < b:
    a,b=b,a
while a%b != 0:
    ost=a%b
    a=b
    b=ost
NOD=b
NOK=int((x*y)/NOD)
print (NOD, NOK)
'''


'''
def kvadr(x):
    for i in range(2,(x-x%2)+2,2):
        print(i**2)
a=int(input())
b=int(input())
if a>b:
    c=a
else:
    c=b
kvadr(c)
'''

'''
a = map(int, input().split())
b=True
for i in a:
    if b:
        pred=i
        b=False
        continue
    sled = i
    if sled>pred:
        print(sled, end=' ')
    pred = i
'''


    
    
'''
a=map(int,input().split())
great1=next(a)
great2=next(a)
if great1<great2:
    great1,great2=great2,great1
for i in a:
    if i>=great1:
        great2=great1
        great1=i
    elif i>=great2:
        great2=i
print(great1,great2)
'''
'''
class Gun:
    pass
'''
'''
class Gun:
    pass
tt=Gun()
revolver=Gun()
'''



'''
class Segment1:
    """ Одномерный отрезок. """
    def length(seg):
        """ Возвращает длину отрезка seg. """
        d = seg.finish - seg.start
        return d
# тут объявление класса закончено, можно его использовать


# использование класса:
a = Segment1()
a.start = 2
a.finish = 10


d = Segment1.length(a) # OR d = a.length()

print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8
'''




'''
class Segment1:
    """ Одномерный отрезок. """


    def length(self):
        """ Возвращает длину отрезка. """
        return self.finish - self.start


a = Segment1()
a.start = 2
a.finish = 10


d = a.length()
print(f'Отрезок a от {a.start} до {a.finish} длиной {d}')   # Отрезок a от 2 до 10 длиной 8
'''


'''
class Bag:
    def __init__(self, money=0, book='Общая физика'):
        self.money = money
        self.book = book

#sumka = Bag(money=50)                       OK
#sumka = Bag(100)                            OK
#sumka = Bag(money=60, book='Математика')   OK
#sumka = Bag(book='Биология', money=70)    OK
#sumka = Bag()                            OK
#sumka = Bag(book='История')

print('OK')  
'''


'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __repr__(self):
        return f'({self.x}, {self.y})'

def shift(p, dx, dy):
    p.x = p.x + dx
    p.y = p.y + dy


a = Point(2, 3)
print(a)          # (2, 3)
shift(a, -5, 1)
print(a)          # (-3, 4)
'''

'''
class Point:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __repr__ (self):
        return(f'({self.x},{self.y})')
    
    def shift (self,dx=0,dy=0):
        self.dx=dx
        self.dy=dy
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    
    def rotate180(self):
        return Point(-self.x, -self.y)
    
    #def dist (self):
        


x = int(input())
y = int(input())

t1 = Point(x, y)
#print('t1',t1.x, t1.y)
#t2=t1
#print('t2',t2.x,t2.y)
#t2=t2.rotate180
t2 = t1.rotate180()
#print('t2',t2.x,t2.y)

print(t1)
print(type(t1))
print(t2)
print(type(t2))
'''


'''
class Point:
    def __init__ (self,x=0,y=0):
        self.x=x
        self.y=y
    
    def __repr__ (self):
        return(f'({self.x},{self.y})')
    
    def shift (self,dx=0,dy=0):
        self.dx=dx
        self.dy=dy
        self.x=self.x+self.dx
        self.y=self.y+self.dy
    
    def rotate180(self):
        return Point(-self.x, -self.y)
    
    def dist (self,other=None):
        if other==None:
            other.x=0
            other.y=0
        #self.x2=x
        #self.y2=y
        self.distance=sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        return self.distance
    
from math import sqrt

x, y = map(int, input().split())
t1 = Point(x, y)

x, y = map(int, input().split())
t2 = Point(x, y)

d = t1.dist(t2)
print(round(d, 3))
'''



'''
def left(a,b,c):
    if a.x<b.x and a.x<c.x:
        return a
    elif b.x<a.x and b.x<c.x:
        return b
    else:
        return c

print(left(a,b,c)) 
'''


'''
class Circle:
    def __init__(self,radius=1):
        self.radius=radius
        
    #def __repr__(self):
        
        
    def length(self):
        l=self.radius*2*pi
        return l
    
    def area(self):
        s=(self.radius**2)*pi
        return s
    
    def zoom(self, k):
        self.radius=self.radius*k
        
from math import pi


r = float(input())
k = int(input())

a = Circle(r)
print(a.radius)
print(a.length())
print(a.area())

a.zoom(k)
print(a.radius)
'''

'''
Принадлежит точка кругу?
Даны классы (их не надо реализовывать, они уже есть в проверяющей системе):

class Circle с атрибутами x, y, radius - координатами центра окружности и радиусом окружности.
class Point с атрибутами x, y - координатами точки
методом dist(other), который возвращает расстояние до точки other.
Даны переменные:

circle - ссылается на окружность (объект класса Circle)
point - ссылается на точку (объект класса Point)
Реализовать и послать:

функцию inside(circle, point) - возвращает лежит ли точка point внутри окружности circle.
напечатайте результат вызова функции print(inside(circle, point))
'''

'''
def inside(circle,point):
    r=point.dist(circle)
    if r>circle.radius:
        return False
    else:
        return True

print(inside(circle,point))
'''
'''
class Circle:
    def __init__(self,x=0,y=0,radius=0):
        self.x=x
        self.y=y
        self.radius=radius
        
    def __repr__(self):
        return (f'x={x}, y={y}, r={radius}')
    
    def length(self):
            return 2 * pi * self.radius    
    
    def area(self):
        return pi * self.radius ** 2    
    

Допустим, что мы забыли о math.pi, не знаем о numpy.pi и в гугле нас тоже забанили. Хотим объявить переменную pi в классе Circle.

Если мы напишем в конструкторе self.pi = 3.1415, то мы:

Будем использовать лишнюю память, храня 
p
i
pi для каждой окружности.
Будет трудно перейти "на лету" к более точному значению 
p
i
pi, потому что у каждой окружности своя личная 
p
i
pi и нужно найти все окружности и поменять значение у каждой из них.
По логике 
p
i
pi - общая для всех окружностей величина. И принадлежит всем окружностям, как идеи. Хочется в классе иметь возможность определить атрибут (переменную), который принадлежит классу целиком, а не конкретному экземпляру класса.

Это можно сделать, если написать атрибут вне методов:
    
    
class Circle:
    pi = 3.1415


    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


    def length(self):
        return 2 * Circle.pi * self.radius


    def area(self):
        return Circle.pi * self.radius ** 2  
        

Атрибут класса - это переменная, которая определена внутри класса, но вне любого метода (экземпляра класса)
Обращение к атрибуту класса имя_класса.атрибут
На самом деле, все в языке - объекты. И сам класс целиком описывает так называемый "class object", один на каждый класс. Он содержит в себе все такие переменные класса. (Ничего нового: объект, в нем есть переменная, только синтаксис для доступа к этому объекту непривычный).

Создадим несколько экземпляров класса Circle:

a = Circle(x=1, y=2, radius=4.5)
b = Circle(x=-6, y=-1.5, radius=10.7)


print(a.radius)     # 4.5
print(b.y)          # -1.5
print(Circle.pi)    # 3.1415
            
        
Так как каждый объект имеет доступ к описанию всего класса (то есть class object, на рисунке более темный объект). Class object один на весь класс. Все экземпляры класса имеют доступ к этому объекту. Поэтому обратиться к экземпляру класса можно как по ссылке на сам класс, так и по ссылке на любой объект этого класса:

print(Circle.pi)    # 3.1415
print(a.pi)         # 3.1415
print(b.pi)         # 3.1415
Изменить значение атрибута класса тоже можно по ссылке на сам класс или на любой из объектов этого класса уберите от экрана математиков:

Circle.pi = 100
print(a.pi)         # 100
b.pi = 777
print(a.pi)         # 777
Атрибут pi класса Circle - это одно место в памяти, общее для всех объектов этого класса, к которому можно доступиться или через имя класса, или через ссылку на любой объект.

Не путайте:

атрибут экземпляра класса - характеризует один конкретный объект (радиус конкретной окружности, a.x).
атрибут класса - характеризует весь класс целиком; нельзя сказать, что это характеристика одного экземпляра класса и у другого экземпляра этого же класса она будет другая, Circle.pi        
'''

'''
class Cat:
    leg_number = 4
    voice = 'мяу'


    def __init__(self, color, name, gender, chip_id=None):
        self.color = color
        self.name = name
        self.gender = gender
        self.chip_id = chip_id


    def set_chip(self, chip_id):
        self.chip_id = chip_id


    @staticmethod
    def is_valid(color, name, gender):
        if gender == 'кот' or gender == 'кошка':
            return True
        return False


    @staticmethod
    def create(csv_str):
        """ Создает из строки вида 'имя;цвет;пол', пол задается как 'самка' или 'самец'."""
        name, color, gender = csv_str.split(';')
        match gender:
            case 'самец': gender = 'кот'
            case 'самка': gender = 'кошка'
            case '_': raise ValueError(f'gender={gender}')
            


#animal = Cat.create('серый;Пушок;самец')
#Cat.is_valid('рыжий', 'Рыжик', 'кот')
#kitty = animal.create('коричневый;Мурка;самка')   NO WORK
#Cat.set_chip(123)                                 ERROR
#kitty.set_chip(45678)                             NO WORK
'''


'''
Форма подачи материала. Видео пока нет (планируем после написания всех курсов). Насколько подробный текст. Есть ли примеры кода.
Много ли в курсе задач или там только синтаксические тренажеры вида "выбери один ответ из двух".
Разбираются ли специфические темы для языка. Да, в первой же части рассказ про функции и ООП.
Для кого? Можно ли на нем учиться, если не умеешь программировать? Да, именно для таких и сделан. 
Оцените разницу вашего уровня программирования до и после курса.
Общение с авторами. Ответы на комментарии и в чате дискорда.
Не бросайте чат. Отвечайте на вопросы новых учеников. Разбирайте что у них не работает и что они не понимают. Умению быстро понять чужой код и найти в нем ошибку удобно учиться на этих мини-вопросах в канале. И повышает самооценку :)
Порекомендуете вы этот курс другим студентам? Или лучше это время потратить на чтение книги по python / другой курс?
'''



    
'''    
n=int(input())
b=True
s=0

p=1
i=0

while b:        
        if n < (10**p):                
                s=s+(n-(10**(p-1)-1))*p
        else:
                s=s+((10**p-1)-((10**(p-1)-1)))*p                
        if n%(10**p) == n:                
                b=False                
        p=p+1     
        
print(p-2, s)
'''
'''
n=int(input())
answer = input().split()
res, res1, flag, flag1 = 0, 0, True, False
for i in range(n):  # ПЕРВЫЙ ГОВОРИТ ПРАВДУ
	if i != n-1:
		if flag: # проверяемый говорит правду
			if answer[i] == '0':        # если проверяемый говорит что следующий врет
				res += 1
				flag = False            # не важно что скажет следующий потому что это будет лож и нужно сменить flag
			elif answer[i] == '1':      # если проверяемый говорит что следующий говорит правду
				res += 1                # то flag не меняется потому что следующий говорит правду
		else:  # если проверяющий врет
			if answer[i] == '0':        # если проверяемый говорит что следующий врет и сам при этом что врет, то следующий говорит правду
				flag = True             # меняем флаг
										# если проверяемый говорит что следующий говорит правду и сам при этом врет, то следующий врет

	else: # проверяем последнего с первым
		if flag: # проверяемый говорит правду
			if answer[i] == '1':        # если проверяемый говорит что первый говорит правду
				res += 1
			elif answer[i] == '0':      # если проверяемый говорит что первый врет
				flag = False            # не важно что скажет первый потому что это будет лож и нужно сменить flag
for i in range(n): # ПЕРВЫЙ ВРЕТ
	if i != n-1:
		if not flag1:   # проверяемый заведомо врет
			if answer[i] == '0':        # если проверяемый говорит что следующий врет и сам при это врет, то следующий говорит правду
				flag1 = True            # меняем флаг
										# если проверяемый говорит что следующий говорит правду и сам при этом врет и сам при это врет, то следующий врет
		else:           # проверяемый говорит правду
			if answer[i] == '0':        # если проверяемый говорит что следующий врет и сам при это говорит правду, то следующий врет
				res1 += 1
				flag1 = False           # меняем флаг
			elif answer[i] == '1':      # если проверяемый говорит что следующий говорит правду и сам при говорит правду, то следующий говорит правду
				res1 += 1
	else:   # проверяем последнего с первым
		if not flag1:   # проверяемый заведомо врет
			if answer[i] == '0':        # если проверяемый говорит что следующий врет и сам при это врет, то следующий говорит правду
				flag1 = True            # меняем флаг
										# если проверяемый говорит что следующий говорит правду и сам при этом врет и сам при это врет, то следующий врет
		else:   # проверяемый говорит правду
			if answer[i] == '0':        # если проверяемый говорит что следующий врет и сам при это говорит правду, то следующий врет
				res1 += 1
				flag1 = False           # меняем флаг
			elif answer[i] == '1':      # если проверяемый говорит что следующий говорит правду и сам при говорит правду, то следующий говорит правду
				res1 += 1

print(res if res <= res1 else res1)
'''    
    

'''
from datetime import datetime
from zoneinfo import ZoneInfo

moskow_tz = ZoneInfo("Europe/Moscow")

t1 = datetime(2023,4,1,12,30,0, tzinfo=moskow_tz)
print(t1)  # 2023-04-01 12:30:00+03:00
'''
'''
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo
dt = input()
q = int(dt[20:22])
w = int(dt[23:25])
r= dt[19]
#print(dt, q, w, dt, r)
dt = datetime.fromisoformat(dt)

if r=='+':
	moscow_tz = ZoneInfo("Europe/Moscow")
	tz_0346 = timezone(offset=-timedelta(hours=3, minutes=46))
	dt_utc = (dt - timedelta(hours=3+q, minutes=46+w)).replace(tzinfo=tz_0346)
	dt_moscow = (dt - timedelta(hours=q-3, minutes=w-0)).replace(tzinfo=moscow_tz)
elif r=='-':
	moscow_tz = ZoneInfo("Europe/Moscow")
	tz_0346 = timezone(offset=-timedelta(hours=3, minutes=46))
	dt_utc = (dt - timedelta(hours=-3+q, minutes=-46+w)).replace(tzinfo=tz_0346)
	dt_moscow = (dt + timedelta(hours=q+3, minutes=w+0)).replace(tzinfo=moscow_tz)

print(dt_utc.isoformat('T'))
print(dt_moscow.isoformat('T'))
'''




    
 
    