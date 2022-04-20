"""

Liskov Substitution Principle
A sub-class must be substitutable for its super-class.
The aim of this principle is to ascertain that a sub-class can assume the place of its super-class without errors. 
If the code finds itself checking the type of class then, it must have violated this principle.

"""
class Database:
    def __init__(self, name):
        self.name = name
        
        
    def connection_name(self):
        print(self.name)
    
    def get_table(self):
        fetch = func(self.name)
        return fetch

    def get_structure(self):
        pass
        
    def get_view(self, table, query):
        table = get_table()
        view = query(table)

class BigTable(Database):
    def get_view(self, table, query, index):
        table = get_table()
        view = query(table, index)

class Cassandra(Database):
    def get_view(self, table, query, index):
        table = get_table()
        view = query(table, index)

class Spanner(Database):
    def get_view(self, table, query, key):
        table = get_table()
        view = query(table, key)
