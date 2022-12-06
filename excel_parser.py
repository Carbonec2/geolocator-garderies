import csv
import pandas


class ExcelParser:

    def __init__(self, path, sheet_name):
        self.workbook = pandas.read_excel(path, sheet_name=sheet_name)
        self.workbook.head()

        f = open('output.csv', 'w')
        self.writer = csv.writer(f)

        row_data = ["street", "city", "postalcode", "lon", "lat"]

        self.writer.writerow(row_data)

    def get_address_data_dict(self, row):
        # Le data commence à la row 3
        # Le data commence à la col 2
        dict_address = {'street': self.workbook.iloc[row, 2], 'city': self.workbook.iloc[row, 3],
                        'postalcode': self.workbook.iloc[row, 4], 'country': 'Canada', 'state': 'QC'}

        return dict_address

    def write_geocode_to_csv(self, street, city, postalcode, lon, lat):
        row_data = [street, city, postalcode, lon, lat]
        self.writer.writerow(row_data)
