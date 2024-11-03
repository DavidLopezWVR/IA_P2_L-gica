#21110344  David López Rojas  6E2

import random
import math

def funcion_objetivo(x):
    # Función objetivo que se desea maximizar
    # En este caso, es una función cuadrática simple: -x^2 + 5*x + 10
    return -x**2 + 5*x + 10

def hill_climbing(funcion_objetivo, paso=0.1, intentos_maximos=1000):
    # Algoritmo de Hill Climbing para encontrar un máximo local de la función objetivo

    # Inicialización aleatoria de x en el intervalo [-10, 10]
    x = random.uniform(-10, 10)
    valor_actual = funcion_objetivo(x)  # Calcula el valor inicial de la función objetivo

    # Itera hasta alcanzar el número máximo de intentos
    for _ in range(intentos_maximos):
        # Genera un pequeño cambio aleatorio en x en el rango [-paso, paso]
        paso_x = random.uniform(-paso, paso)
        nuevo_x = x + paso_x  # Nuevo candidato de x
        nuevo_valor = funcion_objetivo(nuevo_x)  # Calcula el valor de la función objetivo para el nuevo x

        # Si el nuevo valor es mayor, actualiza x y el valor actual
        if nuevo_valor > valor_actual:
            x, valor_actual = nuevo_x, nuevo_valor

    return x, valor_actual  # Retorna el punto máximo local y su valor correspondiente

# Ejemplo de uso
x_maximo, valor_maximo = hill_climbing(funcion_objetivo)

# Imprime el máximo local encontrado
print("Máximo local encontrado en x = {:.2f} con un valor de {:.2f}".format(x_maximo, valor_maximo))
