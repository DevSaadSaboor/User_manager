"""
---------------
Storage layer for the User Manager project.

Responsibilities:
- Save users to a file
- Load users from a file

File Format:
Each line represents one user:
username,password_hash

Rule:
- Storage must always return a list of dicts:
  [{"username": str, "password": str}, ...]
- Storage must never return lists inside dict values (e.g., ["saad"]).
"""
class FileStorage:
    def __init__(self,filepath):
        self.filepath = filepath

    # Read file line-by-line. Each line must be: username,password_hash
    # We strip whitespace and skip empty lines to avoid parsing errors.
    def load_users(self):
        users = []
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    username,password = line.split(",",1)
                    data  = {
                        'username' : username,
                        'password' : password
                    }
                    users.append(data)
        except FileNotFoundError:
            pass    
        
        return users
    
    # Write all users back to file (overwrite mode).
    # Each user is stored as: username,password_hash
    # One user per line to keep file readable and stable across restarts.  
    def save_users(self, users):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            for user in users:
                file.write((f'{user["username"]},{user["password"]}\n'))

    
                








    
        