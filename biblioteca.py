# Inicio de programa
print("Sistema Biblioteca Mastersystem/ Grupo 2")
print("------>BIENVENIDOS<-------")
print("--------------------------------")

# Función del menú
def menu():
    print("******* MENÚ DE OPCIONES *******")
    print("1. Registrar estudiante en biblioteca")
    print("2. Estudiante activos en Biblioteca")
    print("3. Desactivar estudiante de Biblioteca")
    print("4. Consulta de estudiante")
    print("5. Lista de ingresos")
    print("6. Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

# Función lista de nombres de estudiante
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)


# Listas vacías para almacenar nombres
estudiante = []
rut = []
carrera = []


# Menú de opciones
while True:
    opcion = menu()

    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        rut = int(input("Ingrese el rut del estudiante: "))
        carrera = input("Ingrese la carrera del alumno: ")
        estudiante.append({"nombre": nombre,"rut": rut,"carrera": carrera})
        print("--------------------------------")
        print("Estudiante:", nombre, "- Rut:", rut, "- Carrera:", carrera)
        print("--------------------------------")

    elif opcion == 2:
        print("Estudiantes activos")
        print("--------------------------------")
        imprimir_nombres(estudiante)
        print("--------------------------------")

    elif opcion == 3:
        if not estudiante:
            print("No hay estudiantes registrados.")
        else:
            nombre_borrar = input("Ingrese el nombre del estudiante a eliminar: ")
            encontrado = False

        for est in estudiante:
            if est["nombre"].lower() == nombre_borrar.lower():  
                estudiante.remove(est)
                print(f"Estudiante {nombre_borrar} eliminado correctamente.")
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un estudiante con ese nombre.")


        print("--------------------------------")
        
    elif opcion == 4:
        print("--------------------------------")

    elif opcion == 5:
        print("--------------------------------")

    elif opcion == 6:
        print("--------------------------------")
        print('Muchas gracias por usar AT&T')
        print("--------------------------------")
        menu = False

    else:
        print("Opción no válida, intente nuevamente.")








