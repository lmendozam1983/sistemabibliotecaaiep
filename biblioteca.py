# Inicio de programa
print("Sistema Biblioteca Universidad Master Senior")
print("--------> BIENVENIDOS <---------")
print("--------------------------------")

# Función del menú
def menu():
    print("******* MENÚ DE OPCIONES *******")
    print("1. Registrar estudiante en Biblioteca")
    print("2. Estudiantes activos en Biblioteca")
    print("3. Desactivar estudiante de Biblioteca")
    print("4. Consultar si estudiante está en Biblioteca")
    print("5. Lista de ingresos")
    print("6. Créditos")
    print("7. Salir")
    opcion = int(input("Elige una opción: "))
    return opcion

# Listas vacías para almacenar datos
estudiante = []
rut = []
carrera = []

# Función ingreso de estudiante a Biblioteca
def registrar_estudiante(estudiante):
        nombre = input("Ingrese el nombre del estudiante: ")
        rut = input("Ingrese el rut del estudiante: ")
        carrera = input("Ingrese la carrera del alumno: ")
        estudiante.append({"nombre": nombre,"rut": rut,"carrera": carrera})
        print("********************************")
        print("Estudiante agregado/a a Biblioteca Master Senior")
        print("--------------------------------")
        print("Estudiante:", nombre, "/ Rut:", rut, "/ Carrera:", carrera)
        print("--------------------------------")

# Función lista de nombres de estudiante
def imprimir_nombres(lista):
    for nombre in lista:
        print("********************************")
        print("Ahora en Biblioteca")
        print("--------------------------------")
        print(nombre)
        print("--------------------------------")

# Función borrar estudiante de Biblioteca
def rut_borrar(estudiante):
        if not estudiante:
            print("No hay estudiantes registrados.")
        else:
            rut_borrar = input("Ingrese el rut del estudiante a eliminar: ")
            encontrado = False

        for i in estudiante:
            if str(i["rut"]) == rut_borrar:  
                estudiante.remove(i)
                print("--------------------------------")
                print(f"Estudiante {rut_borrar} eliminado correctamente.")
                print("--------------------------------")
                encontrado = True
                break

        if not encontrado:
            print(f"No se encontró un estudiante con RUT {rut_borrar}.")
            print("--------------------------------")     

# Función consulta de nombres en Biblioteca
def consulta_estudiante(estudiantes):   # recibe la lista
    rut_consulta = input("Ingrese rut a consultar: ").strip()
    encontrado = False

    for i in estudiantes:
        if str(i["rut"]).strip() == rut_consulta:
            print("********************************")
            print("Estudiante activo/a en Biblioteca")
            print("--------------------------------")
            print(f"Nombre: {i['nombre']}")
            print("--------------------------------")
            encontrado = True
            break

    if not encontrado:
        print("No se encontró un estudiante con ese RUT.")

# Función créditos
def creditos():
    print("********************************")
    print("Grupo 2")
    print("Alumnos: Cristóbal Hernández, Luis Mendoza Moraga")
    print("Docente: Leonardo Soto Cárdenas")
    print("Carrera: Ánalisis y programación Computacional")
    print("Módulo: Fundamento de programación Computacional")
    print("--------------------------------")

# Función salir
def salir():
    print("--------------------------------")
    print("""Muchas gracias por usar AT&T

     /\_/\  
    ( o.o ) 
     > ^ < 
""")
    print("--------------------------------")
    
# Menú de opciones
while True:
    opcion = menu()

    if opcion == 1:
        registrar_estudiante(estudiante)

    elif opcion == 2:
        imprimir_nombres(estudiante)

    elif opcion == 3:
        rut_borrar(estudiante)
        
    elif opcion == 4:
        consulta_estudiante(estudiante)

    elif opcion == 5:
        print("--------------------------------")

    elif opcion == 6:
        creditos()

    elif opcion == 7:
        salir()
        break       

    else:
        print("Opción no válida, intente nuevamente.")








