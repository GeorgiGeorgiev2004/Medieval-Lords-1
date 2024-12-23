class Choice:
    def __init__(self, text, consequences):
        self.text = text
        self.consequences = consequences

    def __repr__(self):
        return f"{self.text} with the consequences of affecting your " + ", ".join(f"{flag} with this -> {value}" for flag, value in self.consequences.items())
