from utils.validators import username_validation,password_validation
from utils.security import hash_password,verify_password
from storage.file_storage import FileStorage

"""
---------------
Business logic layer for the User Manager project.

Responsibilities:
- Validate input (via validators)
- Hash/verify passwords (via security utils)
- Perform CRUD operations on users
- Persist changes using storage (FileStorage)
Rule:
- This layer does NOT use input() or print().
- It returns (success, message) so main.py can decide what to display.
"""

 # Helper method: internal search utility used by multiple service methods.
# Returns a user dict if found, otherwise None.
class UserService:
   

    def __init__(self,storage):
        self.storage = storage
        self.users = self.storage.load_users()

    def _find_users(self ,username):
        for user in self.users:
            if user['username'] == username:
                return user
        return None
    
    # Service methods return: (bool, message)
    # This keeps output consistent and makes CLI/UI simple.
    def register_user(self,username,password):
        is_valid, message = username_validation(username)
        if not is_valid:
            return False,message
            
    
        is_valid , message = password_validation(password)
        if not is_valid:
            return False, message
    
        if self._find_users(username):
            return False, 'user already exist'
    
        hashed  = hash_password(password)

        new_user = {
        'username' : username,
        'password' : hashed
        }

        self.users.append(new_user)
        self.storage.save_users(self.users)

        return True, 'User registered successfully'

    def list_users(self):
        return self.users
    
    # Service methods return: (bool, message)
    # This keeps output consistent and makes CLI/UI simple.
    def login_user(self,username,passowrd):
        user = self._find_users(username)
        if not user:
            return False,'User not found'
        
        if not verify_password(passowrd , user['password']):
            return False, 'Invalid Username or Password'
        
        return True,'login done'
    
    # Service methods return: (bool, message)
    # This keeps output consistent and makes CLI/UI simple.
    def update_password(self,username, new_password):
        user = self._find_users(username)
        if not user:
            return False ,'User not found '
        hashed_password = hash_password(new_password)
        user['password'] = hashed_password
        self.storage.save_users(self.users)
        return True, 'password changed'
    
    # Service methods return: (bool, message)
    # This keeps output consistent and makes CLI/UI simple.
    def delete_user(self,username):
        user = self._find_users(username)
        if not user:
            return False, 'user not found'
        self.users.remove(user)
        self.storage.save_users(self.users)
        return True,'Use deleted'




















    

    




