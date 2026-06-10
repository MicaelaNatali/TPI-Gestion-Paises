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

def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar:"). lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            pais["poblacion"] = int(input("Nueva población:"))
            pais["superficie"] = int(input("Nueva superficie:"))
            print("País actualizado correctamente.")
            return
    print("País no encontrado.")

def ordenar_nombre(paises):
    for i in range(len(paises)):
        for j in range (i+ 1, len (paises)):
            if paises [i]["nombre"] > paises [j]["nombre"]:
                aux = paises [i]
                paises [i] = paises [j]
                paises [j] = aux
    for pais in paises:
        print(pais)

def ordenar_poblacion(paises):
    for i in range(len(paises)):
        for j in range (i + 1, len (paises)):
            if paises[i]["poblacion"] > paises [j]["poblacion"]:
                aux = paises [i]
                paises [i] = paises [j]
                paises [j] = aux
    for pais in paises:
        print (pais)

def ordenar_superficie(paises):
    for i in range (len(paises)):
        for j in range(i + 1, len (paises)):
            if paises [i]["superficie"] > paises [j]["superficie"]:
                aux = paises [i]
                paises [i] = paises [j]
                paises [j] = aux
    for pais in paises:
        print (pais)
            
            
