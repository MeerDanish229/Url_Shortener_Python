import pyshorteners
import tkinter as tk
from tkinter import *

def generate_short_url(parm):
    parm = url_entry.get()
    # short_url_entry.config(state='normal',bg='light blue')
    if parm == "":
         short_url_entry.delete(0, END) 
         short_url_entry.insert(END,"Please Enter Url")
         short_url_entry.config(bg='light blue')     
         short_url_entry.config(state='readonly') 
    else:
         short_url = pyshorteners.Shortener().tinyurl.short(parm)
        #  short_url_entry.config(state='normal')    
         short_url_entry.delete(0, END) 
         short_url_entry.insert(END,short_url)
         url_entry.delete(0,END)
        #  short_url_entry.config(bg='light pink') 
    # short_url_entry.config(state='readonly')
         
    # short_url = pyshorteners.Shortener().tinyurl.short(parm)
    # short_url_entry.delete(0, END) 
    # short_url_entry.insert(END,short_url)

def output_window_center(parm):
    parm.update_idletasks()
    width = parm.winfo_width()
    height = parm.winfo_height()
    x = (parm.winfo_screenwidth() // 2) - (width // 2)
    y = (parm.winfo_screenheight() // 2) - (height //2)
    parm.geometry("{}x{}+{}+{}".format(width,height,x,y))


root = tk.Tk()
root.title("Codexcue Url Shortner")
root.configure(bg="light blue")
root.geometry('600x500')
root.resizable(False,False)
output_window_center(root)

tk.Label(root,text="Enter Url :",font=('impact',20,'italic'),bg='light blue').pack(pady=10)
url_entry = tk.Entry(root,width=100,font=('Ariel 18 bold'))
url_entry.pack(padx=10)
url_btn =tk.Button(root,text="Generate Short Url" ,font=('Sans 16 bold'),command=lambda:generate_short_url(url_entry)).pack(pady=5)
short_url_entry = tk.Entry(root, width=80, font=('Ariel 16 italic'), bd=0, bg='light blue', foreground='black')
short_url_entry.pack(pady=20, padx=20)
# short_url_entry.config(background='light blue',state='readonly')
root.mainloop()
