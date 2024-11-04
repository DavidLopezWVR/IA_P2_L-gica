#21110344  David López Rojas  6E2

from sympy import symbols, Implies, And
from sympy.logic.boolalg import ForAll, Exists

# Definimos los predicados
Humano = symbols('Humano')  # Predicado "ser humano"
Mortal = symbols('Mortal')  # Predicado "ser mortal"
Socrates = symbols('Socrates')  # Individuo "Sócrates"

# 1. "Todos los humanos son mortales" (Cuantificador Universal)
# Esto se expresa como: ∀x (Humano(x) → Mortal(x))
# Para simplificar, usamos Humano e Mortal como si fueran predicados en lugar de funciones.
# En sympy, podemos usar ForAll para representar el cuantificador universal.
todos_humanos_mortales = ForAll(Humano, Implies(Humano, Mortal))

# 2. "Existe un ser humano llamado Sócrates" (Cuantificador Existencial)
# Esto se expresa como: ∃x (Humano(x) ∧ x=Socrates)
existe_socrates = Exists(Socrates, And(Humano, Socrates))

# 3. Razonamiento: Si Sócrates es humano, entonces Sócrates es mortal.
# Dado que todos los humanos son mortales y existe Sócrates que es humano,
# concluimos que Sócrates es mortal.
socrates_mortal = Implies(And(todos_humanos_mortales, existe_socrates), Mortal)

# Imprimimos las expresiones para verificar su estructura
print("Expresión de 'Todos los humanos son mortales':")
print(todos_humanos_mortales)

print("\nExpresión de 'Existe un ser humano llamado Sócrates':")
print(existe_socrates)

print("\nRazonamiento sobre 'Sócrates es mortal':")
print(socrates_mortal)

# Evaluación de la expresión de razonamiento
print("\nResultado del razonamiento sobre Sócrates:")
print("¿Sócrates es mortal?", socrates_mortal.doit())
