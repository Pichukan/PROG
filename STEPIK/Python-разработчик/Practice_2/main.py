'''
# -*- coding: utf-8 -*-
from collections import Counter

with open('file.txt', mode='r', encoding='utf-8') as f:
	a=f.read()

text=a.replace('\n',' ').replace(',',' ').replace('.',' ').split()

text_count=Counter(text)

big=text_count.most_common(1)

word = big[0][0]
#print(word)

word_count = big[0][1]
#print(word_count)
'''

with open('file.txt', mode='x', encoding='utf-8') as f:
	a=f.read()
