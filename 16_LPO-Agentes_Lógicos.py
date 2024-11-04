#21110344  David López Rojas  6E2

class AgenteLogico:
    def __init__(self):
        # Base de conocimiento: (sintoma, enfermedad)
        self.base_conocimiento = {
            'tos': 'resfriado',
            'fiebre': 'gripe',
            'dolor de cabeza': 'migraña',
            'fiebre y tos': 'gripe',
            'dolor de cabeza y fiebre': 'meningitis',
        }

    def diagnosticar(self, sintomas):
        # Diagnóstico basado en síntomas presentados
        for sintoma in sintomas:
            if sintoma in self.base_conocimiento:
                return self.base_conocimiento[sintoma]
        
        return "No se puede realizar un diagnóstico."

# Ejemplo de uso del Agente Lógico
def main():
    agente = AgenteLogico()
    
    # Sintomas del paciente
    sintomas_paciente = ['tos', 'fiebre']
    
    # Diagnóstico
    diagnostico = agente.diagnosticar(sintomas_paciente)
    
    print("Síntomas presentados:", sintomas_paciente)
    print("Diagnóstico:", diagnostico)

if __name__ == "__main__":
    main()
