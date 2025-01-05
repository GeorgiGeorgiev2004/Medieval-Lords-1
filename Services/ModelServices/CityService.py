import Models.City as c
from Common.Constants import CityAlgorithm as ca
from Common.Constants import GameEssentials as ge
from Common.Constants import Modifiers as ccm
from Models import CustomError as ce
import Configuration.BuildingConfiguration as cbc
import math

def show_building_slots(city):
    print(city.slots)

def show_pop(city):
    print(city.pop)

def show_city_buildings(city):
    print(city.buildings)

def add_building(city):
    if city.slots <= len(city.buildings):
        raise ce.NoFreeSlotsToBuildIn()
    buildings = cbc.generate_buildings()
    print("Available buildings: "+", ".join([str(x) for x in buildings]))
    cmd = input("Which building would you like to build?")
    while cmd not in [x.name for x in buildings]:
        cmd = input("Which building would you like to remove?")
    ind = [x.name for x in buildings].index(cmd)
    if ge.PLAYER_CHARACTER.modifiers[ccm.gold]<buildings[ind].price:
        raise ce.YokParichok()
    else:
        ge.PLAYER_CHARACTER.modifiers[ccm.gold] -=buildings[ind].price
        city.buildings.append(buildings[ind])

def remove_building(city):
    a = ge.PLAYER_CHARACTER
    print("Available buildings: "+", ".join([str(x) for x in city.buildings]))
    cmd = input("Which building would you like to remove?")
    while cmd not in [x.name for x in city.buildings]:
        cmd = input("Which building would you like to remove?")
    ind = [x.name for x in city.buildings].index(cmd)
    city.buildings.remove(city.buildings[ind])

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
    return c.City(name, pop, buildings)

