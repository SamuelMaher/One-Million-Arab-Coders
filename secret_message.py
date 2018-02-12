import os
import string
def rename_files():
    file_list = os.listdir(r"E:\Udacity Full stack foundation\alphabet")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"E:\Udacity Full stack foundation\alphabet")
    for file_name in file_list:
        os.rename (file_name, file_name.strip ("0123456789"))
    os.chdir(saved_path)
rename_files()
