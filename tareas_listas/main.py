from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    lista.añadir(Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"))
    lista.añadir(Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"))
    lista.añadir(Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"))
    lista.añadir(Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"))
    lista.añadir(Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"))
    print("  ✓ Datos de prueba cargados")


def mostrar_opciones(titulo, extras=False):
    print("\n" + "=" * 55)
    print(f"        ✈  SISTEMA DE PASAJEROS")
    print(f"             {titulo}")
    print("=" * 55)

    print("\n  [1] Añadir pasajero")
    print("  [2] Listar pasajeros")
    print("  [3] Insertar en una posición")

    print("  [4] Buscar por número (lineal)")
    print("  [5] Buscar por número (binaria)")
    print("  [6] Modificar pasajero")

    print("  [7] Eliminar por posición")
    print("  [8] Eliminar por número")
    
    print("  [9] Ordenar ascendentemente")
    print(" [10] Ordenar descendentemente")
    print(" [11] Invertir lista")

    print(" [12] Copiar lista")
    print(" [13] Mostrar cantidad de pasajeros")

    if extras:
        print("\n  --- FUNCIONES EXCLUSIVAS DE LISTA PYTHON ---")
        print(" [14] Filtrar pasajeros por destino")
        print(" [15] Mostrar mayores de edad")

    print("\n  --- DATOS Y SALIDA ---")
    print("  [C] Cargar datos de prueba")
    print("  [0] Volver al menú principal")

    print("\n" + "=" * 55)


# ---------------------- MENÚ 1 · MiLista ----------------------
def menu_lista1():
    while True:
        mostrar_opciones("MENÚ 1 · MiLista")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if lista1.añadir(pasajero):                # 2. LLAMAR
                print("  ✓ Pasajero añadido")          # 3. MOSTRAR
        elif op == "2":
            lista1.listar()
        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()

            if lista1.insertar(posicion, pasajero):
                print("  ✓ Pasajero insertado correctamente")
            else:
                print("  ⚠ No se pudo insertar el pasajero")
        elif op == "4":
            numero = leer_entero("  Número de pasajero a buscar: ")
            posicion = lista1.buscar(numero)

            if posicion != -1:
                print("  ✓ Pasajero encontrado:")
                print(f"  Posición: {posicion}")
                print(f"  {lista1.datos[posicion]}")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "5":
            numero = leer_entero("  Número de pasajero: ")
            posicion = lista1.buscar_binaria(numero)

            if posicion != -1:
                print("  ✓ Pasajero encontrado:")
                print(f"  {lista1.datos[posicion]}")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "6":
            numero = leer_entero("  Número del pasajero: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista1.modificar(numero, destino, asiento):
                print("  ✓ Pasajero modificado")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "7":
            posicion = leer_entero("  Posición a eliminar: ")
            pasajero = lista1.eliminar_por_posicion(posicion)

            if pasajero is not None:
                print("  ✓ Pasajero eliminado:")
                print(f"  {pasajero}")
            else:
                print("  ⚠ Posición no válida")
        elif op == "8":
            numero = leer_entero("  Número del pasajero a eliminar: ")

            if lista1.eliminar_por_valor(numero):
                print("  ✓ Pasajero eliminado")
            else:
                print("  ⚠ Pasajero no encontrado")
        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Lista ordenada de menor a mayor")
            lista1.listar()
        elif op == "9":
            lista1.ordenar_asc()
            print("  ✓ Lista ordenada de menor a mayor")
            lista1.listar()
        elif op == "11":
            lista1.reversar()
            print("  ✓ Lista invertida")
            lista1.listar()
        elif op == "12":
            copia = lista1.copiar()

            print("  ✓ Copia creada correctamente")
            copia.listar()
        elif op == "13":
            print(f" Cantidad de pasajeros {lista1.longitud()}o") 
        elif op == "C":
            cargar_datos_prueba(lista1)

        # ✍ TODO: opciones 3 a 13 con el patrón LEER → LLAMAR → MOSTRAR

        elif op == "0":
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · list de Python ----------------------

def menu_lista2():
    while True:
        mostrar_opciones("MENÚ 2 - Lista de Python", extras=True)

        op = input("\n  Seleccione una opción: ").strip().upper()

        # 1. Añadir pasajero
        if op == "1":
            pasajero = leer_pasajero()

            if lista2.añadir(pasajero):
                print("\n  ✓ Pasajero añadido correctamente")

        # 2. Listar pasajeros
        elif op == "2":
            lista2.listar()

        # 3. Insertar en una posición
        elif op == "3":
            posicion = leer_entero("  Posición donde insertar: ")
            pasajero = leer_pasajero()

            if lista2.insertar(posicion, pasajero):
                print("\n  ✓ Pasajero insertado correctamente")
            else:
                print("\n  ⚠ No se pudo insertar el pasajero")

        # 4. Buscar por número (lineal)
        elif op == "4":
            numero = leer_entero("  Número de pasajero a buscar: ")
            posicion = lista2.buscar(numero)

            if posicion != -1:
                print(f"\n  ✓ Pasajero encontrado en posición {posicion}")
                print(lista2.pasajeros[posicion])
            else:
                print("\n  ⚠ Pasajero no encontrado")

        # 5. Buscar por número (binaria)
        elif op == "5":
            numero = leer_entero("  Número de pasajero a buscar: ")

            # La búsqueda binaria necesita orden ascendente
            lista2.ordenar_asc()
            posicion = lista2.buscar_binaria(numero)

            if posicion != -1:
                print(f"\n  ✓ Pasajero encontrado en posición {posicion}")
                print(lista2.pasajeros[posicion])
            else:
                print("\n  ⚠ Pasajero no encontrado")

        # 6. Modificar pasajero
        elif op == "6":
            numero = leer_entero("  Número del pasajero a modificar: ")
            destino = input("  Nuevo destino: ").strip()
            asiento = input("  Nuevo asiento: ").strip().upper()

            if lista2.modificar(numero, destino, asiento):
                print("\n  ✓ Pasajero modificado correctamente")
            else:
                print("\n  ⚠ Pasajero no encontrado")

        # 7. Eliminar por posición
        elif op == "7":
            posicion = leer_entero("  Posición del pasajero a eliminar: ")
            pasajero = lista2.eliminar_por_posicion(posicion)

            if pasajero is not None:
                print("\n  ✓ Pasajero eliminado:")
                print(pasajero)
            else:
                print("\n  ⚠ Posición no válida")

        # 8. Eliminar por número
        elif op == "8":
            numero = leer_entero("  Número del pasajero a eliminar: ")

            if lista2.eliminar_por_valor(numero):
                print("\n  ✓ Pasajero eliminado correctamente")
            else:
                print("\n  ⚠ Pasajero no encontrado")

        # 9. Ordenar ascendentemente
        elif op == "9":
            lista2.ordenar_asc()
            print("\n  ✓ Lista ordenada de menor a mayor")
            lista2.listar()

        # 10. Ordenar descendentemente
        elif op == "10":
            lista2.ordenar_desc()
            print("\n  ✓ Lista ordenada de mayor a menor")
            lista2.listar()

        # 11. Invertir lista
        elif op == "11":
            lista2.reversar()
            print("\n  ✓ Orden de la lista invertido")
            lista2.listar()

        # 12. Copiar lista
        elif op == "12":
            copia = lista2.copiar()
            print("\n  ✓ Copia de la lista creada correctamente")
            copia.listar()

        # 13. Mostrar cantidad de pasajeros
        elif op == "13":
            print(f"\n  Cantidad de pasajeros: {lista2.longitud()}")

        # 14. Filtrar por destino
        elif op == "14":
            destino = input("  Ingrese el destino que desea buscar: ").strip()
            resultado = lista2.filtrar_por_destino(destino)

            if resultado:
                print(f"\n  ✓ Pasajeros con destino a {destino}:")
                for pasajero in resultado:
                    print(f"  {pasajero}")
            else:
                print(f"\n  ⚠ No hay pasajeros con destino a {destino}")

        # 15. Mostrar mayores de edad
        elif op == "15":
            resultado = lista2.mayores_de_edad()

            if resultado:
                print("\n  ✓ Pasajeros mayores de edad:")
                for pasajero in resultado:
                    print(f"  {pasajero}")
            else:
                print("\n  ⚠ No hay pasajeros mayores de edad")

        # C. Cargar datos de prueba
        elif op == "C":
            cargar_datos_prueba(lista2)

        # 0. Volver al menú principal
        elif op == "0":
            break

        else:
            print("\n  ⚠ Opción no válida. Intente nuevamente.")



# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA LISTAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · MiLista")
        print("2. Menú 2 · list de Python")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_lista1()
        elif op == "2":
            menu_lista2()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()