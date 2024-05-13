class equipo:
    __id: int
    __nombre: str
    __goles_favor: int
    __goles_contra: int
    __diferencia_goles: int
    __puntos: int

    def __init__(self, id: int, nombre: str, goles_favor: int, goles_contra: int, diferencia_goles: int, puntos: int):
        self.__id = id
        self.__nombre = nombre
        self.__goles_favor = goles_favor
        self.__goles_contra = goles_contra
        self.__diferencia_goles = diferencia_goles
        self.__puntos = puntos

    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_goles_favor(self):
        return self.__goles_favor
    
    def get_goles_contra(self):
        return self.__goles_contra
    
    def get_diferencia_goles(self):
        return self.__diferencia_goles
    
    def get_puntos(self):
        return self.__puntos
    
    def set_goles_favor(self, goles_favor: int):
        self.__goles_favor = goles_favor
    
    def set_goles_contra(self, goles_contra: int):
        self.__goles_contra = goles_contra
    
    def set_diferencia_goles(self, diferencia_goles: int):
        self.__diferencia_goles = diferencia_goles
    
    def set_puntos(self, puntos: int):
        self.__puntos+= puntos

    def __gt__(self, otro_equipo):
        if self.__puntos == otro_equipo.get_puntos():
            if self.__diferencia_goles == otro_equipo.get_diferencia_goles():
                return self.__goles_favor > otro_equipo.get_goles_favor()
            else:
                return self.__diferencia_goles > otro_equipo.get_diferencia_goles()
        else:
            return self.__puntos > otro_equipo.get_puntos()
