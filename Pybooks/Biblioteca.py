# Biblioteca.py
import random

# Diccionarios de productos y stock
productos = {
    '8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
    '2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
    'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2050Ti'],
    'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'Integrada'],
    'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
    '123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'Integrada'],
    '342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
    'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {
    '8475HD': [387990, 10],
    '2175HD': [327990, 4],
    'JjfFHD': [424990, 1],
    'fgdxFHD': [664990, 21],
    '123FHD': [290890, 32],
    '342FHD': [444990, 7],
    'GF75HD': [749990, 2],
    'UWU131HD': [4349990, 1],
    'Fs1230HD': [249990, 0],
}

# Marcas válidas
marcas_validas = ['hp', 'lenovo', 'asus', 'dell']

# Ver el stock de una marca (aleatorios)
def stock_marca(marca):
    while True:
        marca = marca.lower()
        if marca not in marcas_validas:
            print("Lo sentimos. No manejamos esas marcas.")
            marca = input("Ingrese marca a consultar: ")
            continue
        break

    total_stock = 0
    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            # Genera número aleatorio entre 0 y 50
            stock_aleatorio = random.randint(0, 50)
            if total_stock + stock_aleatorio > 50:
                stock_aleatorio = 50 - total_stock
            total_stock += stock_aleatorio
    
    print(f"El stock de la marca {marca.capitalize()} es: {total_stock}")

# Buscar dentro del rango de precios
def busqueda_precio(p_min, p_max):
    
    if p_min < 0 or p_max < 0:
        print("¡Error!: Debe ingresar un precio válido")
        return

    encontrados = []
    
    # Verifición de precios
    for modelo, datos in productos.items():
        if stock[modelo][1] > 0 and p_min <= stock[modelo][0] <= p_max:
            encontrados.append(f"{datos[0]}--{modelo}")
    
    if len(encontrados) > 0:
        encontrados.sort()
        print("Los notebooks entre los precios consultados son:", encontrados)
    else:
        print("Lo sentimos. No hay notebooks en ese rango de precios.")

# Función para actualizar el precio
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p  # Actualizar el precio
        return True  # Si el modelo existe, True
    return False  # Si el modelo no existe, False

# Función principal
def menu():
    while True:
        print("\n*** MENU PRINCIPAL ***")
        print("1. Stock marca")
        print("2. Búsqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")
        
        # Opción para elegir en el menú
        opcion = input("Ingrese opción: ")

        # Opción 1
        if opcion == "1":
            marca = input("Ingrese marca a consultar: ")
            stock_marca(marca)
        
        # Opción 2
        elif opcion == "2":
            # Precio mínimo
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    break
                except ValueError:
                    print("¡Error!: Ingrese valores enteros")

            # Precio máximo
            while True:
                try:
                    p_max = int(input("Ingrese precio máximo: "))
                    break
                except ValueError:
                    print("¡Error!: Ingrese valores enteros")

            busqueda_precio(p_min, p_max)

        # Opción 3
        elif opcion == "3":
            modelo = input("Ingrese modelo a actualizar: ")
            while True:
                try:
                    precio_nuevo = int(input("Ingrese precio nuevo: "))
                    break
                except ValueError:
                    print("¡Error!: Debe ingresar un precio válido")

            if actualizar_precio(modelo, precio_nuevo):
                print("¡El precio se ha actualizado!")
            else:
                print("Lo sentimos. El modelo no existe")
            
            # Preguntar si desea actualizar otro precio
            respuesta = input("¿Desea actualizar otro precio (s/n)? ").lower()
            if respuesta != 's':
                continue

        # Opción 4
        elif opcion == "4":
            print("Programa FINALIZADO.")
            break
        
        # Si se ingresa una opción incorrecta
        else:
            print("¡Error!: Selecione una opción válida")

