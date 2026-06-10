def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay países cargados.")
        return

    mayor = max(paises, key=lambda pais: pais["poblacion"])
    menor = min(paises, key=lambda pais: pais["poblacion"])

    promedio_poblacion = sum(
        pais["poblacion"] for pais in paises
    ) / len(paises)

    promedio_superficie = sum(
        pais["superficie"] for pais in paises
    ) / len(paises)

    print("\n===== ESTADÍSTICAS =====")

    print("País con mayor población:", mayor["nombre"])
    print("País con menor población:", menor["nombre"])
    print("Promedio de población:", promedio_poblacion)
    print("Promedio de superficie:", promedio_superficie)

    continentes = {}

    for pais in paises:

        continente = pais["continente"]

        if continente in continentes:
            continentes[continente] += 1
        else:
            continentes[continente] = 1

    print("\nCantidad de países por continente:")

    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)
