import pytest
from notas import calcular_promedio_final


def test_aprobado_tres_practicas_sin_eliminar():
    resultado = calcular_promedio_final([14, 14, 14], 14, 14)
    assert resultado == {"promedio": 14, "aprobado": True}


def test_elimina_practica_mas_baja_con_cuatro_notas():
    # Elimina el 5; promedio de [15, 15, 15] = 15 -> 15*0.5 + 12*0.25 + 14*0.25 = 14.0
    resultado = calcular_promedio_final([15, 5, 15, 15], 12, 14)
    assert resultado == {"promedio": 14, "aprobado": True}


def test_elimina_solo_una_practica_si_hay_empate_en_la_menor():
    # Elimina solo un 10; promedio de [10, 13, 13] = 12 -> 12*0.5 + 12*0.25 + 12*0.25 = 12.0
    resultado = calcular_promedio_final([10, 10, 13, 13], 12, 12)
    assert resultado == {"promedio": 12, "aprobado": True}


def test_frontera_redondeo_mitad_hacia_arriba_aprueba():
    # Prácticas: 11, Parcial: 10, Final: 10 -> 11*0.5 + 10*0.25 + 10*0.25 = 10.5 -> debe subir a 11
    resultado = calcular_promedio_final([11, 11, 11], 10, 10)
    assert resultado == {"promedio": 11, "aprobado": True}


def test_frontera_debajo_de_mitad_desaprueba():
    # Prácticas: 10, Parcial: 11, Final: 10 -> 10*0.5 + 11*0.25 + 10*0.25 = 10.25 -> baja a 10
    resultado = calcular_promedio_final([10, 10, 10], 11, 10)
    assert resultado == {"promedio": 10, "aprobado": False}


def test_valores_extremos_cero_y_veinte():
    assert calcular_promedio_final([0, 0, 0], 0, 0) == {"promedio": 0, "aprobado": False}
    assert calcular_promedio_final([20, 20, 20], 20, 20) == {"promedio": 20, "aprobado": True}


def test_error_practicas_vacias():
    with pytest.raises(ValueError, match="Se necesita al menos una práctica"):
        calcular_promedio_final([], 12, 12)


@pytest.mark.parametrize("practicas,parcial,final,mensaje", [
    ([-1, 12, 12], 12, 12, "Nota de práctica fuera de rango"),
    ([21, 12, 12], 12, 12, "Nota de práctica fuera de rango"),
    ([12, 12, 12], -0.5, 12, "Nota del parcial fuera de rango"),
    ([12, 12, 12], 12, 20.1, "Nota del final fuera de rango"),
])
def test_error_notas_fuera_de_rango(practicas, parcial, final, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        calcular_promedio_final(practicas, parcial, final)
