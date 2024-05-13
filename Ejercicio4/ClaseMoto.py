class Moto:
    __patente: str
    __marca: str
    __nombre: str  
    __apellido: str 
    __kilometraje: int

    def __init__(self, patente: str, marca: str, nombre: str, apellido: str, kilometraje: int):
        self.__patente = patente
        self.__marca = marca
        self.__nombre = nombre
        self.__apellido = apellido
        self.__kilometraje = kilometraje
    
    def get_patente(self):
        return self.__patente
    
    def get_marca(self):
        return self.__marca

    def get_nombre(self):
        return self.__nombre
    
    def get_apellido(self):
        return self.__apellido
    
    def get_kilometraje(self):
        return self.__kilometraje
    