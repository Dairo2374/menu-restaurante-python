# [Nombre del Producto, Categoría, Precio Base].
menu = [
    ["Hamburguesa", "Comida Rapida", 18000],
    ["Pizza", "Comida Rapida", 25000],
    ["Pie de limon", "Postre", 15000],
    ["Jugo Natural", "Bebida", 8000],
    ["Helado Frutos rojos", "Postre", 8000],
    ["Gaseosa", "Bebida", 5000],
]

categoria_descuento = "Postre"
umbral_precio = 12000


def calcular_precio_final(categoria, precio_base):

    if categoria == categoria_descuento and precio_base > umbral_precio:
        descuento = precio_base * 0.15
        precio_final = precio_base - descuento
    else:
        precio_final = precio_base

    return precio_final


print("===== MENÚ DEL RESTAURANTE =====\n")

for producto in menu:
    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    precio_final = calcular_precio_final(categoria, precio_base)

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio Base: $", precio_base)
    print("Precio Final: $", precio_final)
    print("-----------------------------")
