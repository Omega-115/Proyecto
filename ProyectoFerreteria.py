print("Bienvenido a F.E.R.R.E")

import json
import os

Archivo_inventario = "inventario.json"
Archivo_ventas = "ventas.json"

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


# Es inventario, producto y cantidad disponible

inventario = [
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

# esta es la funcion para mostrar el inventario

def mostrar_inventario(inventario):
    print("\n================================")
    print("       INVENTARIO ACTUAL")
    print("================================")

    for producto in inventario:
        print(producto[0], ":", producto[1], "piezas")

    print("================================")



# esta es la funcion para buscar un producto 

def buscar_producto(inventario,nombre):

    for producto in inventario:

        if producto[0] == nombre:
            return producto
        
    return None

# funcion para hacer una venta con return con varios valores

def vender_producto(inventario, precios, nombre, cantidad):
    producto = buscar_producto(inventario, nombre)

    if producto is None:
        return False, f"El producto '{nombre}' no existe en el inventario."

    if cantidad <= 0:
        return False, "La cantidad debe ser mayor a 0."

    if producto[1] < cantidad:
        return False, f"No hay suficiente stock de '{nombre}'. Disponible: {producto[1]}"

    precio_unitario = precios.get(nombre)
    if precio_unitario is None:
        return False, f"No se encontró el precio de '{nombre}'."

    # restar inventario
    producto[1] -= cantidad
    total = precio_unitario * cantidad
    return True, total



    # cargado y guardado del inventario y las ventas

def cargar_inventario():

    # carga el inventario desde el archivo guardado la ultima vez.
    # si el archivo no existe aun, se usa el inventario inicial  

    if os.path.exists(Archivo_inventario): 
        with open(Archivo_inventario, "r") as archivo:
            return json.load(archivo)

    else:
        # copia para no modificar accidentalmente la lista original
        return [fila[:] for fila in inventario]

def guardar_inventario(inventario):
    with open(Archivo_inventario, "w") as archivo:
        json.dump(inventario, archivo)

def cargar_ventas():
    if os.path.exists(Archivo_ventas):
        with open(Archivo_ventas, "r") as archivo:
            return json.load(archivo)
    else:   
        return []

def guardar_ventas(ventas):
    with open(Archivo_ventas, "w") as archivo:
        json.dump(ventas, archivo)


# validación de los precios

def validar_precios(precios):
    # esto revisa que todos los precios sean mayores a 0
    for producto, precio in precios.items():
        if precio <= 0:
         print(f"AVISO: el precio de '{producto}' no es válido ({precio}). Debe ser mayor a 0.")
    


# funciones de inventario

def mostrar_inventario(inventario):
    print("\n================================")
    print("       INVENTARIO ACTUAL")
    print("================================")

    for producto in inventario:
        print(producto[0], ":", producto[1], "piezas")

    print("================================")


def mostrar_stock_bajo(inventario, limite=5):
   # esto muestra los productos en limite o en stock bajo
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

# esta será el área de ventas

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
    if producto [1] < cantidad:
        return False, f"No hay suficiente stock de '{nombre}' Disponible: {producto[1]}"


    # esto es para restar el inventario 
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
                  f"| Precio unitario: ${venta['precio_unitario']} | Total: ${venta['total']}")

    print("================================")


def cancelar_ultima_venta(inventario, ventas):

    # esto cancela la ultima venta hecha, regresando el producto al inventario
    if not ventas:
        return False, "No hay ventas que cancelar."

    ultima_venta = ventas.pop()
    producto = buscar_producto(inventario, ultima_venta["producto"])
  
    if producto is not None:
        producto[1] += ultima_venta["cantidad"]

    return True, ultima_venta



# ahora si este es el programa principal 