import BuildingService as BS
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
