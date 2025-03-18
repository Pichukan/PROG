'''
x=input()
y=input()
s=int((float(x)*60+int(y))*9)
print(s)
'''

'''
x=int(input())
print(int(x//60))
print(int(x%60))
'''

'''
import tkinter

window = tkinter.Tk()
window.geometry('400x400')
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Hello World!").pack()
window.mainloop()
'''

from tkinter import *
window = Tk()
window.title("Desktop Application for IT club in the 359 lab")
text1 = Label(window, text = "Hello, Brogrammers and Prosisters! This our first program, so be sure that we can accomplish this year without any doubts!")
text1.pack()
window.mainloop()