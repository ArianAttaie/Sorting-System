import os
import logging

logging.basicConfig(filename = "Sorting.log", level = logging.INFO , format = '%(filename)s , %(asctime)s , %(levelname)s , %(message)s')

def get_user():
    user = os.getlogin()
    return user

def sorting_files(files_path, user):
    for i in files_path:

        if os.path.isdir(i) == False:

            splited = i.split('.')

            # skipping 'ini' files:
            if splited[-1] == 'ini':
                continue

            # sorting system:
            elif len(splited) > 1:

                # Making directory if it doesn't exist
                os.makedirs(rf'C:\Users\{user}\Downloads\{splited[-1]}_format', exist_ok=True)

                # Check if the file already exists in the directory or not
                if os.path.exists(rf'C:\Users\{user}\Downloads\{splited[-1]}_format\{i}') == False:
                    
                    # Moveing the file
                    os.rename(rf'C:\Users\{user}\Downloads\{i}' , rf'C:\Users\{user}\Downloads\{splited[-1]}_format\{i}')
                    logging.info(f'MOVED , file \"{i}\" moved to \"{splited[-1]}_format\" folder ')

                else:
                    logging.info(f'EXIST , file \"{i}\" already exists in \"{splited[-1]}_format\" folder ')
                    continue

            else:
                continue

        else:
            continue

# user = get_user()
# files = os.listdir(rf'C:\Users\{user}\Downloads')