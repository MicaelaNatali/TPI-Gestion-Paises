from datos import cargar_paises, agregar_pais
from consultas import (buscar_pais, filtrar_continente, filtrar_poblacion, filtrar_superficie, actualizar_pais, ordenar_nombre, ordenar_poblacion, ordenar_superficie)
from estadisticas import mostrar_estadisticas


def mostrar_menu():
    print("\n========== GESTIÓN DE PAÍSES ==========")
    print("1. Agregar país")
    print("2. Buscar país")
    print("3. Filtrar por continente")
    print("4. Filtrar por población")
    print("5. Filtrar por superficie")
    print("6. Ordenar por nombre")
    print("7. Ordenar por población")
    print("8. Ordenar por superficie")
    print("9. Actualizar país")
    print("10. Mostrar estadísticas")
    print("11. Salir")
    print("=======================================")


def main():

    paises = cargar_paises()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            buscar_pais(paises)

        elif opcion == "3":
            filtrar_continente(paises)

        elif opcion == "4":
            filtrar_poblacion(paises)

        elif opcion == "5":
            filtrar_superficie(paises)

        elif opcion == "6":
            ordenar_nombre(paises)

        elif opcion == "7":
            ordenar_poblacion(paises)

        elif opcion == "8":
            ordenar_superficie(paises)

        elif opcion == "9":
            actualizar_pais(paises)

        elif opcion == "10":
            mostrar_estadisticas(paises)

        elif opcion == "11":
            print ("Programa finalizado.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")


main()
