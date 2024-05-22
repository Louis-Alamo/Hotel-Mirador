class EmptyFieldException(Exception):
    def __init__(self, message="Los campos no pueden estar vacíos" ):
        super().__init__(message)