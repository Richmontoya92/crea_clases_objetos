# Este programa permite al usuario generar un pedido de té.

# Importamos la clase Te desde el archivo te.py para poder usar sus métodos.
from te import Te

# Mensajes para el usuario sobre los sabores disponibles
print("Bienvenido al sistema de pedidos de té artesanal.")
print("Sabores disponibles:")
print("  1: Té negro")
print("  2: Té verde")
print("  3: Agua de hierbas")

# Pedimos al usuario que ingrese el sabor deseado.
# Convertimos la entrada a un número entero.
sabor_elegido_num = int(input("Ingrese el número del sabor de té que desea (1, 2 o 3): "))

# Pedimos al usuario que ingrese el formato deseado.
print("\nFormatos disponibles:")
print("  300: 300 gramos")
print("  500: 500 gramos")
formato_elegido_num = int(input("Ingrese el formato en gramos que desea (300 o 500): "))

# Usamos los métodos estáticos de la clase Te para obtener la información.
# No necesitamos crear una instancia de Te para llamar a estos métodos,
# ya que son estáticos y operan directamente sobre la clase.

# Obtenemos el tiempo de preparación y la recomendación.
# La función retorna un diccionario, por eso accedemos a 'tiempo' y 'recomendacion'.
info_sabor = Te.obtener_tiempo_y_recomendacion(sabor_elegido_num)
tiempo_preparacion = info_sabor["tiempo"]
recomendacion_consumo = info_sabor["recomendacion"]

# Obtenemos el precio del té.
precio_te = Te.obtener_precio(formato_elegido_num)

# Convertimos el número de sabor a un texto descriptivo para mostrar al usuario.
# Esto mejora la legibilidad para el usuario final.
if sabor_elegido_num == 1:
    sabor_texto = "Té Negro"
elif sabor_elegido_num == 2:
    sabor_texto = "Té Verde"
elif sabor_elegido_num == 3:
    sabor_texto = "Agua de Hierbas"
else:
    sabor_texto = "Sabor desconocido" # Aunque se asume que el usuario ingresará valores válidos.

# Mostramos el resumen del pedido al usuario.
print("\n--- Detalle de su Pedido ---")
print(f"Sabor del té: {sabor_texto}")
print(f"Formato: {formato_elegido_num} gramos")
# Formateamos el precio para que se vea como moneda, si es un número válido.
if precio_te is not None:
    print(f"Precio: ${precio_te:,.0f}") # Formato con separador de miles
else:
    print("Precio: Formato no válido")

print(f"Tiempo de preparación: {tiempo_preparacion} minutos")
print(f"Recomendación de consumo: {recomendacion_consumo}")
print("----------------------------")
print("¡Gracias por su pedido!")