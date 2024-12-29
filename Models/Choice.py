class Choice:
    def __init__(self, text, consequences, flag, other_char=None, func_to_handle=None):
        self.text = text
        self.consequences = consequences
        self.flag = flag
        self.other_char = other_char
        self.func_to_handle = func_to_handle

    def __repr__(self):
        return f"{self.text} with the consequences of affecting your " + ", ".join(f"{flag} with this -> {value}" for flag, value in self.consequences.items())
