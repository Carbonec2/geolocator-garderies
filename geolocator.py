import time

from geopy import Nominatim, GoogleV3
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd


class GeoLocator:

    def __init__(self):
        # self.locator = Nominatim(user_agent="myGeocoder")
        f = open('api.txt')
        self.api_key = f.read()
        self.locator = GoogleV3(self.api_key)

    def locate(self, addressString):
        location = self.locator.geocode(addressString)

        time.sleep(2)

        if location:
            print(' ')
            print(addressString)
            print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
            return location
        return None

    def locate_dict(self, address_dict):

        location = self.locator.geocode(address_dict)
        time.sleep(1)

        if location:
            print(' ')
            #print(address_dict['street']+' '+address_dict['city']+' '+address_dict['postalcode'])
            print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))
            return location
        return None