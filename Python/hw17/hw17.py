# Homework 17
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw17.txt
#
# ###############################################################################
#

from exif import Image
from Python.hw16.hw16 import *


def image_coordinates(image_path):
    coords = {}
    with open(image_path, 'rb') as src:
        img = Image(src)
    if img.has_exif:
        try:
            coords['lat'] = img.gps_latitude
            coords['lng'] = img.gps_longitude
            return coords
        except AttributeError:
            print('No Coordinates have been found')
    else:
        print('The Image has no EXIF information')


def gps_to_str(coords):
    lat = str(coords['lat'][0]) + ',' + str(coords['lat'][1])
    lng = str(coords['lng'][0]) + ',' + str(coords['lng'][1])
    return str(lat + ';' + lng + "'")


def write_gps_to_file(file, coords):
    with open(file, 'a') as f:
        f.write(gps_to_str(coords))
        f.write('\n')
    f.close()


if __name__ == '__main__':
    key_file_path = '../resources/GoogleMapsAPIKey.txt'
    coordinates_file_path = '../resources/GPS_coordinates_from_images.txt'
    images = ['../resources/nepal_with_gps.jpeg', '../resources/normadling_with_gps.jpg']
    for img in images:
        coords = image_coordinates(img)
        write_gps_to_file(coordinates_file_path, coords)
        res = get_google_place(coordinates_file_path)
    print_context(res, key_file_path)
