class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

class Country:
    def __init__(self, name, location):
        self.name = name
        self.location = location


location = Location
country = Country("Croatia", location)