import random
from collections import deque

def flip(arr, k):
    """Flips the elements of arr starting from index k."""
    arr[k:] = arr[k:][::-1]


def generate_permutations(arr):
    """Generates all permutations by performing all possible flips on the current permutation."""
    permutations = []
    for i in range(len(arr)):
        new_arr = arr[:]
        flip(new_arr, i)
        permutations.append((tuple(new_arr), i))
    return permutations

def pancake_graph_sort(arr):
    """Sorts the array using the Pancake graph approach and returns the sequence of flips."""
    n = len(arr)
    target = tuple(sorted(arr, reverse=True))
    start = tuple(arr)
    
    if start == target:
        return []

    queue = deque([(start, [])])
    visited = set([start])
    i = 0
    while queue:
        current, flips = queue.popleft()
        
        for new_perm, flip_index in generate_permutations(list(current)):
            if new_perm == target:
                return flips + [flip_index + 1]
            if new_perm not in visited:
                visited.add(new_perm)
                queue.append((new_perm, flips + [flip_index + 1]))
        i += 1
        
    return []

arreglo = []
for i in range(1, 15+1):
    arreglo.append(i)
random.shuffle(arreglo)
print("Arreglo desordenado:", arreglo)  # This should print the shuffled array [5, 4, 3, 2, 1]

flips = pancake_graph_sort(arreglo)

print("Secuencia de flips:", flips)
#print("Arreglo ordenado:", sorted(arreglo, reverse=True))  # This should print the sorted array [5, 4, 3, 2, 1]
# print(arreglo)
for i in flips:
    flip(arreglo,i-1)
    
print("comprobacion: ", arreglo)





