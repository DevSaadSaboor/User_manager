class User:
    def __init__(self,username,password):
        self.username = username
        self.password  = password
    
    def to_dict(self):
        users= {
            'username': self.username,
            'password' : self.password
        }
        return users
    
    @staticmethod
    def from_dict(data):
        return User  (
            data['username'],
            data['password']
        )
    
    

        

        