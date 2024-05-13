class fecha:
    __fecha: str
    __id_local: int
    __id_visitante: int
    __goles_local: int
    __goles_visitante: int

    def __init__(self, fecha: str, id_local: int, id_visitante: int, goles_local: int, goles_visitante: int):
        self.__fecha = fecha
        self.__id_local = id_local
        self.__id_visitante = id_visitante
        self.__goles_local = goles_local
        self.__goles_visitante = goles_visitante
    
    def get_fecha(self):
        return self.__fecha
    
    def get_equipo_local(self):
        return self.__id_local
    
    def get_equipo_visitante(self):
        return self.__id_visitante
    
    def get_goles_local(self):
        return self.__goles_local
    
    def get_goles_visitante(self):
        return self.__goles_visitante