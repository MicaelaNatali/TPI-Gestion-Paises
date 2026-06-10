import csv

archivo = "paises.csv"

def cargar_paises():
    #Lee el CSV manualmente y devuelve una lista de diccionarios.
    paises = []
    try:
        with open(archivo, encoding="utf-8") as f:
            lineas = f.readlines()
            # La primera línea es el encabezado, la saltamos
            for linea in lineas[1:]:
                linea = linea.strip()  # saca el \n del final
                if linea == "":       # ignora líneas vacía
                    continue
                partes = linea.split(",")  # separa por coma
                pais = {
                    "nombre": partes[0],
                    "poblacion": int(partes[1]),
                    "superficie": int(partes[2]),
                    "continente": partes[3]
                }
                paises.append(pais)
    except FileNotFoundError:
        print("Error: no se encontró el archivo CSV.")
    return paises

def agregar_pais(paises):
    print("Agregar país")
    nombre = input("Ingresá el nombre del país: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    
    try:
        poblacion = int(input("Ingresá la población: ").strip())
        if poblacion <= 0:
            print("Error: la población debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: la población debe ser un número entero.")
        return
    
    try:
        superficie = int(input("Ingresá la superficie: ").strip())
        if superficie <= 0:
            print("Error: la superficie debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: la superficie debe ser un número entero.")
        return
    
    continente = input("Ingresá el continente: ").strip()
    if continente == "":
        print("Error: el continente no puede estar vacío.")
        return
    
    pais = {
    "nombre": nombre,
    "poblacion": poblacion,
    "superficie": superficie,
    "continente": continente
    }

    paises.append(pais)
    guardar_paises(paises)  
    print("País agregado correctamente.")

def guardar_paises(paises):
    #Guarda la lista de países en el CSV.
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            f.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")

def actualizar_datos(paises):
    nombre = input("Ingrese el nombre de un pais que este en la lista: ")
    for pais in paises:
        if pais["nombre"] == nombre:            
            print("Pais encontrado")

            try:
                poblacion = int(input("Ingrese la nueva poblacion: "))
                if poblacion <= 0:
                    print("Error: la población debe ser mayor a cero.")
                    return
            except ValueError:
                print("Error: la población debe ser un número entero.")
                return
            
            try:
                superficie = int(input("Ingrese la nueva superficie: "))
                if superficie <=0:
                    print("Error: La superficie debe ser un numero mayor a cero.")
                    return
            except ValueError:
                print("Error: la superficie debe ser un número entero.")
                return
            
            pais["poblacion"] = poblacion
            pais["superficie"] = superficie 

            guardar_paises(paises)
            print("País actualizado correctamente.")
            return
        
    print("Pais no encontrado")


    

