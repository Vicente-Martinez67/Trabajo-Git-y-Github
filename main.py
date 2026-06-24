#Evidencia N°1: Creacion del ejercicio para trabajo.


#Evidencia N°2: Creacion del menu principal , Opciones de salida y validación basica de opciones de menu.
#Creacion de lista para hacer una lista de diccionario.
tareas=[]

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


#Creacion de la funcion Agregar tareas y sus respectivas validaciones 
def agregarTarea():
    tareaAgregar=input("Ingrese el nombre de la tarea: ")

    if tareaAgregar.strip() == "":
        print("Este apartado no puede estar vacio y no puede estar en blanco.")
        return tareaAgregar
    
    nuevaTarea={
        "Tarea":tareaAgregar
    }

    tareas.append(nuevaTarea)
    print("tarea agregada con exito")


#Creacion de funcion para listar tareas usando ciclo for para recorrer el diccionario y mostrar la tarea listada.
def listarTareas():
    if len(tareas)==0:
        print("No hay tareas registradas")
        return
    
    for tarea in tareas:
        print("Tarea:",tarea["Tarea"])
        print("tarea listada.")
        print("==================================")






#Main- Programa principal
while True:
    menu()
    opcion =op()
#Agrege las funciones hechas en las opciones.
    if opcion==1:
        agregarTarea()
    elif opcion==2:
        listarTareas()
    elif opcion ==3:
        print("¡Gracias por usar el programa!.")
        print("Saliendo........")
        break