class AlreadyExistException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = args[0]
