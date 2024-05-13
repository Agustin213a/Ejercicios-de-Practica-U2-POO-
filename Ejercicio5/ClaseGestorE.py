from ClaseEquipo import equipo
import csv

class Gestorequipo:
    __listaEquipo: list

    def __init__(self):
        self.__listaEquipo = []

    def agregarEquipo(self, unEquipo):
        self.__listaEquipo.append(unEquipo)
    
    def testEquipo(self):
        archivo= open("equipos2024.csv", mode= 'r')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unEquipo= equipo(int(fila[0]), fila[1], int(fila[2]), int(fila[3]), int(fila[4]), int(fila[5]))
            self.__listaEquipo.append(unEquipo)
        archivo.close()
    
    def mostrarEquipos(self):
        print("ID       NOMBRE       GOLES FAVOR       GOLES CONTRA       DIFERENCIA DE GOLES       PUNTOS       PUNTOS")
        for i in self.__listaEquipo:
            print(f"""
{i.get_id()}       {i.get_nombre()}           {i.get_goles_favor()}          {i.get_goles_contra()}          {i.get_diferencia_goles()}          {i.get_puntos()}         {i.get_puntos()}""")
            
    def agregarEquipos(self):
        print("         Carga de datos")
        id= int("ID: ")
        nombre= str("Nombre: ")
        goles_favor= int("Goles favor: ")
        goles_contra= int("Goles contra: ")
        diferencia_goles= int("Diferencia de goles: ")
        puntos= int("Puntos: ")
        unEquipo= equipo(id, nombre, goles_favor, goles_contra, diferencia_goles, puntos)
        self.__listaEquipo.append(unEquipo)
        print("Equipo agregado")

    def buscar_ID(self, equipo):
        i=0
        while(i<len(self.__listaEquipo) and self.__listaEquipo[i].get_nombre()!=equipo):
            i+=1
        
        if(i<len(self.__listaEquipo)):
            print(f"Nombre: {equipo}")
            return self.__listaEquipo[i].get_id()
        else:
            return -1
        
    def actualiza(self, idlocal, idvisitante, goles_local, goles_visitante, dif, puntos):
        for eq in self.__listaEquipo:
            if(eq.get_id()==idlocal):
                eq.set_goles_favor(goles_local)
                eq.set_goles_contra(goles_visitante)
                eq.set_diferencia_goles(dif)
                eq.set_puntos(puntos)
            elif(eq.get_id()==idvisitante):
                eq.set_goles_favor(goles_visitante)
                eq.set_goles_contra(goles_local)
                eq.set_diferencia_goles(dif)
                eq.set_puntos(puntos)
    
    def ordena(self):
        self.__listaEquipo= sorted(self.__listaEquipo)
        print("Ordenado")

    def guardar_datos(self):
        archivo= open("equipos.csv","w")
        writer= csv.writer(archivo, delimiter= ';')
        listalocal= []
        for eq in self.__listaEquipo:
            equipox= []
            equipox.append(eq.get_id())
            equipox.append(eq.get_nombre())
            equipox.append(eq.get_goles_favor())
            equipox.append(eq.get_goles_contra())
            equipox.append(eq.get_diferencia_goles())
            equipox.append(eq.get_puntos())
            listalocal.append(equipox)
        for fila in listalocal:
            writer.writerow(fila)
        archivo.close()
