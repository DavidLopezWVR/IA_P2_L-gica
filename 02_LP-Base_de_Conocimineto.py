#21110344  David López Rojas  6E2

import itertools

# Función para generar todas las combinaciones de valores booleanos para un número dado de variables
def generate_truth_table(num_vars):
    # Utiliza itertools.product para crear el producto cartesiano de [True, False] repetido num_vars veces.
    truth_values = list(itertools.product([True, False], repeat=num_vars))
    return truth_values

# Función para imprimir una tabla de verdad para una expresión lógica dada
def print_truth_table(expression):
    # Cuenta el número de variables 'A' en la expresión (limitado a solo 'A' en este contexto)
    num_vars = expression.count('A')  # Se asume que las variables se representan como 'A', 'B', 'C', ...
    
    # Genera la tabla de verdad usando el número de variables
    truth_table = generate_truth_table(num_vars)
    
    # Prepara el encabezado para la tabla, reemplazando términos lógicos por símbolos matemáticos
    header = expression.replace('(', '').replace(')', '').replace('and', '∧').replace('or', '∨').replace('not', '¬')
    print(f"{'|'.join(header):^{2*num_vars + len(header) + 1}} | Resultado")
    print('-' * (2*num_vars + len(header) + 12))
    
    # Itera sobre cada combinación de valores booleanos
    for row in truth_table:
        # Crea un diccionario que asocia cada variable con su valor correspondiente en la combinación actual
        values_dict = {chr(65 + i): value for i, value in enumerate(row)}
        # Convierte los valores booleanos a cadenas para la impresión
        values_str = [str(value) for value in row]
        # Evalúa la expresión lógica con los valores actuales usando el formato del diccionario
        eval_expression = expression.format(**values_dict)
        # Imprime los valores y el resultado de la evaluación de la expresión
        print(f"{'|'.join(values_str):^10} | {'True' if eval(eval_expression) else 'False':^8}")

# Ejemplos de expresiones lógicas
expressions = [
    "not A",
    "A and B",
    "A or B",
    "A or (B and C)"
]

# Genera y muestra las tablas de verdad para las expresiones dadas
for expression in expressions:
    print(f"Tabla de verdad para la expresión: {expression}")
    print_truth_table(expression)
    print()
