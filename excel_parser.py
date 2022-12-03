import pandas
import sys


class ExcelParser:

    def __init__(self, path, sheet_name):
        self.workbook = pandas.read_excel(path, sheet_name=sheet_name)
        self.workbook.head()

    def get_address_data(self, row):
        # Le data commence à la row 3
        # Le data commence à la col 2
        return_address = ''

        return_address += self.workbook.iloc[row, 2]
        return_address += ', ' + self.workbook.iloc[row, 3]
        return_address += ', ' + self.workbook.iloc[row, 4]

        return return_address

    def get_address_data_dict(self, row):
        # Le data commence à la row 3
        # Le data commence à la col 2
        dict_address = {'street': self.workbook.iloc[row, 2], 'city': self.workbook.iloc[row, 3],
                        'postalcode': self.workbook.iloc[row, 4], 'country': 'Canada', 'state': 'QC'}

        return dict_address
