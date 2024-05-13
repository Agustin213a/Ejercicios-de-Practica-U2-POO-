from ClaseGestorMoto import GestorMoto
from ClaseGestorPedido import GestorPedido

def menu():
    op= int(input("""
                MENU DE OPCIONES
[1] Mostrar datos del Gestor de Motos
[2] Mostrar datos del Gestor de Pedidos
[3] Cargar nuevos pedidos asignando una moto a ese pedido
[4] Modificar el tiempo real de un pedido
[5] Leer por una patente de una moto, mostrar los datos del conductor y el tiempo promedio 
real de entrega de los pedidos que hizo
[6] Generar un listado para cada moto, para el pago de comisiones a los conductores de las 
motos
[0] Salir
        ---> """))
    return op

if __name__ == "__main__":
    GM= GestorMoto()
    GP= GestorPedido()
    GM.testMoto()
    GP.testPedido()
    GP.ordenar_por_patente()
    op= menu()
    while op!= 0:
        if op == 1:
            GM.mostrar_datos()
        elif op == 2:
            GP.mostrar_pedidos()
        elif op == 3:
            patente= input("Ingrese la patente de la moto: ")
            c=GM.asignar_patente(patente)
            if(c!=-1): #La moto existe
                GP.nuevosPedidos(patente)
            else: 
                print("No existe esa matricula")
        elif op == 4:
            patente= input("Ingrese la patente de la moto: ")
            id= int(input("Ingrese el id del pedido: "))
            tiempo= int(input("Ingrese el tiempo real de entrega: "))
            GP.modificar_tiempo(patente,id,tiempo)
        elif op == 5:
            patente= input("Ingrese la patente de la moto: ")
            GM.mostrar_datos_conductor(patente)
            GP.mostrar_pedidos_conductor(patente)
        elif op == 6:
            GM.mostrar_lista(GP)
        op= menu()