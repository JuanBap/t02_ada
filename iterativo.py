def calcular_cobertura(intervalos):
    if not intervalos:
        return 0

    intervalos_ordenados = sorted(intervalos, key=lambda inter: inter[0])
    cobertura = 0
    y_actual_inf, y_actual_sup = intervalos_ordenados[0]

    for i in range(1, len(intervalos_ordenados)):
        y_inf, y_sup = intervalos_ordenados[i]
        if y_inf > y_actual_sup:
            cobertura += (y_actual_sup - y_actual_inf)
            y_actual_inf, y_actual_sup = y_inf, y_sup
        else:
            y_actual_sup = max(y_actual_sup, y_sup)

    cobertura += (y_actual_sup - y_actual_inf)
    return cobertura


def area_union_rectangulos(rectangulos):
    eventos = []
    for (xu, yu, xd, yd) in rectangulos:
        eventos.append((xu, +1, yd, yu))
        eventos.append((xd, -1, yd, yu))

    eventos.sort(key=lambda e: e[0])

    intervalos_activos = []
    x_anterior = None
    area_total = 0

    for i, (x, tipo, y_inf, y_sup) in enumerate(eventos):
        if x_anterior is not None and x != x_anterior:
            cobertura_y = calcular_cobertura(intervalos_activos)
            delta_x = x - x_anterior
            area_total += cobertura_y * delta_x

        if tipo == +1:
            intervalos_activos.append((y_inf, y_sup))
        else:
            intervalos_activos.remove((y_inf, y_sup))

        x_anterior = x

    return area_total
