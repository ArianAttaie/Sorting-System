import os
import logging

logging.basicConfig(filename = "Sorting.log", level = logging.INFO , format = '%(filename)s , %(asctime)s , %(levelname)s , %(message)s')
user = os.getlogin()
directory_path = str()

def get_list(path):
    files = os.listdir(path)
    return files

def sort_files():
    my_files = get_list(directory_path)

    for i in my_files:
        isdir = os.path.isdir(rf"{directory_path}\{i}")

        if isdir == True:
            continue

        elif isdir == False:
            splited = i.split('.')

            # skipping 'ini' files:
            if splited[-1] == 'ini':
                continue

            # sorting system:
            elif len(splited) > 1:

                # Making directory if it doesn't exist
                os.makedirs(rf'{directory_path}\{splited[-1]}_format', exist_ok=True)

                # Check if the file already exists in the directory or not
                if os.path.exists(rf'{directory_path}\{splited[-1]}_format\{i}') == False:

                    # Moveing the file
                    os.rename(rf'{directory_path}\{i}' , rf'{directory_path}\{splited[-1]}_format\{i}')
                    logging.info(f'MOVED , file \"{i}\" moved to \"{splited[-1]}_format\" folder ')

                else:
                    logging.info(f'EXIST , file \"{i}\" already exists in \"{splited[-1]}_format\" folder ')