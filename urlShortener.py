import pyshorteners
import tkinter as tk

def generate_short_url():
    url = url_entry.get()
    if url == "":
        short_url_label.config(text="Please Enter Url", bg='light pink')
    else:
        try:
            url_entry.delete(0, tk.END)
            short_url = pyshorteners.Shortener().tinyurl.short(url)
            short_url_label.config(text=short_url, bg='light blue')
        except Exception as e:
            short_url_label.config(text="Error: Invalid URL", bg='light pink')

def copy_to_clipboard():
    short_url = short_url_label.cget("text")
    if short_url and "http" in short_url: 
        root.clipboard_clear()
        root.clipboard_append(short_url)
        root.update()  
        copy_label.config(text="Copied!", bg='light green')
    else:
        copy_label.config(text="Nothing to copy", bg='light pink')            

def output_window_center(parm):
    parm.update_idletasks()
    width = parm.winfo_width()
    height = parm.winfo_height()
    x = (parm.winfo_screenwidth() // 2) - (width // 2)
    y = (parm.winfo_screenheight() // 2) - (height //2)
    parm.geometry("{}x{}+{}+{}".format(width, height, x, y))

root = tk.Tk()
root.title("Codexcue Url Shortener")
root.configure(bg="light blue")
root.geometry('600x500')
root.resizable(False, False)
output_window_center(root)

tk.Label(root, text="Enter Url:", font=('impact', 20, 'italic'), bg='light blue').pack(pady=10)
url_entry = tk.Entry(root, width=100, font=('Ariel 18 bold'))
url_entry.pack(padx=10)

url_btn = tk.Button(root, text="Generate Short Url", font=('Sans 16 bold'), command=generate_short_url)
url_btn.pack(pady=5)

short_url_label = tk.Label(root, text="", font=('Ariel 16 italic'), bg='light blue', foreground='black', wraplength=500)
short_url_label.pack(pady=20, padx=20)

copy_button = tk.Button(root, text="Copy URL", command=copy_to_clipboard)
copy_button.pack(pady=5)

copy_label = tk.Label(root, text="", width=50, height=2, bg='light grey')
copy_label.pack(pady=10)

root.mainloop()
