# Lista global que almacenará los estudiantes registrados
estudiantes = []

def menu():
    """
    Esta función muestra el menú principal del sistema.
    Permite al usuario seleccionar entre diferentes opciones.
    """
    print("\nBienvenido al Sistema de Registro de Matrículas")
    print("1. Registrar nuevo estudiante")
    print("2. Mostrar estudiantes registrados")
    print("3. Actualizar información de un estudiante")
    print("4. Eliminar un estudiante")
    print("5. Salir")
    opcion = input("Elige una opción (1/2/3/4/5): ")
    return opcion

def registrar_estudiante():
    """
    Esta función permite registrar un nuevo estudiante en el sistema.
    Pide al usuario ingresar el nombre y la edad del estudiante, y lo añade a la lista global 'estudiantes'.
    """
    nombre = input("Ingresa el nombre del estudiante: ")
    edad = int(input("Ingresa la edad del estudiante: "))
    estudiante = {'nombre': nombre, 'edad': edad}
    estudiantes.append(estudiante)
    print(f"Estudiante {nombre} registrado con éxito.")
    
def mostrar_estudiantes():
    """
    Esta función muestra la lista de estudiantes registrados.
    Si no hay estudiantes registrados, informa al usuario.
    """
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados.")
    else:
        print("Lista de estudiantes registrados:")
        for i, estudiante in enumerate(estudiantes, start=1):
            print(f"{i}. Nombre: {estudiante['nombre']}, Edad: {estudiante['edad']}")
            
def actualizar_estudiante():
    """
    Esta función permite actualizar la información de un estudiante existente.
    Busca al estudiante por su nombre y permite modificar su nombre y edad.
    """
    nombre = input("Ingresa el nombre del estudiante que deseas actualizar: ")
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            print(f"Estudiante encontrado: {nombre}")
            nuevo_nombre = input("Ingresa el nuevo nombre (o presiona Enter para no cambiarlo): ")
            nueva_edad = input("Ingresa la nueva edad (o presiona Enter para no cambiarla): ")

            # Solo actualizamos si el usuario ingresó nuevos valores
            if nuevo_nombre:
                estudiante['nombre'] = nuevo_nombre
            if nueva_edad:
                estudiante['edad'] = int(nueva_edad)

            print(f"Estudiante {nombre} actualizado con éxito.")
            return
    
    print(f"No se encontró ningún estudiante con el nombre {nombre}.")
    
def eliminar_estudiante():
    """
    Esta función permite eliminar a un estudiante del sistema.
    Busca al estudiante por su nombre y lo elimina de la lista.
    """
    nombre = input("Ingresa el nombre del estudiante que deseas eliminar: ")
    for estudiante in estudiantes:
        if estudiante['nombre'] == nombre:
            estudiantes.remove(estudiante)
            print(f"Estudiante {nombre} eliminado con éxito.")
            return
    
    print(f"No se encontró ningún estudiante con el nombre {nombre}.")
    
def main():
    """
    Función principal que controla el flujo del programa.
    Usa un bucle while para mostrar el menú y realizar las acciones según la elección del usuario.
    """
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