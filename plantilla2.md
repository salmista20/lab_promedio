**Rol:** Actúa como un ingeniero de QA especializado en pruebas unitarias con `[framework_testing, ej. pytest]` en `[lenguaje, ej. Python]`.

**Tarea:** Genera una suite completa de tests unitarios para `[nombre_funcion_o_clase]` ubicada dentro de las etiquetas `<codigo>`, diseñando casos que validen tanto el flujo normal como los valores frontera descritos en sus reglas.

**Contexto:** El archivo de pruebas se guardará como `[nombre_archivo_test]` y se ejecutará mediante `[comando_ejecucion]`. El objetivo es garantizar que [objetivo_de_calidad].

**Reglas:**
- Importa el módulo usando `[instruccion_import]`.
- Usa únicamente `[dependencias_permitidas]`.
- Incluye obligatoriamente pruebas para:
  1. Casos normales de éxito: [listar_casos_normales].
  2. Casos límite y valores frontera: [listar_valores_frontera_criticos].
  3. Manejo de errores y excepciones: [listar_errores_y_mensajes_esperados].
- Usa nombres de funciones descriptivos (`test_<escenario>`).

**Formato:** Devuelve únicamente código válido y listo para guardar en `[nombre_archivo_test]`, sin explicaciones adicionales fuera de los comentarios del código.

**Ejemplo de estructura esperada:**
