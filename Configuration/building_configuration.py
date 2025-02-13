from Models.Building import Building


def generate_buildings():
    buildings =[]
    b = Building("Lumberjack", 80, 0.61, 2)
    buildings.append(b)
    b = Building("Market", 110, 1.2, 2)
    buildings.append(b)
    b = Building("Church", 90, 0.71, 3)
    buildings.append(b)
    b = Building("Mine", 330, 11, 5)
    buildings.append(b)
    b = Building("Small camp", 60, 0.47, 1)
    buildings.append(b)

    return  buildings