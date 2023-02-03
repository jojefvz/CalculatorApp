from tkinter import *

root = Tk()
root.title('Simple Calculator')

e = Entry(root, width=35, borderwidth=5)
# e.pack()
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))
    return

def erase():
    e.delete(0, END)

def equals():
    num2 = e.get()
    e.delete(0, END)
    if sign == '+':
        e.insert(0, first_num + int(num2))
    if sign == '-':
        e.insert(0, first_num - int(num2))
    if sign == 'x':
        e.insert(0, first_num * int(num2))
    if sign == '/':
        e.insert(0, first_num / int(num2))


def add():
    num1 = e.get()
    global first_num
    global sign
    first_num = int(num1)
    sign = '+'
    e.delete(0, END)

def subtract():
    num1 = e.get()
    global first_num
    global sign
    first_num = int(num1)
    sign = '-'
    e.delete(0, END)

def multiply():
    num1 = e.get()
    global first_num
    global sign
    first_num = int(num1)
    sign = 'x'
    e.delete(0, END)

def divide():
    num1 = e.get()
    global first_num
    global sign
    first_num = int(num1)
    sign = '/'
    e.delete(0, END)

#Define buttons
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))

button_equals = Button(root, text='=', padx=40, pady=20, command=equals)
button_clear = Button(root, text='Clear', padx=151, pady=20, command= erase)

button_add = Button(root, text='+', padx=40, pady=20, command=add)
button_subtract = Button(root, text='-', padx=40, pady=20, command=subtract)
button_multiply = Button(root, text='x', padx=40, pady=20, command=multiply)
button_divide = Button(root, text='/', padx=40, pady=20, command=divide)


#Place butttons
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_equals.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)

button_add.grid(row=4, column=1)
button_subtract.grid(row=4, column=2)
button_multiply.grid(row=5, column=0)
button_divide.grid(row=5, column=1)


root.mainloop()