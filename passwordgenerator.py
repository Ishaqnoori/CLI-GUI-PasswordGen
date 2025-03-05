import random
import datetime
import os
import ctypes
from tkinter import *

# Function to generate a simple password
def simple(n):
    password = ''.join(random.choice(upper + lower + num) for _ in range(n))
    return password

# Function to generate a complex password
def hard(n):
    password = ''.join(random.choice(allchar) for _ in range(n))
    return password

# Function to handle CLI version
def cli_mode():
    os.system("title Secure Password Generator")
    os.system('color 0a')

    d_date = datetime.datetime.now()
    reg_format_date = d_date.strftime("  %d-%m-%Y\t\t\t\t\t  Secure Password Generator\t\t\t\t  %I:%M:%S %p")
    
    print('+' * 120)
    print(reg_format_date)
    print('+' * 120)

    n = int(input('\nEnter length of your password: '))
    z = int(input('Press 1 for simple password\nPress 2 for complex password\n> '))

    if z == 1:
        password = simple(n)
    elif z == 2:
        password = hard(n)
    else:
        print('Wrong input')
        return

    print(f'Your generated password is:\n{password}')

    filename = input('\nEnter filename to save it: ')
    with open(filename + '.txt', 'w') as f:
        f.write('Your generated password is:\n\n' + password)

    ctypes.windll.user32.MessageBoxW(0, f"Your generated password is saved in {filename}.txt", "Message", 0)

# Function to handle GUI version
def gui_mode():
    obj = Tk()
    obj.title("Secure Password Generator")
    obj.geometry("600x400")

    def generate_password(mode):
        try:
            n = int(entry_length.get("1.0", 'end-1c'))
            if mode == "simple":
                password = simple(n)
            else:
                password = hard(n)
            output_text.delete('1.0', END)
            output_text.insert(END, password)
        except ValueError:
            output_text.delete('1.0', END)
            output_text.insert(END, "Enter a valid number!")

    Label(obj, text="Enter Length:").pack(pady=10)
    entry_length = Text(obj, height=1, width=10)
    entry_length.pack()

    Button(obj, text="Simple", command=lambda: generate_password("simple")).pack(pady=5)
    Button(obj, text="Complex", command=lambda: generate_password("complex")).pack(pady=5)

    output_text = Text(obj, width=50, height=5)
    output_text.pack(pady=10)

    obj.mainloop()

# Character sets
num = '1234567890'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
specialchar = '`~!@#$%^&*()_+-=[]{}|/;:,<.>?'
allchar = upper + lower + num + specialchar

# Ask the user which mode they want to run
mode = input("Choose mode: (1) CLI (2) GUI\n> ")

if mode == "1":
    cli_mode()
elif mode == "2":
    gui_mode()
else:
    print("Invalid input! Please restart and choose 1 or 2.")
