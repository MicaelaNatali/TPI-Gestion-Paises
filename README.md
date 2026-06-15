# TPI - Gestión de Datos de Países en Python

Trabajo Práctico Integrador de Programación 1 - Tecnicatura Universitaria en Programación a Distancia.

## Descripción

Desarrollamos una aplicacion en Python que permite gestionar información sobre países (nombre, población, superficie y continente), utilizando listas, diccionarios, funciones, estructuras condicionales y repetitivas. Los datos se almacenan en un archivo CSV y el sistema debe permitir agregar países, realizar búsquedas, aplicar filtros y obtener estadísticas.

## Estructura del proyecto

```
TPI-Gestion-Paises/
├── paises.csv          # Dataset de países
├── datos.py            # Carga, guardado y alta de países
├── consultas.py        # Búsqueda y filtros
├── estadisticas.py      # Cálculo de estadísticas
└── main.py             # Menú principal
```

## Funcionalidades

El programa muestra un menú con las siguientes opciones:

1. **Agregar país**: solicita nombre, población, superficie y continente. No permite campos vacíos ni valores numéricos inválidos.
2. **Buscar país**: busca por coincidencia parcial o exacta en el nombre.
3. **Filtrar por continente**: muestra todos los países de un continente dado.
4. **Filtrar por población**: muestra países dentro de un rango de población.
5. **Filtrar por superficie**: muestra países dentro de un rango de superficie.
6. **Ordenar países por nombre**: ordena y muestra países en orden alfabético.
7. **Ordenar países por población**: ordena y muestra los países de menor a mayor población.
8. **Ordenar países por superficie**: ordena y muestra los países de menor a mayor superficie.
9. **Actualizar información de un país**: permite modificar la población y superficie de un país en específico.
10. **Mostrar estadísticas**: muestra país con mayor y menor población, promedio de población y superficie, y cantidad de países por continente.
11. **Salir**: finaliza el programa.

## Ejemplo de entrada/salida

```
========== GESTIÓN DE PAÍSES ==========
1. Agregar país
2. Buscar país
3. Filtrar por continente
4. Filtrar por población
5. Filtrar por superficie
6. Ordenar por nombre
7. Ordenar por población
8. Ordenar por superficie
9. Actualizar país
10. Mostrar estadísticas
11. Salir

=======================================
Seleccione una opción: 2
Ingrese el nombre a buscar: arg
{'nombre': 'Argentina', 'poblacion': 45376763, 'superficie': 2780400, 'continente': 'América'}
```

```
Seleccione una opción: 10

===== ESTADÍSTICAS =====
País con mayor población: China
País con menor población: Australia
Promedio de población: 274159056.0
Promedio de superficie: 3786580.875

Cantidad de países por continente:
América : 2
Europa : 2
Asia : 2
África : 1
Oceanía : 1
```
```
Seleccione una opción: 4
Población mínima: 50000000
Población máxima: 250000000
{'nombre': 'Brasil', 'poblacion': 213993437, 'superficie': 8515767, 'continente': 'América'}
{'nombre': 'Japón', 'poblacion': 125800000, 'superficie': 377975, 'continente': 'Asia'}
{'nombre': 'Nigeria', 'poblacion': 218541212, 'superficie': 923768, 'continente': 'África'}
```
## Integrantes y participación

Abrate Pilar: Desarrollo de datos.py (carga, guardado, alta y actualización de países), redacción del README y documentación.
Micaela Natali Villanueva: Desarrollo de consultas.py (búsqueda y filtros), estadisticas.py (cálculo de estadísticas) y main.py (menú principal).

Ambos integrantes participaron en la definición conjunta de la estructura de datos (diccionario de país), pruebas del programa y elaboración del informe.

## Video
 
Video demostrativo:
https://youtu.be/XDTUi6khpk0 
