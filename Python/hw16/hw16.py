# Homework 16
#
# https://github.com/CsteerDevops1/lectures_devops2/blob/main/Python/Homework/hw16.txt
#
# ###############################################################################
#
import requests


def get_lat_lng(apiKey, lat, lng):
    url = ('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}'
           .format(lat, lng, apiKey))
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        address = resp_json_payload['results'][0]['formatted_address']
    except:
        print('ERROR: {}, {}'.format(lat, lng))
        address = ''
    return address


if __name__ == '__main__':
    f_name = '../resources/GoogleMapsAPIKey.txt'
    f_coordinates_name = '../resources/GPS_coordinates.txt'
    coordinates = []

    file = open(f_name, 'r')
    apiKey = file.read()
    file.close()

    file = open(f_coordinates_name, 'r')
    for line in file.readlines():
        coordinates.append({"lat": line.rstrip().split(',')[0], "lng": line.rstrip().split(',')[1]})
    file.close()

    for item in coordinates:
        address = get_lat_lng(apiKey, item['lat'], item['lng'])
        print("==========================================")
        print('Location: {}'.format(address))
        print('Goggle Maps URL: https://www.google.com/maps/search/?api=1&query={},{}'.format(item['lat'], item['lng']))
