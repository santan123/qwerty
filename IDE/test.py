# First five line we have gotten a simple editor
from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
IDE = Tk()
# Adding of title to the IDE
IDE.title('Group 2 IDE')
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python{file_path}'
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


menu_bar = Menu(IDE)

file_menu = Menu(menu_bar, tearoff=0)  # Remove all the unnecessary dashes
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)
IDE.config(menu=menu_bar)


run_bar = Menu(menu_bar, tearoff=0)  # Remove all the unnecessary dashes
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)


editor = Text()
editor.pack()
code_output = Text(height=5)
code_output.pack()
IDE.mainloop()
