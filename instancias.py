# Este archivo importará la clase Te y creará instancias de ella.

# Importamos la clase Te desde el archivo te.py
from te import Te

# Creamos la primera instancia de la clase Te.
# Una instancia es un objeto concreto que nace de la "plantilla" de la clase Te.
instancia_te_1 = Te()

# Creamos la segunda instancia de la clase Te.
instancia_te_2 = Te()

# Obtenemos el tipo de dato de cada instancia.
# La función type() nos dice de qué tipo es un objeto.
tipo_instancia_1 = type(instancia_te_1)
tipo_instancia_2 = type(instancia_te_2)

# Mostramos por pantalla el tipo de dato de cada instancia.
print(f"Tipo de la primera instancia: {tipo_instancia_1}")
print(f"Tipo de la segunda instancia: {tipo_instancia_2}")

# Comparamos si ambos tipos de datos son iguales.
if tipo_instancia_1 == tipo_instancia_2:
    print("Ambos objetos son del mismo tipo.")
else:
    print("Los objetos no son del mismo tipo.")