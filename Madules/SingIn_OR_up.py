from DB_connect import Pythone_coonect_to_SQL as PS
import os
import Variable

def get_username():
    while True:
        User_name = input("Please Type your Username: ")

        if not User_name.isalpha():
            print("❌ Username must contain only letters.")
            continue

        if len(User_name) < 3:
            print("❌ Username must be at least 3 characters.")
            continue

        return User_name


def get_email():
    while True:
        user_Email = input("Please Type your Email: ")

        if "@" not in user_Email or "." not in user_Email:
            print("❌ Invalid Email.")
            continue

        return user_Email


def get_password():
    while True:
        user_Password = input("Please Type your Password: ")

        if len(user_Password) < 8:
            print("❌ Password must be at least 8 characters.")
            continue

        return user_Password


def get_firstname():
    while True:
        user_FirstName = input("Please Type your firstname: ")

        if not user_FirstName.isalpha():
            print("❌ Firstname must contain only letters.")
            continue

        if len(user_FirstName) < 2:
            print("❌ Firstname must be at least 2 characters.")
            continue

        return user_FirstName


def get_lastname():
    while True:
        user_LastName = input("Please Type your Lastname: ")

        if not user_LastName.isalpha():
            print("❌ Lastname must contain only letters.")
            continue

        if len(user_LastName) < 2:
            print("❌ Lastname must be at least 2 characters.")
            continue

        return user_LastName


def get_phone():
    while True:
        user_phone = input("Please Type your phoneNumber: ")

        if not user_phone.isdigit():
            print("❌ Phone number must contain only numbers.")
            continue

        if len(user_phone) != 11:
            print("❌ Phone number must be 11 digits.")
            continue

        if not user_phone.startswith("0"):
            print("❌ Phone number must start with 0.")
            continue

        return user_phone


def Sing_in():
    while True:
        User_ID = int(input("Please Type your UserId: "))
        user_Password = input("Please Type your Password: ")
        check = PS.check_user(User_ID,user_Password)
        if check is not None:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Userid:",check.User_ID)
            print("UserName:",check.User_name)
            Variable.V_userI = check.User_ID
            Variable.V_userN = check.User_name
            print("-------------------------------------- \n")
            break
        else:
            print("Incorrect User ID or Password.")
    return    

def Sing_Up():
 
    User_name = get_username()

    user_Email = get_email()

    user_Password = get_password()

    user_FirstName = get_firstname()

    user_LastName = get_lastname()

    user_phone = get_phone()

    topl = PS.input_USer(
        User_name,
        user_Email,
        user_Password,
        user_FirstName,
        user_LastName,
        user_phone
    )

    Variable.V_userI = topl[0]
    Variable.V_userN = topl[1]

    print("Your data Confirm ✅")
    print("Enter every key To next section")
    input()

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Userid:", Variable.V_userI)
    print("UserName:", Variable.V_userN)
    print("-----------------------------------------------")
