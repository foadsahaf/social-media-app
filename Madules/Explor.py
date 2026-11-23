import os
import DB_connect.Pythone_coonect_to_SQL as PS
import Variable
from color_text import color_Text as C
def post():
    posts = PS.Show_post()
    if not posts:
        print("\nNo posts available.")
        return False
    
    print("\n--- List of Posts ---")
    for i in range(0, len(posts), 3):
        row = posts[i:i+3]
        print(row)
    print("-" * 20)
    return True

def select_post():
    has_posts = post()
    if not has_posts:
        return

    while True: 
        try:
            inp = int(input("\nWhich Post do you select? ['0' Exit]: "))
        except ValueError:
            print(C.YELLOW_TExt + "Please enter only a number!" + C.RESET_TExt)
            continue

        if inp == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Exiting the Explore section...")
            break

        list_post = PS.Show_post()

        # for in list_post:
        post_ids = [p[0] for p in list_post]
        if inp in post_ids:
            print(C.BLUE_TExt + f"\n[OK!] You selected post {inp}" + C.RESET_TExt)
            Variable.V_PostI = inp  

            while True:
                print("\nOptions: [1] Comment | [2] Like / Unlike | [3] Back to posts list")
                try:
                    action = int(input("Select: "))
                except ValueError:
                    print(C.RED_TExt +"Please enter only a number!"+C.RESET_TExt)
                    continue

                if action == 1:
                    comment(inp)
                elif action == 2:
                    Like()
                elif action == 3:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    post()
                    break  
                else:
                    print(C.YELLOW_TExt + "Invalid option!" + C.RESET_TExt)
        else:
            print(C.YELLOW_TExt + "Post not found! Please try again." + C.RESET_TExt)


def comment(inp_PID):
        lis = PS.Show_comment()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("----------------------------------------------------")
        print(C.BLUE_TExt + f"\n[OK!] You selected post {Variable.V_PostI}" + C.RESET_TExt)
        for p in lis:
            if p[0] == inp_PID and Variable.V_userI== p[1]:
                print(C.BOLD_TExt+ C.BLUE_TExt + f"{p[1]} : {p[2]}" + C.RESET_TExt )
            elif p[0] == inp_PID:
                print(f"{p[1]} : {p[2]}")
        print("****************************************************")

        while True:
            print("Are you add comment for this post? [1] yes [2] no")

            try:
                z = int(input(": "))
            except ValueError:
                print(C.YELLOW_TExt + "Please enter only a number!" + C.RESET_TExt)
                continue

            if z == 1:
                print("Type your Comment ---> ")
                inp_comment = input(":")
                PS.Add_comment(inp_comment)
                print(C.GREEN_TExt + "Successful ADD comment" + C.RESET_TExt)
                return

            elif z == 2:
                return

            else:
                print(C.YELLOW_TExt + "Invalid option!" + C.RESET_TExt)

                      
def Like():
        


        #select = int(input("Like [1] | UnLike [2] : "))

        if PS.Check_like() is None:
                print("You haven't liked this post. Are you sure you want to like it? [1]yes [2]no")
                while True:
                    try:
                        z = int(input("Which one: "))
                    except ValueError:
                        print("Please enter only a number!")
                        continue

                    if z == 1: 
                        PS.Insert_like()
                        print("❤️ " +C.GREEN_TExt + "Post Liked successfully!" + C.RESET_TExt)
                        return
                    elif z==2:
                        return
                    else:
                        print(C.YELLOW_TExt + "Invalid option!" + C.RESET_TExt)
              
        else:
                print("You have already liked this post.")
                print("-------------------------")
                print("[1] Unlike")
                print("[2] Back")
                while True:          
                        try:
                            choice = int(input("Select: "))
                        except ValueError:
                            print("Please enter only a number!")
                            continue

                        if choice == 1:
                            PS.Delete_like()
                            print("💔 " + C.GREEN_TExt + "Post unliked successfully!" + C.RESET_TExt)
                            break

                        elif choice == 2:
                            return

                        else:
                            print(C.YELLOW_TExt + "Invalid option! Please try again." + C.RESET_TExt)

def creat_post():
    #new_post_id =
    loc = input("Location: ")
    imgU = input("Image URL: ")
    cont = input("Content: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    PS.insert_post(loc,imgU,cont)
