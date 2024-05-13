from ClasePedido import Pedido
import csv

class GestorPedido:
    __listaPedidos: list

    def __init__(self):
        self.__listaPedidos = []
    
    def cargar(self, unPedido):
        self.__listaPedidos.append(unPedido)

    def testPedido(self):
        archivo= open("datosPedidos.csv", mode= 'r')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unPedido= Pedido(fila[0], int(fila[1]), fila[2], float(fila[3]), float(fila[4]), float(fila[5]))
            self.cargar(unPedido)
        archivo.close()

    def mostrar_pedidos(self):
        for pedido in self.__listaPedidos:
            print(f"""
            DATOS DE PEDIDOS
Patente: {pedido.get_patente()}
ID: {pedido.get_id()}
Comida: {pedido.get_comida()}
Tiempo Estimado: {pedido.get_tiempo_estimado()}
Tiempo Real: {pedido.get_tiempo_real()}
Precio: {pedido.get_precio()}
""")
    
    def nuevosPedidos(self, patente):
        print("DATOS")
        id= int(input("ID: "))
        comida= input("Comida: ")
        TE= float(input("Tiempo Estimado: "))
        TR= float(input("Tiempo Real: "))
        precio= float(input("Precio: "))
        unPedido= Pedido(patente, id, comida, TE, TR, precio)
        self.cargar(unPedido)
        print("Pedido creado")
    
    def modificar_tiempo(self, patente, id, tiempo):
        i=0
        while(i<len(self.__listaPedidos) and self.__listaPedidos[i].get_patente()!= patente):
            i+=1

        if i<len(self.__listaPedidos):
            self.__listaPedidos[i].set_tiempo_real(tiempo)
            print("Tiempo modificado")
        else:
            print("No se encontro el pedido")

    def mostrar_pedidos_conductor(self, patente):
        acum= 0
        cont=0
        for i in range(len(self.__listaPedidos)):
            if self.__listaPedidos[i].get_patente() == patente:
                acum+= self.__listaPedidos[i].get_tiempo_real()
                cont+=1
        
        print(f"Tiempo total: {acum}")
        print(f"Numero de pedidos: {cont}")
        print(f"Tiempo rel promedio: {acum/cont}")
    
    def listado2(self, patente):
        print("Identificador de pedido      Tiempo estimado     Tiempo real     Precio ")
        for i in range(len(self.__listaPedidos)):
            if self.__listaPedidos[i].get_patente() == patente:
                print(f"{self.__listaPedidos[i].get_id()}      {self.__listaPedidos[i].get_tiempo_estimado()}      {self.__listaPedidos[i].get_tiempo_real()}      {self.__listaPedidos[i].get_precio()}")
            
        
    def ordenar_por_patente(self):
        self.__listaPedidos= sorted(self.__listaPedidos)
        print(type(self.__listaPedidos))
