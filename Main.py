from Madules.SingIn_OR_up import Sing_Up,Sing_in
from Madules import Explor
import os
import sys
from DB_connect import Pythone_coonect_to_SQL as DB
from color_text import color_Text as C
import Variable
os.system('cls' if os.name == 'nt' else 'clear')
#print(C.BLUE_TExt+"SALAM"+C.RESET_TExt)
print("*" * 50,"\n")
print(" "*18,'Hello,Wellcome','\n')
print("*" * 50)
print()


while(True):
    try:
        x = int(input("Sing in [1] | Sing Up [2] : "))
        if x == 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            Sing_in()
            break
        elif x == 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            Sing_Up()
            break
        else:
            print("Select Not True !!!")
    except ValueError:
        print("Only Number :)")

#print("========================")
while True:

    print("1. Show Explor !")
    print("2. Creat post !")
    print("3. Exit !")
    print("------------------------")

    try:
        z = int(input("Which item: "))
    except ValueError:
        print("Please enter only a number!")
        continue

    if z == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        Explor.select_post()

    elif z == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        Explor.creat_post()

    elif z == 3:
        print("Goodbye!")
        break

    else:
        print("Try Again.")