class Database:
    def __init__(self, name):
        self.name = name
        
        
    def connection_name(self):
        print(self.name)
    
    def get_table(self):
        fetch = func(self.name)
        return fetch

# Decouple the responsibility
class QueryDatabase:
    def get_table(self):
        fetch = func(self.name)
        return fetch