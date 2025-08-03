from alg import Sorting_System
import tkinter as tk
from tkinter import ttk

user = Sorting_System.get_user()

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
    format_label.config(text="Selected format: " + selected_item)


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
path_combo_box = ttk.Combobox(root, values=[rf"C:\Users\{user}\Downloads", rf"C:\Users\{user}\Documents"])
path_combo_box.pack(pady=5)

format_label = tk.Label(root, text="Choose the sorting system: ")
format_label.pack(pady=10)
format_combo_box = ttk.Combobox(root, values=["file format"])
format_combo_box.pack(pady=5)


path_combo_box.set(rf"C:\Users\{user}\Downloads")
format_combo_box.set("file format")
path_combo_box.bind("<<ComboboxSelected>>", select_path)
format_combo_box.bind("<<ComboboxSelected>>", select_format)

files_path = path_combo_box.get()
button = tk.Button(root, text="Sort", width=25, command=Sorting_System.sort_files(files_path=files_path, user=user)).pack(pady=15)


root.mainloop()