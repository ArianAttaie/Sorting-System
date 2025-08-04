import os
from alg import Sorting_System
import tkinter as tk
from tkinter import ttk

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def select_path(event):
    selected_item = path_combo_box.get()
    path_label.config(text="Selected folder: " + selected_item)

def select_format(event):
    selected_item = format_combo_box.get()
    format_label.config(text="Selected sorting system: " + selected_item)

def sort_task():
    path = path_combo_box.get()
    formatting = format_combo_box.get()
    counter = 0
    for i in format_list:
        if i == formatting:
            counter+=1

    if os.path.isdir(path) == False:
        top = tk.Toplevel()
        top.title('Task Report')
        top.iconbitmap('SortingSystem.ico')
        top.geometry("150x100")
        top.resizable(False, False)
        top.attributes('-alpha', 0.0)
        center(top)
        top.attributes('-alpha', 1.0)
        label = tk.Label(top, text="Directory was not found!")
        label.pack(pady=10)
        button = tk.Button(top, text="OK", command=top.destroy)
        button.pack(pady=10)
        top.mainloop()

    elif os.path.isdir(path) == True:
        if counter == 0:
            top = tk.Toplevel()
            top.title('Task Report')
            top.iconbitmap('SortingSystem.ico')
            top.geometry("300x100")
            top.resizable(False, False)
            top.attributes('-alpha', 0.0)
            center(top)
            top.attributes('-alpha', 1.0)
            label = tk.Label(top, text="You have to choose a valid sorting system.")
            label.pack(pady=10)
            button = tk.Button(top, text="OK", command=top.destroy)
            button.pack(pady=10)
            top.mainloop()

        else:
            Sorting_System.path = path_combo_box.get()
            Sorting_System.sort_files()
            print(Sorting_System.path)

            top = tk.Toplevel()
            top.title('Task Report')
            top.iconbitmap('SortingSystem.ico')
            top.geometry("150x100")
            top.resizable(False, False)
            top.attributes('-alpha', 0.0)
            center(top)
            top.attributes('-alpha', 1.0)
            label = tk.Label(top, text="Task compeleted!")
            label.pack(pady=10)
            button = tk.Button(top, text="OK", command=top.destroy)
            button.pack(pady=10)
            top.mainloop()

        


format_list = ["file format"]

root = tk.Tk()
root.title("Sorting System")
root.iconbitmap('SortingSystem.ico')
root.geometry("500x200")
root.resizable(False, False)
root.attributes('-alpha', 0.0)
center(root)
root.attributes('-alpha', 1.0)


path_label = tk.Label(root, text="Choose your folder: ")
path_label.pack(pady=10)
path_combo_box = ttk.Combobox(root, values=[rf"C:\Users\{os.getlogin()}\Downloads",
                                             rf"C:\Users\{os.getlogin()}\Documents",
                                               rf"C:\Users\{os.getlogin()}\OneDrive\Documents"], width=35)
path_combo_box.pack(pady=5)

format_label = tk.Label(root, text="Choose the sorting system: ")
format_label.pack(pady=10)
format_combo_box = ttk.Combobox(root, values=format_list, width=35)
format_combo_box.pack(pady=5)

path_combo_box.bind("<<ComboboxSelected>>", select_path)
format_combo_box.bind("<<ComboboxSelected>>", select_format)

button = tk.Button(root, text="Sort", width=25, command=sort_task).pack(pady=15)


root.mainloop()