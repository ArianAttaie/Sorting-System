import os
import tkinter as tk
from tkinter import ttk

from alg import Sorting_System
from dict import system_path_dict as spd



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
    path_label.config(text="Set folder: " + selected_item)

def store_path(path):
    memory = open(rf"{os.path.dirname(__file__)}\dict\path_memory.txt", 'r')
    memory_items = memory.read().split(',')
    memory.close()

    if path not in memory_items:
        if path not in list(spd.path_dict.values()):
            memory2 = open(rf"{os.path.dirname(__file__)}\dict\path_memory.txt", 'a')
            memory2.write(f",{path}")
            memory2.close()  
    
def sorting_task():
    path = path_combo_box.get()

    # Check if the directory does exist
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

    # Check if the system does exists
    elif os.path.isdir(path) == True:
        if system_var.get() == False:
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
            # Run the alg if everything was OK
            Sorting_System.directory_path = path_combo_box.get()
            Sorting_System.sort_files()
            store_path(path_combo_box.get())

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

path_list = [spd.path_dict['Downloads'], spd.path_dict['Documents1'], spd.path_dict['Documents2']]
memory = open(rf"{os.path.dirname(__file__)}\dict\path_memory.txt", 'r')
memory_list = memory.read().split(',')
memory_list.remove('')
if len(memory_list) != 0:
    path_list += memory_list
memory.close()
path_combo_box = ttk.Combobox(root, values=path_list, width=35)
path_combo_box.pack(pady=5)
path_combo_box.bind("<<ComboboxSelected>>", select_path)


system_label = tk.Label(root, text="Choose the sorting system: ")
system_label.pack(pady=5)
system_var = tk.BooleanVar()
tk.Radiobutton(root, text='File format', variable=system_var, value=True).pack(pady=5)


button = tk.Button(root, text="Sort", width=25, command=sorting_task).pack(pady=15)


root.mainloop()