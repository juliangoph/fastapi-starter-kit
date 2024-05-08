class BaseCustomError(Exception):
    def __init__(self, msg: str = "", code: int = None):
        self.msg = msg
        self.code = code

    def __str__(self):
        return self.msg
