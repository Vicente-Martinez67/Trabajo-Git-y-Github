#Evidencia N°1: Creacion del ejercicio para trabajo.


#Evidencia N°2: Creacion del menu principal , Opciones de salida y validación basica de opciones de menu.


#Creacion funcion con menu:
def menu():
    print("===MENU===")
    print("1.-: Agregar Tarea")
    print("2.-: Listar Tareas")
    print("3.-: Salir")

# Función que solicita ingresar opcion  y valida la opción ingresada:
def op():
    while True:
        try:
            op=int(input("Ingrese una opcion: "))

            if op <1:
                print("Debe ingresar un numero entero.")
            elif op <1 or op >3:
                print("Debe escoger una opcion que este entre 1 a 3.")
            else:
                return op
        except ValueError:
            print("Debe ingresar numeros.")




#Main- Programa principal
while True:
    menu()
    opcion =op()

    if opcion==1:
        pass
    elif opcion==2:
        pass
    elif opcion ==3:
        print("¡Gracias por usar el programa!.")
        print("Saliendo........")
        break