# move file
import os

print("\n== Move File ==")
print("1. Move file")
print("E. Exit")
choice = input("choice: ")

src = "Jokes.txt"
dst = r"C:\Users\XaveF\Documents\Jokes.txt"

while choice != 'e' and choice != 'E':
    if choice == '1':
        print("\n[ Move file ]")
        try:
            if os.path.exists(dst):
                print(" File is already exist")
            else:
                os.replace(src,dst)
                print(src + " was moved")
        except FileNotFoundError:
            print("[" + src + " is not found ]")
    else:
        print("\n[ Invalid choice ]")

    print("\n== Move File ==")
    print("1. Move file")
    print("E. Exit")
    choice = input("choice: ")

if choice == 'e' or choice == 'E':
    print("\n== Exit Program ==")