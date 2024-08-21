# Lista global que almacenará los estudiantes registrados
estudiantes = []

def menu():
    print("\nBienvenido al Sistema de Registro de Matrículas")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_estudiante():
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estudiante = {'nombre': nombre, 'edad': edad}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")
    
def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes registrados:")
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")

def actualizar_estudiante():
    print("Estudiantes registrados:")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i + 1}. {estudiante['nombre']} - {estudiante['edad']}")
        
    while True:
        try:
            indice = int(input("Ingresa el número del estudiante que deseas actualizar: ")) - 1
            if 0 <= indice < len(estudiantes):
                break
            else:
                print("Índice fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")
    
    estudiante = estudiantes[indice]
    print(f"Estudiante seleccionado: {estudiante['nombre']} - {estudiante['edad']}")
    
    nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
    nueva_edad = input("Ingresa la nueva edad (o presiona Enter para no cambiarla): ")

    # Solo actualizamos si el usuario ingresó nuevos valores
    if nuevo_nombre:
        estudiante['nombre'] = nuevo_nombre
    if nueva_edad:
        try:
            estudiante['edad'] = int(nueva_edad)
        except ValueError:
            print("Entrada inválida para la edad. No se realizó ningún cambio en la edad.")

    print(f"Estudiante en el índice {indice + 1} actualizado con éxito.")
    
def eliminar_estudiante():
    print("Estudiantes registrados:")
    for i, estudiante in enumerate(estudiantes):
        print(f"{i + 1}. {estudiante['nombre']} - {estudiante['edad']}")

    while True:
        try:
            indice = int(input("Ingresa el número del estudiante que deseas eliminar: ")) - 1
            if 0 <= indice < len(estudiantes):
                break
            else:
                print("Índice fuera de rango. Intenta de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número entero.")

    estudiante = estudiantes[indice]
    estudiantes.pop(indice)
    print(f"Estudiante {estudiante['nombre']} eliminado con éxito.")


    
def main():
 
    while True:
        opcion = menu()
        if opcion == '1':
            registrar_estudiante()
        elif opcion == '2':
            mostrar_estudiantes()
        elif opcion == '3':
            actualizar_estudiante()
        elif opcion == '4':
            eliminar_estudiante()
        elif opcion == '5':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, por favor intenta de nuevo.")

# Ejecutamos la función principal para iniciar el programa
main()
        