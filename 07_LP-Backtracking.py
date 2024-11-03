#21110344  David  López 6E2

class NReinas:
    def __init__(self, N):
        # Inicializa el tamaño del tablero y crea una matriz de NxN con ceros, donde 0 representa una celda vacía.
        self.N = N
        self.tablero = [[0] * N for _ in range(N)]

    def es_seguro(self, fila, columna):
        # Comprueba si es seguro colocar una reina en la posición (fila, columna)

        # Verifica si no hay otra reina en la misma fila a la izquierda
        for i in range(columna):
            if self.tablero[fila][i] == 1:
                return False

        # Verifica si no hay otra reina en la diagonal superior izquierda
        for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
            if self.tablero[i][j] == 1:
                return False

        # Verifica si no hay otra reina en la diagonal inferior izquierda
        for i, j in zip(range(fila, self.N, 1), range(columna, -1, -1)):
            if self.tablero[i][j] == 1:
                return False

        return True  # Devuelve True si no hay conflictos con otras reinas

    def resolver_n_reinas_util(self, columna):
        # Intenta colocar una reina en cada fila de la columna actual y avanza a la siguiente columna recursivamente

        # Caso base: si todas las columnas están cubiertas, la solución es completa
        if columna >= self.N:
            return True

        # Recorre todas las filas en la columna actual
        for i in range(self.N):
            # Si es seguro colocar una reina en (i, columna), procede
            if self.es_seguro(i, columna):
                self.tablero[i][columna] = 1  # Coloca una reina en la posición (i, columna)

                # Realiza una llamada recursiva para colocar la siguiente reina en la siguiente columna
                if self.resolver_n_reinas_util(columna + 1):
                    return True  # Si se encuentra una solución completa, retorna True

                # Si no se encuentra solución, se elimina la reina de la posición actual (backtracking)
                self.tablero[i][columna] = 0

        return False  # Devuelve False si no es posible colocar una reina en ninguna fila de esta columna

    def resolver_n_reinas(self):
        # Inicia la resolución del problema de N reinas llamando a la función auxiliar con la primera columna
        if not self.resolver_n_reinas_util(0):
            print("No hay solución para {} reinas en un tablero de tamaño {}x{}.".format(self.N, self.N, self.N))
            return False  # Indica que no se encontró una solución

        self.imprimir_tablero()  # Si se encontró una solución, imprime el tablero resultante
        return True  # Retorna True indicando que se encontró una solución

    def imprimir_tablero(self):
        # Imprime el tablero en la consola, mostrando la posición de las reinas
        for fila in self.tablero:
            print(' '.join(map(str, fila)))


# Ejemplo de uso
n = 8
n_reinas = NReinas(n)
n_reinas.resolver_n_reinas()
