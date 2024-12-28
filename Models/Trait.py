class Trait:
    def __init__(self,name, modifier_value, modif_flag):
        self.name = name
        self.modifier_value = modifier_value
        self.modif_flag = modif_flag

    def __repr__(self):
        return f"{self.name} gives {self.modifier_value[0]} the effect {self.modifier_value[1]}"