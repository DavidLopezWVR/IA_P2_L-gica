#21110344  David López Rojas  6E2

% Hechos sobre las relaciones familiares
padre(john, mary).   % John es padre de Mary.
padre(john, james).  % John es padre de James.
madre(susan, mary).  % Susan es madre de Mary.
madre(susan, james). % Susan es madre de James.

% Regla para determinar si dos personas son hermanos
hermano(X, Y) :- 
    padre(Z, X),      % Z es el padre de X.
    padre(Z, Y),      % Z también es el padre de Y.
    X \= Y.           % X y Y deben ser diferentes.

% Consulta para determinar si hay hermanos
consultar_hermanos :- 
    hermano(X, Y),                  % Busca todos los pares de hermanos.
    format('~w y ~w son hermanos.~n', [X, Y]),  % Imprime que X y Y son hermanos.
    fail.                           % Fuerza a Prolog a buscar más combinaciones.

consultar_hermanos :-                 % Si ya no hay más hermanos...
    write('No hay más hermanos.').    % Imprime un mensaje indicando que no hay más.

% Ejecución inicial
:- begin.                               % Indica el inicio de la ejecución.
    consultar_hermanos.                % Llama a la consulta para encontrar hermanos.
:- end.                                 % Indica el fin de la ejecución.
