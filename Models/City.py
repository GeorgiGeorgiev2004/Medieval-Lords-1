import services.model_services.city_service as cs


class City:
    def __init__(self, name, population, buildings):
        self.name = name
        self.pop = population
        self.buildings = buildings
        self.slots = cs.calculate_city_slots(self.pop)

    def __repr__(self):
        buildings = "\n".join([str(x) for x in self.buildings]) if self.buildings else "None"
        return f"{self.name} has population of {self.pop}, slots of {self.slots} and the buildings: " + buildings
