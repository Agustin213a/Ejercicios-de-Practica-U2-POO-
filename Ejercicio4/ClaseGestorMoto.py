from ClaseMoto import Moto
import csv

class GestorMoto:
    __listaMoto: list

    def __init__(self):
        self.__listaMoto = []
    
    def testMoto(self):
        archivo= open("datosMotos.csv", mode= 'r')
        reader = csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unaMoto= Moto(fila[0], 
                          fila[1], 
                          fila[2], 
                          fila[3], 
                          int(fila[4]))
            self.__listaMoto.append(unaMoto)
        archivo.close()

    def mostrar_datos(self):
        for moto in self.__listaMoto:
            print(f"""
                DATOS
Patente: {moto.get_patente()}
Marca: {moto.get_marca()}
Nombre y Apellido: {moto.get_nombre()}{moto.get_apellido()}
Kilometraje: {moto.get_kilometraje()}""")
            
    def asignar_patente(self, patente):
        i=0
        while(i<len(self.__listaMoto) and self.__listaMoto[i].get_patente()!= patente):
            i+=1
        
        if(i<len(self.__listaMoto)):
            return 1
        else:
            return -1
    
    def mostrar_datos_conductor(self, patente):
        i=0
        while(i<len(self.__listaMoto) and self.__listaMoto[i].get_patente()!= patente):
            i+=1
        
        if(i<len(self.__listaMoto)):
            print(f"""
                DATOS
Patente: {self.__listaMoto[i].get_patente()}
Marca: {self.__listaMoto[i].get_marca()}
Nombre y Apellido: {self.__listaMoto[i].get_nombre()}{self.__listaMoto[i].get_apellido()}
Kilometraje: {self.__listaMoto[i].get_kilometraje()}""")
        else:
            print("No existe el conductor")
        
    def mostrar_lista(self, GP):
        for i in range(len(self.__listaMoto)):
            print(f"""
Patente de Moto: {self.__listaMoto[i].get_patente()}
Conductor {self.__listaMoto[i].get_nombre()}{self.__listaMoto[i].get_apellido()}

""")
            GP.listado2(self.__listaMoto[i].get_patente())
        
            