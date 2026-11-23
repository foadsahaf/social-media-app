import pyodbc
import Variable
from datetime import datetime 
from color_text import color_Text as C
import os
#___________ Connect  _________
conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=DESKTOP-VD7AVO3;"
    "Database=Main_DB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()
#______________________________


#_____ input user _____
def input_USer(User_name, Email, Password, FirstName, LastName, phone):
    cursor.execute(
        """
        INSERT INTO [User]
        (User_name, Email, Password, [First Name], [Last Name], phone)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (User_name, Email, Password, FirstName, LastName, phone)
    )

    conn.commit()

    cursor.execute(
        """
        SELECT User_ID, User_name
        FROM [User]
        WHERE User_name = ? AND [Password] = ?
        """,
        (User_name, Password)
    )

    return cursor.fetchone()
#___________________________________________

#______ check user ____

def check_user(user_id, password):
    cursor.execute(
        "SELECT User_ID, User_name FROM [User] WHERE User_ID = ? AND [Password] = ?",
        (user_id, password)
    )
    return cursor.fetchone()
#____________________________________________

#____________ show post __________
def Show_post():
    cursor.execute(
        "SELECT Post_ID FROM Post"
    )
    return cursor.fetchall()
#___________________________________

#________________ check Like & Insert Like _________________
def Check_like():
    cursor.execute(
       """ SELECT Like_ID FROM [Like] Where User_ID = ? AND Post_ID = ? """,
       (Variable.V_userI,Variable.V_PostI)
    )
    return cursor.fetchone()
    

def Insert_like():
    cursor.execute(
           """ INSERT INTO [Like] (User_ID,Post_ID,Like_Data)  VALUES (?, ?, ?)""",
           (Variable.V_userI,Variable.V_PostI,datetime.now())
        )
    conn.commit()
    
def Delete_like():
    cursor.execute(
        """ DELETE FROM [Like] WHERE User_ID = ? AND Post_ID = ? """,
        (Variable.V_userI,Variable.V_PostI)
    )
    conn.commit()
#____________________________________________________________

#________________def comment ___________________
def Show_comment():
    cursor.execute(
            "SELECT post_ID,User_ID,[Comment Text] FROM Comment"
        )
    return cursor.fetchall()

def Add_comment(In_comment):
    cursor.execute(
               """ INSERT INTO Comment (Post_ID,User_ID,Comment_Data,[Editet status],[Comment Text])  VALUES (?, ?, ?,? , ?)""",
               (Variable.V_PostI,Variable.V_userI,datetime.now() ,"NO",In_comment)
            )
    conn.commit()
    return
#____________________________________

#________________creatpost_______________________
def insert_post (loc,imgU,cont):

    print("\n----- Post Details -----")
    print("Location :", loc)
    print("Image URL:", imgU)
    print("Content  :", cont)

    temp = input("\nDo you want to create this post? (y/n): ")

    if temp.lower() == 'y':

        cursor.execute(
            """
            INSERT INTO Post
                (User_ID, Location, Image_URL, Post_Date, [Content])
            OUTPUT INSERTED.Post_id
            VALUES (?, ?, ?, ?, ?)
            """,
            (Variable.V_userI,loc,imgU,datetime.now(),cont)
        )

        post_id = cursor.fetchone()[0]

        conn.commit()

        os.system('cls' if os.name == 'nt' else 'clear')
        print(C.GREEN_TExt + "\nPost created successfully!" + C.RESET_TExt )
    else:

        print(C.RED_TExt + "\nPost creation cancelled." + C.RESET_TExt)

        return None
#_______________________________________________________________________
