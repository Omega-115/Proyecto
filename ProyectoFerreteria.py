print("Bienvenido a F.E.R.R.E")

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
    ["Guantes de carnaza": 15],
    ["Guantes de nylon": 15],
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









while True:
    print("\nOpciones: ")
    print("1.- Agregar Producto")
    print("2.- Consultar Inventario")
    print("3.- Buscar Producto")
    print("4.- Vender Producto")
    print("5.- Reporte de Stock Bajo")
    print("6.- Ver Ventas del Día")
    print("7.- Ver Total Vendido en el Día")
    print("8.- Salir")

    opcion = input("¿Qué operación desea realizar?: ")

    if opcion == "1":
        print(input("¿Qué producto desea ingresar al sistema?"))
