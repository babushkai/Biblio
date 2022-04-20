
"""
Open-Closed Principle
Software entities(Classes, modules, functions) should be open for extension, not modification.
"""

class Database:
    def __init__(self, name):
        self.name = name
        
        
    def connection_name(self):
        print(self.name)
    
    def get_table(self):
        query = func(self.name)
        return query

databases = [
    Database("BigTable"),
    Database("Cassandra")
]

def database_structure(databases: list):
    for database in databases:
        if database.name == "BigTable" or "Cassandra":
            print("Unstructured")
        else:
            continue 

"""
This method is imcompatible if the database is for structured
"""

class Database:
    def __init__(self, name):
        self.name = name
        
    def connection_name(self):
        print(self.name)
    
    def get_structure(self):
        pass

class BigTable(Database):
    def get_structure(self):
        print("Unstructured")

class Cassandra(Database):
    def get_structure(self):
        print("Unstructured")

class Spanner(Database):
    def get_structure(self):
        print("Structured")


databases = [
    Database("BigTable"),
    Database("Cassandra"),
    Database("Spanner")
]

def database_structure(databases: list):
    for database in databases:
        database.get_structure()

"""
This allows the extensions
"""