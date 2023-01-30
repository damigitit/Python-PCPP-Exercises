import tkinter as tk
from tkinter import *
from tkinter import messagebox



def calc():
    try:
        result = ''
        if radio_var.get() == 1:
            result = float(entry_1.get()) + float(entry_2.get())
        elif radio_var.get() == 2:
            result = float(entry_1.get()) - float(entry_2.get())
        elif radio_var.get() == 3:
            result = float(entry_1.get()) * float(entry_2.get())
        elif radio_var.get() == 4:
            result = float(entry_1.get()) / float(entry_2.get())
        else:
            pass
            
        messagebox.showinfo(title="results", message = str(result))
    except ZeroDivisionError as e:
        messagebox.showinfo(title="division by zero", message="cannot divide by zero")
    except ValueError as e:
        messagebox.showinfo(title="entry error", message="numeric values only please:\n" + str(e)) 
        
            

                    
        
master = Tk()
master.title("Simple Calculator")

text_1 = StringVar()
text_2 = StringVar()

entry_1 = Entry(master, textvariable=text_1)
entry_2 = Entry(master, textvariable=text_2)

frame = Frame(master)

radio_var = IntVar()
radio_add = Radiobutton(master, text="+", variable=radio_var, value=1)
radio_sub = Radiobutton(master, text="-", variable=radio_var, value=2)
radio_mul = Radiobutton(master, text="*", variable=radio_var, value=3)
radio_div = Radiobutton(master, text="/", variable=radio_var, value=4)
radio_var.set(1)

entry_1.grid(row=2, column=0, sticky=W, pady=2)

radio_add.grid(row=0, column=1, pady=2)
radio_sub.grid(row=1, column=1, pady=2)
radio_mul.grid(row=2, column=1, pady=2)
radio_div.grid(row=3, column=1, pady=2)

entry_2.grid(row=2, column=2, sticky=E, pady=2)

calc_button = Button(master, text="Evaluate", command=calc)
calc_button.grid(row=4, column=1, columnspan=2, sticky=W)

if __name__ == '__main__':
    master.mainloop()
