#21110344  David López Rojas  6e2

# Definimos los hechos y reglas del sistema experto

# Hechos: Los síntomas que pueden estar presentes
sintomas = {
    'fiebre': False,
    'tos': False,
    'dificultad_respiratoria': False,
    'dolor_de_garganta': False,
    'dolor_de_cabeza': False,
}

# Reglas de diagnóstico (en formato de diccionario)
reglas = {
    'gripe': ['fiebre', 'tos'],
    'resfriado': ['tos', 'dolor_de_garganta'],
    'neumonia': ['fiebre', 'dificultad_respiratoria'],
}

def diagnostico(sintomas):
    """Función que determina el diagnóstico basado en los síntomas."""
    for enfermedad, sintomas_requeridos in reglas.items():
        if all(sintomas[sintoma] for sintoma in sintomas_requeridos):
            return enfermedad
    return 'No se puede determinar un diagnóstico.'

# Simulación de entrada de síntomas
sintomas['fiebre'] = True
sintomas['tos'] = True
sintomas['dificultad_respiratoria'] = False
sintomas['dolor_de_garganta'] = False
sintomas['dolor_de_cabeza'] = False

# Ejecutar el diagnóstico
resultado = diagnostico(sintomas)

# Imprimir el resultado
print(f"El diagnóstico es: {resultado}")
