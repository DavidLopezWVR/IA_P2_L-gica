#21110344  David López Rojas  6E2

from sympy import symbols, And, Or, Not, Implies, Equivalent, satisfiable, simplify_logic

# Definir símbolos
p, q, r = symbols('p q r')

# Definir proposiciones lógicas usando los operadores de SymPy
proposicion1 = Equivalent(p, Or(Not(q), r))  # p ↔ (¬q ∨ r)
proposicion2 = Or(Not(p), And(q, Not(r)))    # ¬p ∨ (q ∧ ¬r)
proposicion3 = Implies(p, q)                 # p → q

# Verificar si proposición 1 y proposición 2 son equivalentes
if proposicion1.equivalent(proposicion2):
    print("Las proposiciones 1 y 2 son equivalentes.")
else:
    print("Las proposiciones 1 y 2 no son equivalentes.")

# Verificar si la proposición 3 es válida (es decir, siempre verdadera en todas las interpretaciones)
if proposicion3.is_valid():
    print("La proposición 3 es válida.")
else:
    print("La proposición 3 no es válida.")

# Verificar si existe una asignación que haga la conjunción p ∧ q ∧ r verdadera (satisfacibilidad)
satisfacible = satisfiable(p & q & r)
if satisfacible:
    print("Las variables pueden satisfacerse para que la proposición sea verdadera.")
else:
    print("No hay asignación de variables que satisfaga la proposición.")
