import sys
import time
from leer_rectangulos import leer_rectangulos
from iterativo import area_union_rectangulos
from recursivo import area_union


def medir_tiempo(funcion, rectangulos):
    inicio = time.perf_counter_ns()
    area = funcion(rectangulos)
    fin = time.perf_counter_ns()
    return area, fin - inicio


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main.py <archivo_rectangulos>")
        sys.exit(1)

    archivo_rectangulos = sys.argv[1]
    rectangulos = leer_rectangulos(archivo_rectangulos)

    total_rectangulos = len(rectangulos)
    tamanos_pruebas = [total_rectangulos // 4, total_rectangulos // 2, (3 * total_rectangulos) // 4, total_rectangulos]

    print(f"Ejecutando pruebas con {total_rectangulos} rectángulos en 4 etapas...")

    for n in tamanos_pruebas:
        subconjunto = rectangulos[:n]
        print(f"\n🔹 Prueba con {n} rectángulos:")

        area_iter, tiempo_iter = medir_tiempo(area_union_rectangulos, subconjunto)
        print(f"📌 Iterativo - Área: {area_iter}, Tiempo: {tiempo_iter} ns")

        area_rec, tiempo_rec = medir_tiempo(area_union, subconjunto)
        print(f"📌 Recursivo - Área: {area_rec}, Tiempo: {tiempo_rec} ns")
