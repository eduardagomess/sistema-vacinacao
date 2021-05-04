class Controlador:
    __instancia = None

    def __init__(self, atributo_objeto: str):
        self.__atributo_objeto = atributo_objeto

    def __new__(cls, *args, **kwargs):
        if Controlador.__instancia is None:
            Controlador.__instancia = object.__new__(cls)
        return Controlador.__instancia
