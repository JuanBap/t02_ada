import sys
import time
from leer_rectangulos import leer_rectangulos
from iterativo import calcular_area_total
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
    intervalo = total_rectangulos // 20
    resultados = []

    print(f"Ejecutando pruebas con {total_rectangulos} rectángulos en 20 etapas...")

    for i in range(1, 21):
        n = i * intervalo
        subconjunto = rectangulos[:n]
        print(f"\n🔹 Prueba con {n} rectángulos:")

        area_iter, tiempo_iter = medir_tiempo(calcular_area_total, subconjunto)
        area_rec, tiempo_rec = medir_tiempo(area_union, subconjunto)

        print(f"📌 Iterativo - Área: {area_iter}, Tiempo: {tiempo_iter} ns")
        print(f"📌 Recursivo - Área: {area_rec}, Tiempo: {tiempo_rec} ns")

        resultados.append((n, tiempo_iter, tiempo_rec))

    # Guardar resultados en timestamps.txt
    with open('timestamps.txt', 'w') as f:
        f.write("Rectángulos,Tiempo_Iterativo(ns),Tiempo_Recursivo(ns)\n")
        for n, t_iter, t_rec in resultados:
            f.write(f"{n},{t_iter},{t_rec}\n")
