#Examen de Programación de Gabriel Molina --- Sistema banco internacional

#Importar Librerías
import random
import csv
from statistics import geometric_mean
#Creación de listas y diccionarios de datos
Clientes = []
Clientes_Saldos = {}
Cla_Alto = {}
Cla_Medio = {}
Cla_Bajo = {}

#Codigo fuente de menu
while True:
    print("Bienvenido al Banco Internacional, ¿Que desearia revisar?")
    print("1. Añadir clientes")
    print("2. Clasificar saldos")
    print("3. Ver estadisticas")
    print("4. Actualizar datos CSV")
    print("5. Salir del sistema")
    menu = int(input())
    
    if menu == 5:
        
        print("Hasta pronto, gracias por elegirnos")
        print("Realizado por: Gabriel Molina")
        print("21.612.384-0")
        break
    if menu > 5 or menu < 1:
        
        print("Porfavor, ingrese una opción que sea valida") 
        # Asignar el nombre de los clientes
    if menu == 1:
       for i in range (1,11):
            Nombre = str(input(f"Ingrese el nombre del usuario: {i}: "))
            Clientes.append(Nombre)
       print("Usuarios asignados")           
       for a in Clientes:
            Clientes_Saldos[a] = random.randint(10000, 90000)     
    if menu == 2:
        
        for clave, valor in Clientes_Saldos.items():
            
            if valor >= 80000:
                print(f"El cliente {clave} tiene un saldo alto de: {valor}")
                Cla_Alto[clave] = valor
                
            if valor <= 70000 and valor >= 30000: 
                print(f"El cliente {clave} tiene un saldo medio de: {valor}")
                Cla_Medio[clave] = valor
            
            if valor >= 0 and valor < 30000:
                print(f"El cliente {clave} tiene un saldo bajo de: {valor}")
                Cla_Bajo[clave] = valor
            
                
    if menu == 3:
        # Datos de los saldos mas alto y bajo de los clientes
         num_mayor = max(Clientes_Saldos.values())
         num_menor = min(Clientes_Saldos.values())
        
       
         obtener_saldos = list(Clientes_Saldos.values())
        
         promedio = round( sum(obtener_saldos) / len(obtener_saldos) )
         media_geometrica = geometric_mean(obtener_saldos)
         
         
         print(f"El saldo más alto es de: {num_mayor}")
         print(f"El saldo más bajo es de: {num_menor}")
         print(f"El promedio de todos los saldos es de: {promedio}")
         print(f"La media geometrica es de: {media_geometrica}")
        
    if menu == 4:
         #En una variable, almacenamos los datos de clave y valor del diccionario
        items = Clientes_Saldos.items()
        
        with open('datos.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(items)
            
        print("Archivo CSV 'datos.csv' guardado correctamente")
        
       
       # Leemos el alchivo CSV 
        with open('datos.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)

        print("Contenido original del archivos CSV: ")
        for row in rows:
            print(row)
         
         
    
