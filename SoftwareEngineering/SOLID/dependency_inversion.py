"""
Dependency Inversion Principle
Dependency should be on abstractions not concretions
A. High-level modules should not depend upon low-level modules. Both should depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon abstractions.

There comes a point in software development where our app will be largely composed of modules. 
When this happens, we have to clear things up by using dependency injection. 
High-level components depending on low-level components to function.
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

# Inheritance: is-a-relationship
class Structured(Database):
    def __init__(self):
        pass

# Aggregation: has-a-relationship
class Unstructured:
    def __init__(self, database: Database):
        self.database = database
    

"""
High-level modules should not depend on low-level level modules. It should depend upon its abstraction.
"""