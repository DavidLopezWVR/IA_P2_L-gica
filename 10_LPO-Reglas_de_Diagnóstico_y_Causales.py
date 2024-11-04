#21110344  David López Rojas  6e2

from experta import *

# Definir clase de hechos para representar síntomas de un paciente
class Sintoma(Fact):
    """Clase para los síntomas de un paciente."""
    pass

# Definir sistema experto de diagnóstico
class SistemaDiagnostico(KnowledgeEngine):
    
    # Regla causal: si el paciente tiene infección pulmonar, entonces es probable que tenga fiebre y tos
    @Rule(Sintoma(infeccion_pulmonar=True))
    def regla_causal_infeccion(self):
        self.declare(Sintoma(fiebre=True, tos=True))
        print("Regla causal aplicada: infección pulmonar -> fiebre y tos.")

    # Regla de diagnóstico: si el paciente tiene fiebre y tos, puede tener una infección pulmonar
    @Rule(Sintoma(fiebre=True), Sintoma(tos=True))
    def regla_diagnostico_infeccion(self):
        self.declare(Sintoma(infeccion_pulmonar=True))
        print("Regla de diagnóstico aplicada: fiebre y tos -> posible infección pulmonar.")

    # Regla causal: si el paciente tiene gripe, es probable que tenga fiebre, dolor de cabeza y fatiga
    @Rule(Sintoma(gripe=True))
    def regla_causal_gripe(self):
        self.declare(Sintoma(fiebre=True, dolor_cabeza=True, fatiga=True))
        print("Regla causal aplicada: gripe -> fiebre, dolor de cabeza y fatiga.")
        
    # Regla de diagnóstico: si el paciente tiene fiebre, dolor de cabeza y fatiga, puede tener gripe
    @Rule(Sintoma(fiebre=True), Sintoma(dolor_cabeza=True), Sintoma(fatiga=True))
    def regla_diagnostico_gripe(self):
        self.declare(Sintoma(gripe=True))
        print("Regla de diagnóstico aplicada: fiebre, dolor de cabeza y fatiga -> posible gripe.")
        
    # Regla de diagnóstico adicional: si el paciente tiene fiebre sin dolor de cabeza, podría ser infección pulmonar
    @Rule(Sintoma(fiebre=True), ~Sintoma(dolor_cabeza=True))
    def regla_diagnostico_fiebre_sin_dolor_cabeza(self):
        self.declare(Sintoma(infeccion_pulmonar=True))
        print("Regla de diagnóstico aplicada: fiebre sin dolor de cabeza -> posible infección pulmonar.")
        
# Crear una instancia del sistema experto
motor_diagnostico = SistemaDiagnostico()

# Ejemplo de uso
# Declarar síntomas observados
sintomas_observados = [
    Sintoma(fiebre=True),
    Sintoma(tos=True)
]

# Agregar hechos al motor de inferencia y ejecutar las reglas
motor_diagnostico.reset()
for sintoma in sintomas_observados:
    motor_diagnostico.declare(sintoma)
motor_diagnostico.run()

# Este ejemplo infiere una posible infección pulmonar y ejecuta las reglas causales y de diagnóstico correspondientes.
