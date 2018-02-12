import os
import string
def rename_files():
    file_list = os.listdir(r"E:\Udacity Full stack foundation\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"E:\Udacity Full stack foundation\prank")
    for file_name in file_list:
        print("old Name "+file_name)
        print("New Name "+file_name.strip ("0123456789"))
        os.rename (file_name, file_name.strip ("0123456789"))
    os.chdir(saved_path)
rename_files()
