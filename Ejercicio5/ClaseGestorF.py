from ClaseFecha import fecha
import csv

class Gestorfecha:
    __listaFecha: list

    def __init__(self):
        self.__listaFecha = []
    
    def agregarFecha(self, unaFecha):
        self.__listaFecha.append(unaFecha)
    
    def testFecha(self):
        archivo= open("fechasFutbol.csv", mode= 'r')
        reader= csv.reader(archivo, delimiter= ';')
        next(reader)
        for fila in reader:
            unaFecha= fecha(fila[0], int(fila[1]), int(fila[2]), int(fila[3]), int(fila[4]))
            self.__listaFecha.append(unaFecha)
        archivo.close()

    def mostrarFechas(self):
        print("Fecha     ID Local       ID Visitante        Goles de local      Goles de visitante")
        for i in self.__listaFecha:
            print(f"""
{i.get_fecha()}     {i.get_equipo_local()}       {i.get_equipo_visitante()}       {i.get_goles_local()}       {i.get_goles_visitante()}""")
            
    def agregarFechas(self):
        print("         Carga de datos")
        fecha= input("Fecha: ")
        equipo_local= int(input("Equipo local: "))
        equipo_visitante= int(input("Equipo visitante: "))
        goles_local= int(input("Goles de local: "))
        goles_visitante= int(input("Goles de visitante: "))
        unaFecha= fecha(fecha, equipo_local, equipo_visitante, goles_local, goles_visitante)
        self.__listaFecha.append(unaFecha)
        print("Fecha Cargada!")
    
    def mostrar_Datos(self, id):
        print("Fecha  Goles a Favor  Goles en Contra Diferencia de Goles Puntos")
        puntos= 0
        for lista in self.__listaFecha:
            if lista.get_equipo_local()== id:
                fecha= lista.get_fecha()
                goles_local= lista.get_goles_local()
                goles_visitante= lista.get_goles_visitante()
                dif= goles_local - goles_visitante
                if(dif>0):
                    puntos+= 3
                elif(dif<0):
                    puntos+= 0
                elif(dif==0):
                    puntos+= 1
                print(f"""
{fecha}     {goles_local}   {goles_visitante}   {dif}   {puntos}""")
            elif lista.get_equipo_visitante()== id:
                fecha= lista.get_fecha()
                goles_local= lista.get_goles_local()
                goles_visitante= lista.get_goles_visitante()
                dif= goles_local - goles_visitante
                if(dif>0):
                    puntos+= 3
                elif(dif<0):
                    puntos+= 0
                elif(dif==0):
                    puntos+= 1
                print(f"""
{fecha}     {goles_visitante}   {goles_local}   {dif}   {puntos}""")
                
    def actualizar_datos(self, GE):
        puntos=0
        for lista in self.__listaFecha:
            idlocal= lista.get_equipo_local()
            idvisitante= lista.get_equipo_visitante()
            goles_local= lista.get_goles_local()
            goles_visitante= lista.get_goles_visitante()
            dif= goles_local - goles_visitante
            if(dif>0):
                puntos+= 3
            elif(dif<0):
                puntos+= 0
            elif(dif==0):
                puntos+= 1
            GE.actualiza(idlocal, idvisitante, goles_local, goles_visitante, dif, puntos)
        
                

