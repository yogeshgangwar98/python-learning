# A Database connection context manager

class DatabaseConnection:
    def __enter__(self):
        return "Connected to DB"
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Connection closed")


with DatabaseConnection() as conn:
    print(conn)