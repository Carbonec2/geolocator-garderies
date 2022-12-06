from geopy import GoogleV3


class GeoLocator:

    def __init__(self):
        f = open('api.txt')
        self.api_key = f.read()
        # Calling Google API
        self.locator = GoogleV3(self.api_key)

    def locate_dict(self, address_dict):
        location = self.locator.geocode(address_dict)

        if location:
            print(' ')
            print(address_dict['street'] + ' ' + address_dict['city'] + ' ' + address_dict['postalcode'])
            print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
            return location
        return None
