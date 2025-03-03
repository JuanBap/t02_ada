def leer_rectangulos(archivo):
    """
    Lee un archivo de texto con coordenadas de rectángulos.
    Cada línea del archivo debe tener 4 valores separados por comas: x_u, y_u, x_d, y_d
    """
    rectangulos = []
    with open(archivo, 'r') as file:
        for linea in file:
            valores = list(map(int, linea.strip().split(',')))
            if len(valores) == 4:
                rectangulos.append(tuple(valores))
    return rectangulos
