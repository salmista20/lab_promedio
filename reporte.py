"""Genera reporte.xlsx con el promedio final de cada estudiante de notas.xlsx.

Uso: python reporte.py
Requiere openpyxl (python -m pip install openpyxl).
"""

from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill

from notas import calcular_promedio_final

CARPETA = Path(__file__).resolve().parent
ENTRADA = CARPETA / "notas.xlsx"
SALIDA = CARPETA / "reporte.xlsx"

ENCABEZADOS = [
    "Estudiante", "Práctica 1", "Práctica 2", "Práctica 3", "Práctica 4",
    "Parcial", "Final", "Promedio", "Estado",
]
AZUL = PatternFill(fill_type="solid", fgColor="1F4E79")
VERDE = PatternFill(fill_type="solid", fgColor="C6EFCE")
ROJO = PatternFill(fill_type="solid", fgColor="FFC7CE")


def leer_filas(ruta):
    """Devuelve las filas de la primera hoja, sin el encabezado.

    Cada fila tiene 7 valores: nombre, práctica 1 a 4, parcial y final.
    Una práctica vacía significa que el estudiante no la rindió.
    """
    hoja = load_workbook(ruta).active
    filas = hoja.iter_rows(min_row=2, max_col=7, values_only=True)
    return [fila for fila in filas if fila[0] is not None]


def calcular_fila(fila):
    """Aplica calcular_promedio_final a una fila de notas.xlsx."""
    nombre, p1, p2, p3, p4, parcial, final = fila
    practicas = [nota for nota in (p1, p2, p3, p4) if nota is not None]
    return calcular_promedio_final(practicas, parcial, final)


def escribir_reporte(filas, resultados, ruta):
    """Escribe una fila por estudiante: verde si aprobó, rojo si no."""
    libro = Workbook()
    hoja = libro.active
    hoja.title = "Reporte"
    hoja.append(ENCABEZADOS)
    for celda in hoja[1]:
        celda.font = Font(bold=True, color="FFFFFF")
        celda.fill = AZUL

    for fila, resultado in zip(filas, resultados):
        estado = "Aprobado" if resultado["aprobado"] else "Desaprobado"
        hoja.append([*fila, resultado["promedio"], estado])
        color = VERDE if resultado["aprobado"] else ROJO
        for celda in hoja[hoja.max_row]:
            celda.fill = color

    hoja.column_dimensions["A"].width = 22
    for columna in "BCDEFGHI":
        hoja.column_dimensions[columna].width = 13
    hoja.freeze_panes = "A2"
    libro.save(ruta)


def main():
    try:
        filas = leer_filas(ENTRADA)
    except FileNotFoundError:
        print(f"No encontré {ENTRADA.name} en {CARPETA}")
        return 1

    resultados = [calcular_fila(fila) for fila in filas]

    try:
        escribir_reporte(filas, resultados, SALIDA)
    except PermissionError:
        print(f"No pude guardar {SALIDA.name}. Si está abierto en Excel, ciérralo y vuelve a ejecutar.")
        return 1

    desaprobados = [
        (fila[0], resultado["promedio"])
        for fila, resultado in zip(filas, resultados)
        if not resultado["aprobado"]
    ]
    print(f"{len(filas)} estudiantes: {len(filas) - len(desaprobados)} aprobados, {len(desaprobados)} desaprobados.")
    for nombre, promedio in desaprobados:
        print(f"  Desaprobado: {nombre} ({promedio})")
    print(f"Reporte guardado en {SALIDA.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
