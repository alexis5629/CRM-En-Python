#Importaciones.
from re import X
from turtle import clear
import pandas as pd
import numpy as np
import os

# Definir función para limpiar la consola.
clear_output = lambda: os.system('cls')

#Definir menú principal
def menu():
    print("========================")
    print()
    print("Seleccione una opción:")
    print()
    print("(1) Clientes.")
    print("(2) Productos.")
    print("(3) Notas.")
    print("(4) Finalizar.")  
    print()
    print("========================")

    #Valor de entrada.
    x = int(input("Ingresa el numero de la opcion que deseas: "))

    #Procedimiento Opción 1
    if x == 1: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Clientes")
      print()
      print("(1) Consultar lista de clientes.")
      print("(2) Agregar un cliente.")
      print("(3) Regresar al menú principal.")
      print()
      print("========================")
      # Valor de entrada Opción 1 > Menú 2
      MenuOp1 = int(input("Elije una opción: "))
      #Clientes > Leer base de datos
      if MenuOp1 == 1:
        clear_output()
        tabla_clientes = pd.read_csv('clientes.csv')
        print(tabla_clientes)
        print()
        menu()    
      #Clientes > Agregar nuevo cliente
      elif MenuOp1 == 2: 
        clear_output()
        print("========================")
        print()
        print("(+) Porfavor Ingresa los siguientes datos.")
        name = input("Nombre del cliente: ")
        date = input("Fecha de registro del cliente: ")
        id = input("Clave que le quieres asignar al cliente: ")
        mail = input("Correo electrónico del cliente: ")
        clientes = {'Nombre':[name],
                    'Fecha_de_registro':[date],
                    'Clave':[id],
                    'Correo':[mail],
        }
        clear_output()
        print("Se registrara el cliente con los siguientes datos:  ", clientes)
        print()
        print("Para confirmar pulse 1, para cancelar pulse 2")
        #Confirmar Registro cliente.
        MenuConfirmar = int(input("Confirmar? "))
        #Confirmar, adjuntar cliente a base de datos.
        if MenuConfirmar == 1:
          clear_output()
          print(clientes)
          print()
          myDS1 = pd.DataFrame(clientes)
          print(myDS1)
          myDS1.to_csv('clientes.csv')
          print()
          print("Los Datos han sido almacenados existosamente!")
          print()
          menu()
        #Rechazar, borrar datos de registro.
        elif MenuConfirmar == 2: 
          clear_output()
          clientes = {}
          menu()
        #Opción no válida.
        else:
          clear_output()
          print("Opción no valida, volviendo al menú principal")
          menu()

      #Clientes > Regresar al menú principal
      elif MenuOp1 == 3:
        clear_output()
        menu ()          

    #Procedimiento Opción 2
    elif x == 2: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Productos")
      print()
      print("(1) Consultar Productos.")
      print("(2) Agregar un producto.")
      print("(3) Regresar al menú principal.")
      print()
      print("========================")
      # Valor de entrada Opción 2 > Menú 2
      MenuOp2 = int(input("Elije una opción: "))
      #Productos > Leer Base de datos
      if MenuOp2 == 1:
        clear_output()
        tabla_productos = pd.read_csv('productos.csv')
        print(tabla_productos)
        print("")
        menu()
      #Productos > Agregar nota a la base
      elif MenuOp2 == 2: 
        clear_output()
        print("(+) Porfavor completa los siguientes datos.")
        name = input("Ingresa el nombre del producto: ")
        id = input("Ingresa la clave del producto: ")
        price = int(input("Ingresa el precio unitario del producto: "))      
        desc = input("Ingresa una breve descripcion del producto: ")
        productos = {'Nombre_producto':[name],
                     'Clave_producto':[id],
                     'Precio_prodcuto':[price],
                     'Descripcion':[desc]
      }
        clear_output()

        print("Se registrara el cliente con los siguientes datos:  ", productos)
        print()
        print("Para confirmar pulse 1, para cancelar pulse 2")
        #Confirmar Registro nota.
        MenuConfirmar = int(input("Confirmar? "))
        #Confirmar, adjuntar cliente a base de datos.
        if MenuConfirmar == 1:
          clear_output()
          print(productos)
          print()
          myDS2 = pd.DataFrame(productos)
          print(myDS2)
          myDS2.to_csv('productos.csv')
          print()
          print("Los Datos han sido almacenados existosamente!")
          print()
          menu()
        #Rechazar, borrar datos de registro.
        elif MenuConfirmar == 2: 
          clear_output()
          productos = {}
          menu()
        #Opción no válida.
        else:
          clear_output()
          print("Opción no valida, volviendo al menú principal")
          menu()
       
      #Productos > Volver al menú principal
      elif MenuOp2 == 3: 
        clear_output()
        menu() 
      #Productos > Opción no válida
      else:
        clear_output()
        print("Opción no valida, volviendo al menú principal")
        menu()

    #Procedimiento Opción 3
    elif x == 3: 
      clear_output()
      print("========================")
      print()
      print("Inicio > Notas")
      print()
      print("(1) Consultar notas.")
      print("(2) Agregar una nota.")
      print("(3) Regresar al menú principal.")
      print()
      print("========================")
      # Valor de entrada Opción 1 > Menú 3
      MenuOp3 = int(input("Elije una opción: "))
      # Notas > Mostrar base de datos
      if MenuOp3 == 1: 
        clear_output()
        print("Te mostraremos las notas registradas")
        tabla_notas = pd.read_csv('notas.csv')
        print()
        print(tabla_notas)
        print()
        menu()
      #Notas > Crear nueva nota
      elif MenuOp3 == 2:
          print("(+) Porfavor completa los siguientes datos.")  
          name = input("Nombre del cliente: ")
          clv = input("Clave del articulo: ")
          art = int(input("Numero de articulos comprados: "))
          if art < 0:
            print("Error, no se aceptan numeros negativos.")
            print()
            print("Regresando al menú principal.")
            menu()
          prc = int(input("Precio por unidad del producto comprado: "))
          if prc < 0:
            print("Error, no se aceptan numeros negativos.")
            print()
            print("Regresando al menú principal.")
            menu()
          totalp = prc * art
          notas = {'Nota':[name],
                     'Numero_de_articulos':[art],
                     'Clave_articulo':[clv],
                     'Precio_unitario':[prc],
                     'Precio_total':[totalp]
            }
          clear_output()
          print("El total a pagar es $", totalp)
          print("Se registrara la nota con los siguientes datos:  ", notas)
          print()
          print("Para confirmar pulse 1, para cancelar pulse 2")
        #Confirmar Registro nota.
          MenuConfirmar = int(input("Confirmar?: "))
        #Confirmar, adjuntar cliente a base de datos.
          if MenuConfirmar == 1:
            clear_output()
            print()
            myDS3 = pd.DataFrame(notas)
            myDS3.to_csv('notas.csv')
            print()
            print("Los Datos han sido almacenados existosamente!")
            print()
            menu()
          #Rechazar, borrar datos de registro.
          elif MenuConfirmar == 2: 
            clear_output()
            Notas = {}
            menu()
          #Opción no válida.
          else:
            clear_output()
            print("Opción no valida, volviendo al menú principal")
            menu()

      #Notas > Regresar al Menú principal
      elif MenuOp3 == 3:  
        clear_output()
        menu() 

      #Notas > Opción invalida
      else:
        clear_output()
        print("Opción no valida, volviendo al menú principal")
        print()
        menu()

    #Procedimiento Opción 4
    elif x == 4: 
      clear_output()
      print("========================")
      print()
      print("Gracias por utilizar este sistema.")
      print("Que tengas buen día :)")
      print()
      print("========================")

    #Procedimiento Opción No Valida.
    else:
      print()
      print("ERROR:")
      print("Opción no valida, escoge entre 1 y 4")
      print()
      menu ()

#Invocar Función
menu()