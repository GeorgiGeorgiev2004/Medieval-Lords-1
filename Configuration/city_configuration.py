import services.model_services.city_service as smss
import configuration.building_configuration as cbc

buildings = cbc.generate_buildings()


def generate_cities_for_Viktor():
    cities = []
    city = smss.create_city("Silistra", 6, [buildings[0]])
    cities.append(city)
    city = smss.create_city("Polqnata", 2, [])
    cities.append(city)
    return cities


def generate_cities_for_Smort():
    cities = []
    city = smss.create_city("Mustangrad", 9, [buildings[0]])
    cities.append(city)
    city = smss.create_city("Mezdra", 8, [buildings[1], buildings[2]])
    cities.append(city)
    city = smss.create_city("Pastra", 3, [])
    cities.append(city)
    city = smss.create_city("Tsarigrad", 15, [buildings[2], buildings[3], buildings[1]])
    cities.append(city)
    return cities
