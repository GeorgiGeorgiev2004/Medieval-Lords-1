from Common.Constants import GameEssentials as ge
from Common.Constants import Text as t
from Services.ModelServices import CityService as cs
def display_terry(terry):
    return f"In your territory that can contain {terry.city_slots} cities the currently avaluable are: " + ", ".join([str(x) for x in terry.cities])


def modify_terry():
    print(display_terry(ge.PLAYER_CHARACTER.governed_territory))
    city = input("Which city would you like to change?")
    if city in [x.name for x in ge.PLAYER_CHARACTER.governed_territory.cities]:
        ind = [x.name for x in ge.PLAYER_CHARACTER.governed_territory.cities].index(city)
        cmd = input(t.modify_city_how)
        if cmd == "build":
            cs.add_building(ge.PLAYER_CHARACTER.governed_territory.cities[ind])
        if cmd == "stats":
            ge.PLAYER_CHARACTER.present_self()
        elif cmd == "destroy":
            cs.remove_building(ge.PLAYER_CHARACTER.governed_territory.cities[ind])