import tkinter as tk
from tkinter import font


def get_numbers():
    if number1_entry.get() == '':
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, 'Введите первое число')
        return None

    if number2_entry.get() == '':
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, 'Введите второе число')
        return None

    try:
        num1_str = number1_entry.get().replace(',', '.')
        num2_str = number2_entry.get().replace(',', '.')
        num1 = float(num1_str)
        num2 = float(num2_str)
        return num1, num2
    except ValueError:
        answer_entry.delete(0, tk.END)
        answer_entry.insert(0, 'Вводить можно только числа')
        return None


def get_result(result):
    if str(result).endswith('.0'):
        result = str(int(result))

    answer_entry.delete(0, tk.END)
    answer_entry.insert(0, result)


def clear_all():
    for each_entry in entries:
        each_entry.delete(0, tk.END)


def add():
    num1, num2 = get_numbers()

    if num1 is not None and num2 is not None:
        result = num1 + num2
        get_result(result)


def subtract():
    num1, num2 = get_numbers()
    if num1 is not None and num2 is not None:
        result = num1 - num2
        get_result(result)


def multiply():
    num1, num2 = get_numbers()

    if num1 is not None and num2 is not None:
        result = num1 * num2
        get_result(result)


def divide():
    num1, num2 = get_numbers()

    if num1 is not None and num2 is not None:
        if num2 == 0:
            answer_entry.delete(0, tk.END)
            answer_entry.insert(0, 'На 0 делить нельзя')
        else:
            result = num1 / num2
            get_result(result)


def backspace():
    current_entry = window.focus_get()
    if current_entry:
        current_entry.delete(len(current_entry.get()) - 1, tk.END)


window = tk.Tk()
window.title('Калькулятор')
window.geometry('400x400')
window.resizable(False, False)

number1_text = tk.Label(window, text='Введите первое число:')
number1_text.place(x=60, y=50)
number1_entry = tk.Entry(window)
number1_entry.place(x=60, y=70)

number2_text = tk.Label(window, text='Введите второе число:')
number2_text.place(x=60, y=110)
number2_entry = tk.Entry(window)
number2_entry.place(x=60, y=130)

answer_text = tk.Label(window, text='Результат вычисления:')
answer_text.place(x=60, y=180)
answer_entry = tk.Entry(window)
answer_entry.place(x=60, y=200)

texts = [number1_text, number2_text, answer_text]

for text in texts:
    text.config(font=("Roboto", 10, 'bold'), fg='#FF4500')

entries = [number1_entry, number2_entry, answer_entry]

for entry in entries:
    entry.config(width=46, borderwidth=2)

button_reset = tk.Button(window, text='C', command=clear_all)
button_reset.place(x=60, y=280)
button_add = tk.Button(window, text='+', command=add)
button_add.place(x=110, y=280)
button_sub = tk.Button(window, text='-', command=subtract)
button_sub.place(x=160, y=280)
button_mul = tk.Button(window, text='*', command=multiply)
button_mul.place(x=210, y=280)
button_div = tk.Button(window, text='/', command=divide)
button_div.place(x=260, y=280)
button_backspace = tk.Button(window, text='⌫', command=backspace)
button_backspace.place(x=310, y=280)

buttons = [
    button_reset,
    button_add,
    button_sub,
    button_mul,
    button_div,
    button_backspace,
]

bold_font = font.Font(family='Arial', weight='bold')

for button in buttons:
    button.config(font=bold_font, bg='#FF7F50', fg='white', width=2, height=1)


window.mainloop()
