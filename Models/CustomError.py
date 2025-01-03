class BadAnswerError(Exception):
    def __init__(self, message='Sorry brother no found corresponding input apparently ?!?'):
        self._message = message
        super().__init__(self._message)
