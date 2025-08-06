import os

user = os.getlogin()

path_dict = {
    'Downloads': rf"C:\Users\{user}\Downloads",
    'Documents1': rf"C:\Users\{user}\Documents",
    'Documents2': rf"C:\Users\{user}\OneDrive\Documents"
}