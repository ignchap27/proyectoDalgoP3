from heapq import heappop, heappush

def find_inversions(stack):
    """ Cuenta el número de inversiones en la pila de panqueques """
    inversions = 0
    for i in range(len(stack)):
        for j in range(i + 1, len(stack)):
            if stack[i] > stack[j]:
                inversions += 1
    return inversions

def flip(stack, k):
    """ Devuelve una nueva pila que resulta de realizar un flip en el índice k """
    return stack[:k] + stack[k:][::-1]

def pancake_sort_a_star(stack):
    """ Implementación del A* para ordenar panqueques """
    # Estado inicial
    initial = (stack, 0, find_inversions(stack), [])  # (estado, g(n), h(n), path)
    open_set = []
    heappush(open_set, (initial[1] + initial[2], initial))  # (f(n), nodo)
    
    goal = sorted(stack, reverse=True)
    i = 0
    while i < 100:
        _, (current_stack, g_n, _, path) = heappop(open_set)
        
        if current_stack == goal:
            return path
        
        for k in range(2, len(current_stack) + 1):
            new_stack = flip(current_stack, k)
            if new_stack != current_stack:
                new_g_n = g_n + 1
                new_h_n = find_inversions(new_stack)
                new_path = path + [k]
                heappush(open_set, (new_g_n + new_h_n, (new_stack, new_g_n, new_h_n, new_path)))
        
        i += 1
    
    return heappop(open_set)  # En caso de que no haya solución, lo cual es teóricamente imposible en este contexto

# Ejemplo de uso
pancakes = [1, 4, 3, 2, 5]
solution = pancake_sort_a_star(pancakes)
print("Secuencia de flips:", solution)
