class Database:
    def __init__(self, name):
        self.name = name
        
        
    def connection_name(self):
        print(self.name)
    
    def get_table(self):
        query = func(self.name)
        return query

# Decouple the responsibility
class QueryDatabase:
    def get_table(self):
        query = func(self.name)
        return query