import BuildingService as BS
import Models.City as c
from Common.Constants import CityAlgorithm as ca

import math

def show_building_slots(city):
    print(city.slots)

def show_pop(city):
    print(city.pop)

def show_city_buildings(city):
    print(city.buildings)

def add_building(city, building):
    if city.slots >= len(city.buildings):
        print(f"All {city.slots} city slots are full! Demolish a building or expand the city!")
    else:
        BS.build_building(building)

def calculate_city_slots(steps, start=ca.START, growth_rate=ca.GROWTH_RATE):
    progression = [start]
    current = start

    for i in range(1, steps):
        increment = growth_rate / math.sqrt(i + 1)
        current += increment
        progression.append(current)

    return round(progression[len(progression)-1])

def create_city(name, pop, buildings):
    slots = calculate_city_slots(pop)
    return c.City(name, pop, buildings, slots)

