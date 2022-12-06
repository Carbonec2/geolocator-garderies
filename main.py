from excel_parser import ExcelParser
from geolocator import GeoLocator

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    parser = ExcelParser('./excel/repertoire16-sdg.xlsx', 'CPE et GARD en fonction')
    locator = GeoLocator()

    for i in range(3, 595):
        locator = GeoLocator()
        address_data = parser.get_address_data_dict(int(i))
        location_data = locator.locate_dict(address_data)
        parser.write_geocode_to_csv(address_data['street'], address_data['city'], address_data['postalcode'],
                                    location_data.longitude, location_data.latitude)
