def area_del_rectangulo(rectangulo):
    """
    Calcula el área de un rectángulo dado en forma (x1, y1, x2, y2),
    donde (x1, y1) es la esquina superior izquierda
    y (x2, y2) es la esquina inferior derecha.
    """
    x1, y1, x2, y2 = rectangulo
    return max(0, x2 - x1) * max(0, y1 - y2)


def interseccion_rectas(r1, r2):
    """
    Retorna la intersección de dos rectángulos r1 y r2 en forma (x1, y1, x2, y2).
    Si no se intersectan, retorna None.
    """
    x1a, y1a, x2a, y2a = r1
    x1b, y1b, x2b, y2b = r2

    x_left = max(x1a, x1b)
    y_top = min(y1a, y1b)
    x_right = min(x2a, x2b)
    y_bottom = max(y2a, y2b)

    if x_left < x_right and y_bottom < y_top:
        return (x_left, y_top, x_right, y_bottom)
    else:
        return None


def area_union(rectangles):
    """
    Función principal que llama a la función auxiliar recursiva.
    """
    return area_union_aux(rectangles, 0, len(rectangles))


def area_union_aux(rectangles, begin, end):
    """
    Función auxiliar que maneja la recursión de la unión de áreas de rectángulos.
    """
    if end - begin == 0:
        return 0
    if end - begin == 1:
        return area_del_rectangulo(rectangles[begin])

    mid = (begin + end) // 2
    area_izq = area_union_aux(rectangles, begin, mid)
    area_der = area_union_aux(rectangles, mid, end)

    intersecciones = []
    for i in range(begin, mid):
        for j in range(mid, end):
            inter = interseccion_rectas(rectangles[i], rectangles[j])
            if inter is not None:
                intersecciones.append(inter)

    area_intersection = area_union_aux(intersecciones, 0, len(intersecciones))

    return area_izq + area_der - area_intersection
