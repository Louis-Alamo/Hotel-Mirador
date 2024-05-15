class EmptyFieldException(Exception):
    def __init__(self):
        super().__init__(f"Los campos no pueden estar vacíos")