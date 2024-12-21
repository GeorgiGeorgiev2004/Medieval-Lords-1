import os
from fileinput import close

def Create_save_file(name):
    if os.path.exists(f"{name}.txt"):
        choice = input("Do you want to rewrite existing file?")
        if choice is 'Y':
            open(f"{name}.txt", 'w')
            close()
        elif choice is 'N':
            pass
    else:
        open(f"{name}.txt",'x')
        close()

