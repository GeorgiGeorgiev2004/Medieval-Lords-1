class BadAnswerError(Exception):
    def __init__(self, message='Sorry brother no found corresponding input apparently ?!?'):
        self._message = message
        super().__init__(self._message)


class NoFreeSlotsToBuildIn(Exception):
    def __init__(self, message="All city slots are full! Demolish a building or expand the city!"):
        self._message = message
        super().__init__(self._message)


class YokParichok(Exception):
    def __init__(self, message="Seems like the coffers are running a little thin."):
        self._message = message
        super().__init__(self._message)
