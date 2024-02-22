import tkinter as tk

#FRESHGUI MODULE VERSION 0.2.1

dict = {}

def create(name='FreshGUI Window', size='400x300', icon='', resizable='True'):
    global root

    root = tk.Tk()
    root.title(name)
    root.geometry(size)
    root.resizable(width=resizable, height=resizable)
    root.iconbitmap(icon)
    root.configure(background=themeBG)

def theme(theme='Light'):
    global themeBG

    if theme == 'Dark':
        themeBG = '#1F1F1F'
    elif theme == 'Light':
        themeBG = '#EEEEEE'

def text(name='textVariable', text='Text'):
    dict[name] = tk.Label(root, text=text)
    dict[name].pack()

def textUpdate(name='textVariable', text='Text'):
    dict[name].config(text=text)

def button(name='buttonVariable', text='Button', command='', cursor='hand2'):
    dict[name] = tk.Button(root, text=text, command=command)
    dict[name].pack()
    dict[name].configure(cursor=cursor)

def run():
    root.mainloop()
