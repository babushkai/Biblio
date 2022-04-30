class Country:
    def __init__(self, name):
        self.name = None
        self.map = None

    def product(self, a, b):
        return a*b

    def set_map(self):
        self.map = self.product(self.latitude, self.longitude)

class Tokyo(Country):
    def __init__(self,  longitude, latitude, name):
        super.__init__(name)
        self.longitude = longitude
        self.latitude = latitude

class Paris(Country):
    def __init__(self,  longitude, latitude, name):
        super.__init__(nam)
        self.longitude = longitude
        self.latitude = latitude     
    
class Moscow(Country):
    def __init__(self,  longitude, latitude, name):
        super.__init__(nam)
        self.longitude = longitude
        self.latitude = latitude
