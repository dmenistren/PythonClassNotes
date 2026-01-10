class Auth:
    def __init__(self, con, cur):
        print("Auth class initialized")
        self.con = con
        self.cur = cur
        
    def login(self, username, password):
        # Dummy login method
        print(f"Logging in user: {username}")
        return True
    
