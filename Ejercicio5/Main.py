from ClaseGestorE import Gestorequipo
from ClaseGestorF import Gestorfecha

def menu():
    op= int(input("""
                MENU DE OPCIONES
[1] Mostrar datos del Gestor de Equipo
[2] Mostrar datos del Gestor de Fechas
[3] Agregar datos al Gestor de Equipos
[4] Agregar datos al Gestor de Fechas
[5] Ingresar el nombre de un equipo y obtener un listado de sus datos
[6] Actualizar la tabla de todos los equipos, con los resultados de las fechas disputadas. 
[7] Ordenar la lista
[8] Almacenar la tabla en un archivo csv
[0] Salir
            ---> """))
    return op

if __name__ == "__main__":
    GE = Gestorequipo()
    GF = Gestorfecha()
    GE.testEquipo()
    GF.testFecha()
    op=menu()
    while op!=0:
        if op==1:
            GE.mostrarEquipos()
        elif op==2:
            GF.mostrarFechas()
        elif op==3:
            GE.agregarEquipos()
        elif op==4:
            GF.agregarFechas()
        elif op==5:
            equipo= input("Ingrese equipo a buscar: ")
            id= GE.buscar_ID(equipo)
            if id:
                GF.mostrar_Datos(id)
            else:
                print("No se encontro el equipo")
        elif op==6:
            GF.actualizar_datos(GE)
            GE.mostrarEquipos()
        elif op==7:
            GE.ordena()
            GE.mostrarEquipos()
        elif op==8:
            GE.guardar_datos()
        else:
            print("Opcion no valida")
        op=menu()