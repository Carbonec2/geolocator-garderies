# This is a sample Python script.
from excel_parser import ExcelParser
from geolocator import GeoLocator


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    parser = ExcelParser('./excel/repertoire16-sdg.xlsx', 'CPE et GARD en fonction')

    locator = GeoLocator()

    for i in range(3, 595):
        locator = GeoLocator()
        locator.locate_dict(parser.get_address_data_dict(int(i)))


    # parser.get_address_data(3)
    # locator = GeoLocator()



    # locator.locate(parser.get_address_data(3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
