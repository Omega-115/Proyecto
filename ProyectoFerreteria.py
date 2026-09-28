print("Bienvenido a F.E.R.R.E")

import json
import os

Archivo_inventario = "inventario.json"
Archivo_ventas = "ventas.json"
Archivo_precios = "precios.json"

# Precios de las cosas,los clavos y tornillos se venden por pieza, 10/cu, la manguera se vende por metro, a 25 el metro
precios = {             
    "Tornillo": 10,
    "Martillo": 65,
    "Resistol 5000 tubo chico": 50,
    "Resistol 5000 tubo grande": 100,
    "Flexómetro": 65,
    "Atornillador": 70,
    "Desarmadores": 70,
    "Clavos": 10,
    "Escalera 1.50": 100,
    "Escalera reajustable": 250,
    "Extensión 1 metro": 50,
    "Extensión 2 metros": 100,
    "Extensión 3 metros": 150,
    "Manguera": 25,
    "Foco ecológico": 15,
    "Foco luz cálida": 20,

    # Las luces led son $50 el metro
    "Luces led": 50,

    "Linterna con baterías": 50,
    "Linterna recargable": 75,
    "Escuadra": 50,
    "Regla": 30,
    "Caja para herramientas": 100,
    "Cutters": 45,
    "Llave Allen": 30,
    "Llave Inglesa": 30,
    "Llave ajustable": 45,
    "Taladro": 75,

    # los guantes se venden por caja
    "Guantes de látex": 30,
    "Guantes de carnaza": 40,
    "Guantes de nylon": 45,
    "Serrucho": 75,
    "Segueta": 60,
    "Serrucho con arco": 80,
    "Repuesto de segueta": 50,
    "Electrodo": 25,
    "Careta para soldar": 75,
    " Lentes para soldar": 45,
    
    # el alambre es por metro
    "Alambre": 25,
    "Soldadora pequeña": 150,
    "Báscula chica": 50,
    "Báscula grande": 100,
    "Formones": 75,                         
    "Tijeras para jardinería": 50,
    "Bombas de agua": 250,
    "Repuesto para bomba de agua": 150,
    "Flotadores para agua": 150,

    # la tubería se vende por pieza
    "Tubería PVC 32mm": 25,
    "Tubería PVC 40mm": 30,
    "Tubería PVC 50mm": 35,
    "Tubería PVC 63mm": 40,
    "Tubería PVC 75mm": 45,
    "Tubería PVC 90mm": 50,
    "Tubería PVC 110mm": 55,
    "Tubería PVC 160mm": 60,
    "Tubería PVC 200mm": 70,
    "Enchufe": 20,

    # el cable se vende por metro
    "Cable para instalación eléctrica": 50,
    "Grifos": 65,
    "Manerales": 40,
    "Cerraduras": 50,
    "Cintas": 50,
    "Juego de herramientas": 250
}


# Es inventario, producto y cantidad disponible (esta lista solo se usa
# la primera vez que se corre el programa, cuando todavía no existe el JSON)

inventario_inicial = [
    ["Tornillo", 1000],
    ["Martillo", 15],
    ["Resistol 5000 tubo chico", 15],
    ["Resistol 5000 tubo grande", 15],
    ["Flexómetro", 15],
    ["Atornillador", 15],
    ["Desarmadores", 15],
    ["Clavos", 1000],
    ["Escalera 1.50", 10],
    ["Escalera reajustable", 10],

    # En las extensiones hay 100 metros cada una
    ["Extensión 1 metro", 100],
    ["Extensión 2 metros", 100],
    ["Extensión 3 metros", 100],
    ["Manguera", 100],
    ["Foco ecológico", 20],
    ["Foco luz cálida", 20],
    ["Luces led", 100],

    ["Linterna con baterías", 15],
    ["Linterna recargable", 15],
    ["Escuadra", 15],
    ["Regla", 20],
    ["Caja para herramientas", 10],
    ["Cutters", 15],
    ["Llave Allen", 20],
    ["Llave Inglesa", 20],
    ["Llave ajustable", 45],
    ["Taladro", 10],

    # los guantes es por cajas
    ["Guantes de látex", 15],
    ["Guantes de carnaza", 15],
    ["Guantes de nylon", 15],
    ["Serrucho", 15],
    ["Segueta", 20],
    ["Serrucho con arco", 20],
    ["Repuesto de segueta", 40],
    ["Electrodo", 15],
    ["Careta para soldar", 10],
    ["Lentes para soldar", 15],

    # el alambre es por metro
    ["Alambre", 100],
    ["Soldadora pequeña", 15],
    ["Báscula chica", 10],
    ["Báscula grande", 10],
    ["Formones", 15],                
    ["Tijeras para jardinería", 15],
    ["Bombas de agua", 10],
    ["Repuesto para bomba de agua", 10],
    ["Flotadores para agua", 10],

    # la tubería se vende por pieza
    ["Tubería PVC 32mm", 50],
    ["Tubería PVC 40mm", 50],
    ["Tubería PVC 50mm", 50],
    ["Tubería PVC 63mm", 50],
    ["Tubería PVC 75mm", 50],
    ["Tubería PVC 90mm", 50],
    ["Tubería PVC 110mm", 50],
    ["Tubería PVC 160mm", 50],
    ["Tubería PVC 200mm", 50],
    ["Enchufe", 50],

    # el cable se vende por metro
    ["Cable para instalación eléctrica", 100],
    ["Grifos", 20],
    ["Manerales", 20],
    ["Cerraduras", 20],
    ["Cintas", 20],
    ["Juego de herramientas", 10],
]

encontrado = False
mensaje = ""

# funcion para borrar productos 

def eliminar_producto(inventario, precios, nombre):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False, f"El producto '{nombre}' no existe en el inventario."

    # se quita de la lista de inventario
    inventario.remove(producto)

    # se quita también de precios, si está ahí
    if nombre in precios:
        del precios[nombre]

    return True, f"Producto eliminado: {nombre}"


# gaurdado de precios
def cargar_precios():
    if os.path.exists(Archivo_precios):
        with open(Archivo_precios, "r") as archivo:
            return json.load(archivo)
    else:
        # copia para no modificar el diccionario original
        return dict(precios)

def guardar_precios(precios):
    with open(Archivo_precios, "w") as archivo:
        json.dump(precios, archivo, ensure_ascii=False, indent=2)

# carga y guardado de inventario y ventas en json
def cargar_inventario():
    # carga el inventario desde inventario.json.
    # si el archivo no existe aún (primera vez que se corre el programa),
    # se usa el inventario inicial de arriba.
    if os.path.exists(Archivo_inventario):
        with open(Archivo_inventario, "r") as archivo:
            return json.load(archivo)
    else:
        # copia para no modificar accidentalmente la lista original
        return [fila[:] for fila in inventario_inicial]


def guardar_inventario(inventario):
    with open(Archivo_inventario, "w") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=2)


def cargar_ventas():
    # carga el historial de ventas desde ventas.json.
    # si el archivo no existe aún, se empieza con una lista vacía.
    if os.path.exists(Archivo_ventas):
        with open(Archivo_ventas, "r") as archivo:
            return json.load(archivo)
    else:
        return []


def guardar_ventas(ventas):
    with open(Archivo_ventas, "w") as archivo:
        json.dump(ventas, archivo, ensure_ascii=False, indent=2)



# Funciones de inventario


def mostrar_inventario(inventario):
    print("\n================================")
    print("       INVENTARIO ACTUAL")
    print("================================")

    for producto in inventario:
        print(producto[0], ":", producto[1], "piezas")

    print("================================")


def mostrar_stock_bajo(inventario, limite=5):
    # esto muestra los productos en el límite o en stock bajo
    print("\n================================")
    print("      PRODUCTOS CON STOCK BAJO")
    print("================================")

    bajos = [producto for producto in inventario if producto[1] <= limite]

    if not bajos:
        print("No hay productos en stock bajo.")
    else:
        for producto in bajos:
            print(producto[0], ":", producto[1], "piezas")

    print("================================")


def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto[0] == nombre:
            return producto
    return None

def buscar_producto_info(inventario, precios, nombre):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False, f"El producto '{nombre}' no se encontró en el inventario."

    precio = precios.get(nombre)
    if precio is None:
        return True, f"{producto[0]} | Precio: No registrado."

    return True, f"{producto[0]} | Existencias: {producto[1]} |Precio: ${precio}"

def nombre_valido(nombre):
    permitidos = "abcdefghijklmnñopqrstuvwxyzáéíóúü "
    if nombre == "":
        return False
    for letra in nombre.lower():
        if letra not in permitidos:
            return False
    return True


def agregar_producto(inventario, precios, nombre, precio, cantidad):
    # si el producto ya está registrado, se informa para no duplicarlo
    if buscar_producto(inventario, nombre) is not None:
        return False, f"El producto '{nombre}' ya existe en el inventario."

    # el precio debe ser mayor a 0
    if precio <= 0:
        return False, f"El precio ingresado ({precio}) no es válido. Tiene que ser mayor a 0."

    # la cantidad ingresada debe ser mayor o igual a 0
    if cantidad < 0:
        return False, f"La cantidad ingresada ({cantidad}) no es válida. Tiene que ser mayor o igual a 0."

    # se agrega al inventario y a la lista de precios
    inventario.append([nombre, cantidad])
    precios[nombre] = precio

    return True, f"Producto agregado: {nombre} | Precio: ${precio} | Cantidad: {cantidad}"


# Funciones de ventas

def vender_producto(inventario, precios, nombre, cantidad):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False, f"El producto '{nombre}' no existe en el inventario."

    if cantidad <= 0:
        return False, "La cantidad debe ser mayor a 0."

    precio_unitario = precios.get(nombre)
    if precio_unitario is None:
        return False, f"No se encontró el precio de '{nombre}'."

    if precio_unitario <= 0:
        return False, f"El precio de '{nombre}' no es válido."

    # no se puede vender más de lo que hay en el inventario
    if producto[1] < cantidad:
        return False, f"No hay suficiente stock de '{nombre}'. Disponible: {producto[1]}"

    # se resta del inventario
    producto[1] -= cantidad
    total = precio_unitario * cantidad

    venta = {
        "producto": nombre,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total": total
    }

    return True, venta


def mostrar_ventas(ventas):
    print("\n================================")
    print("      HISTORIAL DE VENTAS")
    print("================================")

    if not ventas:
        print("Todavía no se ha registrado ninguna venta.")
    else:
        for i, venta in enumerate(ventas, start=1):
            print(f"{i}. {venta['producto']} | Cantidad: {venta['cantidad']}"
                  f" | Precio unitario: ${venta['precio_unitario']} | Total: ${venta['total']}")

    print("================================")


def total_vendido(ventas):
    return sum(venta["total"] for venta in ventas)


def cancelar_ultima_venta(inventario, ventas):
    # esto cancela la última venta hecha, regresando el producto al inventario
    if not ventas:
        return False, "No hay ventas que cancelar."

    ultima_venta = ventas.pop()
    producto = buscar_producto(inventario, ultima_venta["producto"])

    if producto is not None:
        producto[1] += ultima_venta["cantidad"]

    return True, ultima_venta



# Programa principal


# se cargan el inventario y las ventas guardadas (o los valores iniciales
# si es la primera vez que se corre el programa)
inventario = cargar_inventario()
ventas = cargar_ventas()
precios = cargar_precios()




while True:
    print("\n=======================")
    print("         OPCIONES")
    print("========================")
    print("1.- Agregar producto")
    print("2.- Consultar inventario")
    print("3.- Buscar producto")
    print("4.- Vender producto")
    print("5.- Reporte de stock bajo")
    print("6.- Ver ventas del día")
    print("7.- Ver total vendido en el día")
    print("8.- Salir")
    print("9.- Eliminar producto")

    opcion = input("¿Qué operación desea realizar?: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ").strip()

        # se valida que el precio sea un número decimal
        try:
            precio = float(input("Precio del producto: "))
        except ValueError:
            print("El precio debe ser un número. Intenta de nuevo.")
            continue

        # se valida que la cantidad ingresada sea un número entero
        try:
            cantidad = int(input("Cantidad inicial en stock: "))
        except ValueError:
            print("La cantidad debe ser un número entero. Intenta de nuevo.")
            continue

        exito, mensaje = agregar_producto(inventario, precios, nombre, precio, cantidad)
        print(mensaje)

        if exito:
            guardar_inventario(inventario)

    elif opcion == "2":
        mostrar_inventario(inventario)

    elif opcion == "3":
        nombre = input("¿Cuál producto desea buscar?: ")
        encontrado, mensaje = buscar_producto_info(inventario, precios, nombre)
        print(mensaje)

    elif opcion == "4":

        nombre = input("Nombre del producto a vender: ").strip()
        try:
            cantidad = int(input("Cantidad a vender: "))
        except ValueError:
            print("La cantidad debe ser un número entero. Intenta de nuevo.")
            continue

        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            continue

        exito, resultado = vender_producto(inventario, precios, nombre, cantidad)

        if exito:
            venta = resultado
            print(f"Venta realizada: {venta['producto']} | Cantidad: {venta['cantidad']} "
                  f"| Precio unitario: ${venta['precio_unitario']} | Total: ${venta['total']}")
            ventas.append(venta)
            guardar_inventario(inventario)
            guardar_ventas(ventas)
        else:
            print(resultado)



    elif opcion == "5":
        mostrar_stock_bajo(inventario)

    elif opcion == "6":
        mostrar_ventas(ventas)

    elif opcion == "7":
        print(f"Total vendido: ${total_vendido(ventas)}")

    elif opcion == "8":
        guardar_inventario(inventario)
        guardar_ventas(ventas)
        guardar_precios(precios)

        print("Gracias por usar el sistema.")
        break

    elif opcion == "9":

        nombre = input("Nombre del producto a eliminar: ").strip()
        exito, mensaje = eliminar_producto(inventario, precios, nombre)
        print(mensaje)

        if exito:
            guardar_inventario(inventario)
            guardar_precios(precios)

    else:
        print("Opción no válida. Intenta de nuevo.")