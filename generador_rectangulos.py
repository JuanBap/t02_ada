import random
import sys


def generate_rectangles(n, max_area=25, filename="rectangulos.txt"):
    """
    Genera 'n' rectángulos, cada uno definido por (x_u, y_u, x_d, y_d),
    donde:
      - (x_u, y_u) es la esquina superior-izquierda,
      - (x_d, y_d) es la esquina inferior-derecha,
      - x_u < x_d, y_d < y_u y todos los valores son >= 0.
    """
    rectangles = []

    # Comenzamos con un x_u inicial
    x_u = 0
    # Podemos arrancar con un y_u aleatorio en [5..15]
    y_u = random.randint(5, 15)

    for _ in range(n):
        # Elegimos un ancho y alto de forma aleatoria,
        # acotando el área para que sea <= max_area
        width = random.randint(1, 5)
        height = random.randint(1, max_area // width)

        # Definimos la esquina inferior derecha
        x_d = x_u + width
        # Aseguramos que y_d sea menor que y_u y no negativo
        y_d = max(0, y_u - height)

        # Agregamos el rectángulo
        rectangles.append((x_u, y_u, x_d, y_d))

        # Ahora actualizamos las coordenadas para el siguiente
        # Aseguramos que el siguiente x_u sea estrictamente mayor
        x_u += random.randint(1, 3)
        # Volvemos a tomar un y_u aleatorio (deja posibilidad de solapar o no)
        y_u = random.randint(5, 15)

    # Guardamos en archivo
    with open(filename, "w") as f:
        for rect in rectangles:
            f.write(f"{rect[0]} ,{rect[1]} ,{rect[2]} ,{rect[3]}\n")

    print(f"Se han generado {n} rectángulos en el archivo '{filename}'")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            # Puedes ajustar max_area o el nombre de archivo si lo deseas:
            generate_rectangles(n, max_area=25, filename="rectangulos.txt")
        except ValueError:
            print("Por favor, ingrese un número válido de rectángulos.")
    else:
        print("Uso: python generador_rectangulos.py <numero_de_rectangulos>")
