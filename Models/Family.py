class Family():
    def __init__(self, spouce=None, kids=None, parents=None):
        self.spouce = spouce
        self.kids = kids if kids is not None else []
        self.parents = parents if parents is not None else []