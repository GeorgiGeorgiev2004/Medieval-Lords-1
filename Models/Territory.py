class Territory:
    def __init__(self, city_slots=4, existing_cities=[], name=""):
        self.city_slots = city_slots
        self.cities = existing_cities
        self.name = name

    def __repr__(self):
        return f"The {self.name} can contain up to {self.city_slots} cities and the already existing ones are: " + ", ".join(
            [x.name for x in self.cities])
