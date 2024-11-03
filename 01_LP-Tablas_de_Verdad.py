#21110344  David López Rojas  6E2

import itertools

# Función para generar todas las combinaciones de valores booleanos para un número dado de variables
def generate_truth_table(num_vars):
    # Se utiliza itertools.product para crear el producto cartesiano de [True, False] repetido num_vars veces.
    truth_values = list(itertools.product([True, False], repeat=num_vars))
    return truth_values

# Función para imprimir una tabla de verdad para una expresión lógica dada
def print_truth_table(expression):
    # Se cuenta el número de variables 'A', 'B', 'C', etc., en la expresión para determinar el número de columnas en la tabla de verdad
    num_vars = expression.count('A')  # Esta línea solo cuenta 'A', lo que limita el número de variables a 1 (debería considerarse una mejora)
    
    # Se generan todas las combinaciones de valores booleanos
    truth_table = generate_truth_table(num_vars)
    
    # Se prepara el encabezado para la tabla, reemplazando términos lógicos por símbolos
    header = expression.replace('(', '').replace(')', '').replace('and', '∧').replace('or', '∨').replace('not', '¬')
    print(f"{'|'.join(header):^{2*num_vars + len(header) + 1}} | Resultado")
    print('-' * (2*num_vars + len(header) + 12))
    
    # Se evalúan las expresiones lógicas para cada combinación de valores booleanos
    for row in truth_table:
        # Se crea un diccionario de valores para las variables usando sus posiciones
        values_dict = {chr(65 + i): value for i, value in enumerate(row)}
        # Se convierte cada valor de la fila a cadena
        values_str = [str(value) for value in row]
        # Se evalúa la expresión lógica con los valores actuales
        eval_expression = expression.format(**values_dict)
        print(f"{'|'.join(values_str):^10} | {'True' if eval(eval_expression) else 'False':^8}")

# Ejemplos de expresiones lógicas
expressions = [
    "not A",
    "A and B",
    "A or B",
    "A or (B and C)"
]

# Generar y mostrar las tablas de verdad para las expresiones dadas
for expression in expressions:
    print(f"Tabla de verdad para la expresión: {expression}")
    print_truth_table(expression)
    print()
