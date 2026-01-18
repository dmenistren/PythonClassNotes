import psycopg2
from psycopg2 import errors

class AuthService:
    def __init__(self, conn, cur):
        # We store these in the instance so methods can access them via 'self'
        self.conn = conn
        self.cur = cur

    def sign_up(self, username, password):
        try:
            # Check if user already exists first
            self.cur.execute("SELECT name FROM usr WHERE name = %s", (username,))
            if self.cur.fetchone():
                print(f"Error: The username '{username}' is already taken.")
                return False

            # Insert new user
            query = "INSERT INTO usr (name, pswd) VALUES (%s, %s)"
            self.cur.execute(query, (username, password))
            self.conn.commit()
            print(f"Successfully created account! Hello {username}!")
            return True
        except Exception as e:
            #to revert any changes in the transaction
            self.conn.rollback()
            print(f"An error occurred: {e}")
            return False

    def login(self, username, password):
        query = "SELECT * FROM usr WHERE name = %s AND pswd = %s"
        self.cur.execute(query, (username, password))
        user = self.cur.fetchone()
        return user

def main():
    # Setup connection outside the loop
    try:
        conn = psycopg2.connect(
            dbname="auth", 
            user="postgres", 
            password="hello123", 
            host="localhost"
        )
        cur = conn.cursor()
        
        # Initialize the service once
        auth_service = AuthService(conn, cur)

        while True:
            print("\n--- Auth System ---")
            choice = input("1. Signup\n2. Login\n3. Exit\nChoice: ")

            if choice == "1":
                name = input("Set a Username: ")
                pswd = input("Set a Password: ")
                auth_service.sign_up(name, pswd)

            elif choice == "2":
                name = input("Enter your Username: ")
                pswd = input("Enter your Password: ")
                user = auth_service.login(name, pswd)
                
                if user:
                    print(f"Welcome back, {name}!")
                else:
                    print("Invalid credentials.")
                    create = input("Would you like to create an account? (y/n): ")
                    if create.lower() == 'y':
                        pswd = input("Set a Password: ")
                        auth_service.sign_up(name, pswd)
            
            elif choice == "3":
                break
        
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Database connection failed: {e}")

if __name__ == "__main__":
    main()