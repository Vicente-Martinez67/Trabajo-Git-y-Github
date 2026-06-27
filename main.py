#Evidencia N°1: Creacion del ejercicio para trabajo.


#Evidencia N°2: Creacion del menu principal , Opciones de salida y validación basica de opciones de menu.
#Creacion de lista para hacer una lista de diccionario.
tareas=[]

#Creacion funcion con menu:
#Creacion de dos nuevas opciones que son 3.-: Marcar tareas como completadas y la otra opcion #4.-: Actualizar Tareas
def menu():
    print("===MENU===")
    print("1.-: Agregar Tarea")
    print("2.-: Listar Tareas")
    print("3.-: Marcar tareas como completadas")
    print("4.-: Actualizar Tareas")
    print("5.-: Eliminar Tarea")
    print("6.-: Salir")

# Función que solicita ingresar opcion  y valida la opción ingresada:
def op():
    while True:
        try:
            op=int(input("Ingrese una opcion: "))

            if op <1:
                print("Debe ingresar un numero entero.")
            elif op <1 or op >6:
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
        "Tarea":tareaAgregar,
        "Estado":"Pendiente"
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



#Creacion de funcion de completar tarea con su respectiva validacion
def completarTarea():
    nombreTarea=input("Ingrese el nombre de la tarea a marcar como completada: ")
    
    encontrada = False

    for tarea in tareas:
        if tarea["Tarea"].lower() == nombreTarea.lower():
            encontrada = True
            tarea["Estado"] = "completado"
            print("Tarea marcada como completada.")
            return nombreTarea
    print("Tarea no encontrada")




#Creacion de funcion de actualizar estado de la tarea con su respectiva validacion
def actualizarEstado():
    nombreEstado=input("Ingrese el nombre de la tarea: ")

    for tarea in tareas:
        if tarea["Tarea"].lower() == nombreEstado.lower():
            nuevo_estado = input("Nuevo estado (Pendiente/Completada): ")

            if nuevo_estado.lower() in ["pendiente", "completada"]:
                tarea["Estado"]=nuevo_estado
                print("Estado actualizado")
            else:
                print("Estado invalido")
            return  
    print("Tarea no encontrada")




#Creacion de funcion para eliminar Tarea con su respectiva validacion
def eliminarTarea():
    if len(tareas)==0:
       print("No hay tareas registradas")
       return
    tareaEliminar=input("Ingrese tarea a eliminar.")
   
    for tarea in tareas:
       
       if tareaEliminar == tarea["Tarea"]:
           tareas.remove(tarea)

           print("Tarea eliminada exitosamente")
           return
    
    print("La tarea no existe")





#Main- Programa principal
while True:
    menu()
    opcion =op()
#Agregue las funciones hechas en las opciones.
#Agregue dos nuevas opciones en el main que son la de completarTarea y la de actualizarEstado
#Agregue nueva opcion para eliminar la tarea
    if opcion==1:
        agregarTarea()
    elif opcion==2:
        listarTareas()
    elif opcion ==3:
        completarTarea()
    elif opcion ==4:
        actualizarEstado()
    elif opcion==5:
        eliminarTarea()
    elif opcion ==6:
        print("¡Gracias por usar el programa!.")
        print("Saliendo........")
        break 
       
        