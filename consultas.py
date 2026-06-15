from datos import guardar_paises

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
    encontrados = False
    for pais in paises:
            if pais ["continente"].lower() == continente:
                print(pais)
                encontrados = True
    if not encontrados:
        print("No se encontraron países en ese continente.")

def filtrar_poblacion(paises):
    try:
        minimo = int(input("Población mínima:"))
        maximo = int(input("Población máxima:"))
    except ValueError:
        print("Error: debe ingresar números enteros.")
        return
    encontrados = False
    for pais in paises:
<<<<<<< HEAD
        if minimo <= int (pais["poblacion"]) <= maximo:
=======
        if minimo <= int(pais["poblacion"]) <= maximo:
>>>>>>> 70dbc524fc1165bf59215b928108afe4609cca30
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países en ese rango.")

def filtrar_superficie(paises):
    try:
        minimo = int(input("Superficie mínima:"))
        maximo = int(input("Superficie máxima:"))
    except ValueError:
        print("Error: debe ingresar números enteros.")
        return
    encontrados = False
    for pais in paises:
        if minimo <= int(pais ["superficie"]) <=maximo:
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países en ese rango.")

def actualizar_pais(paises):
    nombre = input("Ingrese el nombre del país a actualizar:"). lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            try:
                poblacion = int(input("Nueva población:"))
                if poblacion <= 0:
                    print("Error: la población debe ser mayor a cero.")
                    return
            except ValueError:
                print("Error: la población debe ser un número entero.")
                return
            try:
                superficie = int(input("Nueva superficie:"))
                if superficie <= 0:
                    print("Error: la superficie debe ser mayor a cero.")
                    return
            except ValueError:
                print("Error: la superficie debe ser un número entero.")
                return
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie
            guardar_paises(paises)
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
            
            
