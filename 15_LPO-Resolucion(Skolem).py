#21110344  David López Rojas  6E2

class Formula:
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.expression


def skolemize(formula):
    # Función recursiva para realizar la skolemización
    def recursive_skolemize(expr, universal_vars):
        if '∀' in expr:  # Encontrar cuantificador universal
            var = expr[expr.index('∀') + 1]  # Obtener la variable
            rest_expr = expr[expr.index('∀') + 2:].strip()
            return f"∀{var}({recursive_skolemize(rest_expr, universal_vars + [var])})"
        
        if '∃' in expr:  # Encontrar cuantificador existencial
            var = expr[expr.index('∃') + 1]  # Obtener la variable
            rest_expr = expr[expr.index('∃') + 2:].strip()
            skolem_func = f"f({'_'.join(universal_vars)})"  # Crear función de Skolem
            return recursive_skolemize(rest_expr, universal_vars) \
                   .replace(var, skolem_func)  # Reemplazar con la función de Skolem
        
        return expr  # Si no hay más cuantificadores, retornar la expresión original

    return Formula(recursive_skolemize(formula.expression, []))


# Ejemplo de uso
formula = Formula("∀x (P(x) → ∃y Q(x, y))")
print("Fórmula original:", formula)
skolemized_formula = skolemize(formula)
print("Fórmula después de la skolemización:", skolemized_formula)