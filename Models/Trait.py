class Trait:
    def __init__(self,name, modifier_value):
        self.name = name
        self.modifier_value = modifier_value

    def __repr__(self):
        return f"{self.name} gives {self.modifier_value[0]} the effect {self.modifier_value[1]}"