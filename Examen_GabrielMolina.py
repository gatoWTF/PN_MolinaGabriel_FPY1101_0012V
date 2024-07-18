# Examen Transversal Gabriel Molina --- Sistema de Banco Internacional
import random
import csv
from statistics import geometric_mean

# Importe de librerias y diccionarios de datos
Clientes = []
Saldo_Max = {}
Saldo_Medium = {}
Saldo_Min = {}
Saldo_CLientes = {}

# Codigo fuente de menu del banco
while True:
    print("Banco internacional, ¿que desea realizar?")
    print("1. Añadir clientes")
    print("2. Mostrar saldos")
    print("3. Clasificar saldos")
    print("4. Aplicar seguro de salud y AFP")
    print("5. Actualizar datos CSV")
    print("6. Salir del sistema")
    menu = int(input())

    if menu > 6 or menu < 1:
        print("Por favor, ingrese una opcion valida")

    if menu == 6:
        print("Gracias por elegirnos, tenga un buen dia")
        print("Realizado por: Gabriel Molina")
        print("21.612.384-0")
        break
    
    
    # Asignacion de clientes 
    if menu == 1:
        for i in range (1,11):
            i = input("Ingrese el nombre del cliente:")
        print("¡Clientes asignados correctamente!")
        for a in Clientes:
            Saldo_CLientes[a] = random.randint(10000, 90000)
    if menu == 2:
    
      for clave, valor in Saldo_CLientes.items():
            
         if valor >= 80000:
            print(f"El cliente {clave} tiene un saldo alto de: {valor}")
            Saldo_Max[clave] = valor
                
         if valor <= 50000 and valor >= 20000: 
            print(f"El cliente {clave} tiene un saldo medio de: {valor}")
            Saldo_Medium[clave] = valor
            
         if valor >= 0 and valor < 20000:
            print(f"El cliente {clave} tiene un saldo bajo de: {valor}")
            Saldo_Min[clave] = valor
    if menu == 3:
         num_mayor = max(Saldo_CLientes.values())
         num_menor = min(Saldo_CLientes.values())
        
       
         obtener_saldos = list(Saldo_CLientes.values())
        
         promedio = round( sum(obtener_saldos) / len(obtener_saldos) )
         media_geometrica = geometric_mean(obtener_saldos)
         
         
         print(f"El saldo más alto es de: {num_mayor}")
         print(f"El saldo más bajo es de: {num_menor}")
         print(f"El promedio de todos los saldos es de: {promedio}")
         print(f"La media geometrica es de: {media_geometrica}")
