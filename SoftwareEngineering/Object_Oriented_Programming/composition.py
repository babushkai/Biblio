class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

class Country:
    def __init__(self, name):
        self.name = name
        self.location = Location()
