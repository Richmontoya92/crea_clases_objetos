# Este archivo contendrá la definición de la clase Te

class Te:
    # Atributo de clase: es un valor que será el mismo para todas las instancias de Te.
    # En este caso, representa la duración estándar de cualquier té.
    duracion = "1 año" # O "365 días", según la descripción del problema.

    # Método estático para obtener el tiempo de preparación y la recomendación
    # Un método estático no necesita acceder a los atributos de una instancia específica,
    # opera sobre los parámetros que recibe.
    @staticmethod
    def obtener_tiempo_y_recomendacion(sabor):
        # Aquí almacenamos la información de cada tipo de té
        datos_te = {
            1: {"tiempo": 3, "recomendacion": "Consumir al desayuno"},  # Té negro
            2: {"tiempo": 5, "recomendacion": "Consumir al medio día"}, # Té verde
            3: {"tiempo": 6, "recomendacion": "Consumir al atardecer"}  # Agua de hierbas
        }
        # Obtenemos el tiempo y la recomendación según el número de sabor ingresado
        return datos_te.get(sabor, {"tiempo": None, "recomendacion": "Sabor no reconocido"})

    # Método estático para obtener el precio según el formato
    # Similar al anterior, no necesita una instancia para funcionar.
    @staticmethod
    def obtener_precio(formato):
        # Definimos los precios para cada formato
        precios_formato = {
            300: 3000, # Formato de 300gr
            500: 5000  # Formato de 500gr
        }
        # Retornamos el precio según el formato ingresado, si no se encuentra, retorna None
        return precios_formato.get(formato, None)