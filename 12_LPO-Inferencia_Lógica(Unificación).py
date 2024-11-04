#21110344  David López Rojas  6E2

def unificar(exp1, exp2):
    """Intenta unificar dos expresiones."""
    if exp1 == exp2:
        return {}  # Las expresiones son idénticas, no se necesita sustitución.

    # Si una de las expresiones es una variable, se unifica con la otra.
    if es_variable(exp1):
        return {exp1: exp2}
    if es_variable(exp2):
        return {exp2: exp1}

    # Si ambas expresiones son compuestas (no son variables)
    if isinstance(exp1, tuple) and isinstance(exp2, tuple):
        if exp1[0] != exp2[0]:  # Comprobar si los operadores son iguales
            return None  # No se pueden unificar

        # Unificar los argumentos
        if len(exp1) != len(exp2):
            return None  # Diferente número de argumentos

        substitution = {}
        for arg1, arg2 in zip(exp1[1:], exp2[1:]):
            result = unificar(arg1, arg2)
            if result is None:
                return None  # No se puede unificar
            # Aplicar la sustitución
            substitution.update(result)

        return substitution

    return None  # No se puede unificar

def es_variable(exp):
    """Verifica si una expresión es una variable."""
    return isinstance(exp, str) and exp.islower()  # Variables son letras minúsculas

# Ejemplo de uso
# Expresiones a unificar
exp1 = ('P', 'x', 'y')  # P(x, y)
exp2 = ('P', 'a', 'b')  # P(a, b)

# Intentar unificar
sustitucion = unificar(exp1, exp2)

# Imprimir resultados
if sustitucion is not None:
    print("Se puede unificar con la siguiente sustitución:")
    for var, val in sustitucion.items():
        print(f"{var} -> {val}")
else:
    print("No se puede unificar.")
