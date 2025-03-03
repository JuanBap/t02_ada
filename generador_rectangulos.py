import random
import sys


def generate_rectangles(n, max_area=25, filename="rectangles.txt"):
    rectangles = []
    x_start = 0

    for _ in range(n):
        width = random.randint(1, 5)
        height = random.randint(1, max_area // width)
        x_u = x_start
        y_u = random.randint(5, 15)  # Asegurar valores positivos
        x_d = x_u + width
        y_d = max(1, y_u - height)  # Evitar valores negativos

        rectangles.append((x_u, y_u, x_d, y_d))
        x_start += width + random.randint(1, 3)  # Espaciado variable entre rectángulos

    with open(filename, "w") as f:
        for rect in rectangles:
            f.write(f"{rect[0]} ,{rect[1]} ,{rect[2]} ,{rect[3]}\n")

    print(f"Se han generado {n} rectángulos en el archivo '{filename}'")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
            generate_rectangles(n)
        except ValueError:
            print("Por favor, ingrese un número válido de rectángulos.")
    else:
        print("Uso: python generador_rectangulos.py <numero_de_rectangulos>")
