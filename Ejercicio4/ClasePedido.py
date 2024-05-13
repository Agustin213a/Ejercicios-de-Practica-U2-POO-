class Pedido:
    __patente: str
    __id: int
    __comida: str 
    __tiempo_estimado: float   
    __tiempo_real: float
    __precio: float

    def __init__(self, patente: str, id: int, comida: str, tiempo_estimado: float, tiempo_real: float, precio: float):
        self.__patente= patente
        self.__id= id
        self.__comida= comida
        self.__tiempo_estimado= tiempo_estimado
        self.__tiempo_real= tiempo_real
        self.__precio= precio
    
    def get_patente(self):
        return self.__patente

    def get_id(self):
        return self.__id
    
    def get_comida(self):
        return self.__comida
    
    def get_tiempo_estimado(self):
        return self.__tiempo_estimado
    
    def get_tiempo_real(self):
        return self.__tiempo_real
    
    def get_precio(self):
        return self.__precio
    
    def set_tiempo_real(self, tiempo):
        self.__tiempo_real= tiempo

    def __lt__(self, otroPedido):
        return self.__patente < otroPedido.get_patente()