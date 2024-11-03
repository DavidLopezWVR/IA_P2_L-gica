#21110344  David López Rojas  6E2

class MotorInferencia:
    # Constructor que inicializa el motor de inferencia con una base de conocimiento
    def __init__(self, base_conocimiento):
        self.base_conocimiento = base_conocimiento

    # Método principal que intenta resolver una pregunta dada usando la base de conocimiento
    def resolver(self, pregunta):
        # Negar la pregunta para poder probarla usando resolución
        clausula_negada = self.negar_pregunta(pregunta)
        # Se crea una lista de cláusulas completa combinando la base de conocimiento con la pregunta negada
        clausula_completa = self.base_conocimiento + clausula_negada

        # Bucle principal de resolución
        while True:
            # Genera nuevas cláusulas a partir de la combinación de las cláusulas existentes
            nueva_clausula = self.generar_nuevas_clausulas(clausula_completa)
            if not nueva_clausula:
                # Si no se generan nuevas cláusulas, no se puede inferir la pregunta, así que se retorna False
                return False
            if set(nueva_clausula).issubset(clausula_completa):
                # Si las nuevas cláusulas ya están en la base, la pregunta es deducible y se retorna True
                return True
            # Añade las nuevas cláusulas a la lista completa de cláusulas
            clausula_completa += nueva_clausula

    # Método para negar cada predicado en la pregunta (por ejemplo, ['R'] se convierte en ['~R'])
    def negar_pregunta(self, pregunta):
        return ['~' + predicado for predicado in pregunta]

    # Método que genera nuevas cláusulas mediante la resolución de pares de cláusulas
    def generar_nuevas_clausulas(self, clausulas):
        nuevas_clausulas = []
        # Itera sobre todas las combinaciones posibles de cláusulas para aplicar la resolución
        for i, clausula1 in enumerate(clausulas):
            for j, clausula2 in enumerate(clausulas):
                if i != j:
                    # Intenta resolver las dos cláusulas seleccionadas
                    resolvente = self.resolver_clausulas(clausula1, clausula2)
                    # Si la resolución da una nueva cláusula, y no está en las listas actuales, se añade
                    if resolvente and resolvente not in clausulas and resolvente not in nuevas_clausulas:
                        nuevas_clausulas.append(resolvente)
        return nuevas_clausulas

    # Método para resolver dos cláusulas y encontrar una cláusula resolvente
    def resolver_clausulas(self, clausula1, clausula2):
        for predicado in clausula1:
            # Determina el complemento del predicado (por ejemplo, el complemento de 'P' es '~P')
            if predicado.startswith('~'):
                complemento = predicado[1:]
            else:
                complemento = '~' + predicado
            # Verifica si el complemento está en la segunda cláusula
            if complemento in clausula2:
                # Crea una nueva cláusula resolvente eliminando el predicado y su complemento
                clausula_resultante = clausula1.copy()
                clausula_resultante.remove(predicado)
                clausula_resultante.remove(complemento)
                # Si la cláusula resolvente está vacía, se ha encontrado una contradicción, lo que indica que la pregunta es deducible
                if not clausula_resultante:
                    return ['Resuelto']
                else:
                    return clausula_resultante
        # Si no hay resolución posible entre las dos cláusulas, retorna None
        return None


# Ejemplo de uso del motor de inferencia
base_conocimiento = [['P'], ['~P', 'Q'], ['~Q', 'R']]
motor = MotorInferencia(base_conocimiento)

# Pregunta que se desea resolver
pregunta = ['R']
resultado = motor.resolver(pregunta)

# Imprimir resultado
if resultado:
    print("La pregunta es verdadera.")
else:
    print("La pregunta es falsa.")
