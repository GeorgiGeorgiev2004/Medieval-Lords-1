class Territory:
    def __init__(self, city_slots=4, existing_cities=[]):
        self.city_slots = city_slots
        self.cities = existing_cities

    def __repr__(self):
        return f"The territory can contain up to {self.city_slots} cities and the already existing ones are: " + ", ".join(
            [x.name for x in self.cities])
