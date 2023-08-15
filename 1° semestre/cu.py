import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Modelagem')
window.geometry('250x300')




vari = tk.StringVar(value='Insira seu nome')

entry1 = ttk.Entry(master=window, textvariable=vari)
entry1.pack()



button = ttk.Button(master=window, text='Buceta')
button.pack()




window.mainloop()