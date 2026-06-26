from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def execute_query(self, query):
        pass

class MySQLDatabase(Database):
    def connect(self):
        print("Connected to MySQL")

    def disconnect(self):
        print("Disconnected from MySQL")
    
    def execute_query(self, query):
        print(f"Executing:\n{query}")

class MongoDBDatabase(Database):
    def connect(self):
        print("Connected to MongoDB")

    def disconnect(self):
        print("Disconnected from MongoDB")
    
    def execute_query(self, query):
        print(f"Executing:\n{query}")


class PostgreSQLDatabase(Database):
    def connect(self):
        print("Connected to PostgreSQL")

    def disconnect(self):
        print("Disconnected from PostgreSQL")
    
    def execute_query(self, query):
        print(f"Executing:\n{query}")


db = MySQLDatabase()

db.connect()
db.execute_query(
    "SELECT * FROM users"
)
db.disconnect()