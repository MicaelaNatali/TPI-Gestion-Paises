def buscar_pais(paises):
    nombre = input ("Ingrese el nombre a buscar:"). lower()
    encontrados = []
    for pais in paises:
        if nombre in pais ["nombre"].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        print("No se encontraron países.")
    else:
        for pais in encontrados:
            print(pais)

def filtrar_continente(paises):
    continente = input ("Ingrese continente:").lower()
    for pais in paises:
            if pais ["continente"].lower() == continente:
                print(pais)

def filtrar_poblacion(paises):
    minimo = int(input("Población mínima:"))
    maximo = int(input("Población máxima:"))
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(pais)

def filtrar_superficie(paises):
    minimo = int(input("Superficie mínima:"))
    maximo = int(input("Superficie máxima:"))
    for pais in paises:
        if minimo <= pais ["superficie"] <=maximo:
            print(pais)
