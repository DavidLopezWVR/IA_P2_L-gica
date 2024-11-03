#21110344  David López Rojas  6E2

class MotorInferencia:
    def __init__(self, base_conocimiento):
        # Inicializa el motor de inferencia con una base de conocimiento, que es un conjunto de reglas
        self.base_conocimiento = base_conocimiento

    def encadenamiento_hacia_adelante(self, hechos):
        # Método para realizar inferencia por encadenamiento hacia adelante
        # Comienza con un conjunto de hechos y trata de derivar nuevos hechos usando la base de conocimiento

        nuevos_hechos = hechos.copy()  # Copia de los hechos iniciales para ir agregando nuevos hechos
        cambios = True  # Bandera para saber si se han agregado nuevos hechos

        # Ciclo que continúa hasta que no se agreguen más hechos nuevos
        while cambios:
            cambios = False  # Se reinicia la bandera de cambios
            for regla in self.base_conocimiento:
                antecedentes, consecuente = regla[:-1], regla[-1]  # Divide cada regla en antecedentes y consecuente
                # Verifica si todos los antecedentes están en los hechos y el consecuente aún no lo está
                if all(antecedente in hechos for antecedente in antecedentes) and consecuente not in hechos:
                    nuevos_hechos.add(consecuente)  # Agrega el consecuente a los hechos
                    cambios = True  # Marca que hubo cambios para continuar el ciclo

        return nuevos_hechos  # Retorna el conjunto de hechos, incluyendo los nuevos hechos derivados

    def encadenamiento_hacia_atras(self, meta, hechos):
        # Método para realizar inferencia por encadenamiento hacia atrás
        # Intenta demostrar la meta a partir de los hechos y la base de conocimiento

        if meta in hechos:
            return True  # Si la meta ya está en los hechos, la meta es verdadera
        else:
            for regla in self.base_conocimiento:
                antecedentes, consecuente = regla[:-1], regla[-1]  # Divide cada regla en antecedentes y consecuente
                if consecuente == meta:
                    # Verifica recursivamente si todos los antecedentes pueden demostrarse
                    if all(self.encadenamiento_hacia_atras(antecedente, hechos) for antecedente in antecedentes):
                        return True  # Si todos los antecedentes son demostrables, la meta es alcanzable
            return False  # Si no se puede demostrar la meta, devuelve False

# Ejemplo de uso
base_conocimiento = {('P', 'Q'), ('Q', 'R'), ('R', 'S')}
motor = MotorInferencia(base_conocimiento)

# Encadenamiento hacia adelante
hechos_iniciales = {'P'}
nuevos_hechos = motor.encadenamiento_hacia_adelante(hechos_iniciales)
print("Hechos tras encadenamiento hacia adelante:", nuevos_hechos)

# Encadenamiento hacia atrás
meta = 'S'
resultado = motor.encadenamiento_hacia_atras(meta, hechos_iniciales)
print("¿Se puede demostrar la meta 'S'?", resultado)
