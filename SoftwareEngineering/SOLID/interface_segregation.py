
"""
Interface Segregation Principle
Make fine grained interfaces that are client specific
Clients should not be forced to depend upon interfaces that they do not use.
This principle deals with the disadvantages of implementing big interfaces.
"""

class DataBase:
    def get_schema(self):
        raise NotImplementedError

class BigTable(Database):
    def get_schema(self):
        pass

class Cassandra(Database):
    def get_schema(self):
        pass 

class Spanner(Database):
    def get_schema(self):
        pass