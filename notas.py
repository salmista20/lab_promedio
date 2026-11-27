"""Cálculo del promedio final de un curso universitario (escala de 0 a 20)."""


def calcular_promedio_final(practicas, parcial, final):
    """Devuelve el promedio final del curso y si el estudiante aprobó.

    Reglas del curso:
    - Todas las notas van de 0 a 20.
    - Si hay más de tres prácticas, se elimina la más baja.
    - Promedio = 50 % prácticas + 25 % examen parcial + 25 % examen final.
    - El promedio se redondea al entero más cercano; 0.5 sube (10.5 -> 11).
    - Se aprueba con 11 o más.
    """
    if len(practicas) == 0:
        raise ValueError("Se necesita al menos una práctica")
    for p in practicas:
        if p < 0 or p > 20:
            raise ValueError("Nota de práctica fuera de rango: " + str(p))
    if parcial < 0 or parcial > 20:
        raise ValueError("Nota del parcial fuera de rango: " + str(parcial))
    if final < 0 or final > 20:
        raise ValueError("Nota del final fuera de rango: " + str(final))

    notas = list(practicas)
    if len(notas) > 3:
        menor = notas[0]
        for n in notas:
            if n < menor:
                menor = n
        notas.remove(menor)

    suma = 0
    for n in notas:
        suma = suma + n
    promedio_practicas = suma / len(notas)

    promedio = promedio_practicas * 0.5 + parcial * 0.25 + final * 0.25
    nota_final = round(promedio)

    if nota_final >= 11:
        aprobado = True
    else:
        aprobado = False

    return {"promedio": nota_final, "aprobado": aprobado}


