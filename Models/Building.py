class Building:
    def __init__(self, name, price, expected_income, build_time):
        self.name = name
        self.price = price
        self.expected_income = expected_income
        self.build_time = build_time

    def __repr__(self):
        return f"{self.name}'s cost is {self.price} and it makes {self.expected_income} per turn"
