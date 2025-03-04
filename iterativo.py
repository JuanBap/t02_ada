def calcular_area_total(rectangulos):
    def interseccion(r1, r2):
        """ Calcula la intersección entre dos rectángulos dados en formato (x1, y1, x2, y2) """
        x1 = max(r1[0], r2[0])
        y1 = min(r1[1], r2[1])  # Máxima altura de la intersección
        x2 = min(r1[2], r2[2])
        y2 = max(r1[3], r2[3])  # Mínima base de la intersección

        if x1 < x2 and y1 > y2:  # Si hay una intersección válida
            return (x1, y1, x2, y2)
        return None

    def area(r):
        """ Calcula el área de un rectángulo dado """
        return (r[2] - r[0]) * (r[1] - r[3])

    area_total = 0
    rectangulos_previos = []  # Lista para almacenar rectángulos ya procesados

    for rect in rectangulos:
        nueva_area = area(rect)
        area_intersecciones = 0

        # Comparar con todos los rectángulos anteriores para restar intersecciones
        for rect_anterior in rectangulos_previos:
            inter = interseccion(rect_anterior, rect)
            if inter:
                area_intersecciones += area(inter)

        # Sumar solo el área no cubierta previamente
        area_total += nueva_area - area_intersecciones
        rectangulos_previos.append(rect)  # Agregar rectángulo actual a la lista

    return area_total
