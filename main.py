import os
from storage.file_storage import FileStorage
from services.user_service import UserService
"""
main.py
-------
CLI (Command Line Interface) for the User Manager project.

Responsibilities:
- Show menu to user (input/print)
- Call UserService methods
- Display results/messages

Important:
- No business logic here (no hashing, no file parsing).
- Only user interaction + calling the service layer.
"""

def main():
   
    # (prevents "CWD" / working-directory bugs).
    # 🔹 Build absolute path to data/users.txt
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FILE = os.path.join(BASE_DIR, "data", "users.txt")
    print("DATA_FILE =", DATA_FILE)


    # Created object for loaded users 
    # storage = FileStorage('data/users.txt')
    storage = FileStorage(DATA_FILE)

    service = UserService(storage)  
    
    # Main menu loop: keeps the program running until the user chooses Exit.
    while True:
           print("\n=== USER MANAGER ===")
           print("1) Register")
           print("2) Login")
           print("3) Update Password")
           print("4) Delete User")
           print("5) List Users")
           print("0) Exit")

           user_choice = input('Enter user choice from 0 to 5 ')

           if user_choice == '1':
                 username = input('Etner username ').strip()
                 password = input('Enter password ').strip()
                 ok, msg = service.register_user(username,password)
                 print(msg)
                 
           elif user_choice == '2':
                 username = input('Etner username ')
                 password = input('Enter password ')

                 ok,msg = service.login_user(username,password)
                 print(msg)
           elif user_choice == '3':
                 username = input('Enter username want to update ')
                 new_passowrd = input('enter new password ')
                 ok,msg = service.update_password(username,new_passowrd)
                 print(msg)

           elif user_choice == '4':
                 username = input('Enter username want to delete ')
                 ok,msg = service.delete_user(username)
                 print(msg)
           elif user_choice == '5':
                 users = service.list_users()
                 if not users:
                       print('no user found')
                 else:
                    '\n Users are'
                    for i in users:
                          print(i['username'])

           elif user_choice == '0':
                 print('goodbye')
                 break
           else:
                 print('invalid choice')
                 break

if __name__ == "__main__":
        main()








