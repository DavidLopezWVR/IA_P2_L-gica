#21110344  David López Rojas  6E2

class MotorInferencia:
    def __init__(self, reglas):
        self.reglas = reglas  # Lista de reglas en forma (antecedentes, consecuente)

    def encadenamiento_hacia_adelante(self, hechos):
        nuevos_hechos = hechos.copy()
        cambios = True

        while cambios:
            cambios = False
            for regla in self.reglas:
                antecedentes, consecuente = regla[:-1], regla[-1]
                if all(antecedente in nuevos_hechos for antecedente in antecedentes) and consecuente not in nuevos_hechos:
                    nuevos_hechos.add(consecuente)
                    cambios = True

        return nuevos_hechos

    def encadenamiento_hacia_atras(self, meta, hechos):
        if meta in hechos:
            return True
        else:
            for regla in self.reglas:
                antecedentes, consecuente = regla[:-1], regla[-1]
                if consecuente == meta:
                    if all(self.encadenamiento_hacia_atras(antecedente, hechos) for antecedente in antecedentes):
                        return True
            return False

# Definición de reglas: (antecedente1, antecedente2, ..., consecuente)
reglas = [
    (('P',), 'Q'),        # Si P es verdadero, entonces Q es verdadero
    (('Q',), 'R'),        # Si Q es verdadero, entonces R es verdadero
    (('R',), 'S')         # Si R es verdadero, entonces S es verdadero
]

# Crear el motor de inferencia con las reglas
motor = MotorInferencia(reglas)

# Hechos iniciales
hechos_iniciales = {'P'}

# Encadenamiento hacia adelante
nuevos_hechos = motor.encadenamiento_hacia_adelante(hechos_iniciales)
print("Hechos tras encadenamiento hacia adelante:", nuevos_hechos)

# Encadenamiento hacia atrás
meta = 'S'
resultado = motor.encadenamiento_hacia_atras(meta, nuevos_hechos)
print(f"¿Se puede demostrar la meta '{meta}'?", resultado)
