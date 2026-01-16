import json

from decouple import config
from geopy import distance
import folium
import requests


APIKEY = config('APIKEY')


def fetch_coordinates(APIKEY, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": APIKEY,
        "format": "json",
    })
    response.raise_for_status()
    found_places = (
    	response.json()['response']['GeoObjectCollection']['featureMember']
    )

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lon, lat


def get_coffee_shop_coords(shop):
	return shop['distance']


def main():
	with open('coffee.json', 'r', encoding='cp1251') as my_file:
		file_contents = my_file.read()
	
	contents = json.loads(file_contents)		

	your_address = input('Где вы находитесь? ')
	coords = fetch_coordinates(APIKEY, your_address)
	coords_geopy = (coords[1], coords[0])
	coffee_shops = []
	
	for coffee_shop in contents:
		shop = dict()
		shop['title'] = coffee_shop['Name']
		shop['distance'] = distance.distance(
			coords_geopy, (
				coffee_shop['geoData']['coordinates'][1], 
				coffee_shop['geoData']['coordinates'][0],
			)
		).km
		shop['latitude'] = coffee_shop['geoData']['coordinates'][1]
		shop['longitude'] = coffee_shop['geoData']['coordinates'][0]
		coffee_shops.append(shop)

	sorted_shops = sorted(coffee_shops, key=get_coffee_shop_coords)[:5]

	m = folium.Map(coords_geopy, zoom_start=13)
	for shop in sorted_shops:		
		folium.Marker(
			location=(shop['latitude'], shop['longitude']),
			tooltip=shop['title'],
			popup=shop['title'],
			icon=folium.Icon(color='green'),
		).add_to(m)
	m.save('index.html')


if __name__ == '__main__':
	main()