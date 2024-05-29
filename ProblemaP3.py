from collections import deque
import heapq
import sys

def fitness(stack):
    return sum(1 for i in range(len(stack) - 1) if stack[i] < stack[i + 1])

def flip(arr, k):
    """Función auxiliar para voltear el array desde 0 hasta k"""
    return arr[:k] + arr[k:][::-1]


def generate_permutations(arr):
    """Generates all permutations by performing all possible flips on the current permutation."""
    permutations = []
    for i in range(len(arr)):
        new_arr = arr[:]
        new_arr = flip(new_arr, i)
        permutations.append((tuple(new_arr), i))
    return permutations

def pancake_graph_sort(arr):
    """Sorts the array using the Pancake graph approach and returns the sequence of flips."""
    n = len(arr)
    target = tuple(sorted(arr, reverse=True))
    start = tuple(arr)
    
    if start == target:
        return []
    
    # heap = []
    # heapq.heappush(heap, (fitness(start), start, []))
    queue = deque([(start, [])])
    visited = set([start])
    i = 0
    while queue:
        # _,current, flips = heapq.heappop(heap)
        current,flips = queue.popleft()
        
        for new_perm, flip_index in generate_permutations(list(current)):
            if new_perm == target:
                return flips + [flip_index + 1]
            if new_perm not in visited:
                visited.add(new_perm)
                # heapq.heappush(heap, (fitness(new_perm),new_perm, flips + [flip_index + 1]))
                queue.append((fitness(new_perm), new_perm, flips + [flip_index + 1]))
        i += 1
        
    return []

def pancake_sort_greedy(arr):
    answer = []
    greatest_element = len(arr)
    
    for index in range(len(arr)):
        index_largest_element = arr.index(greatest_element - index)
        
        if index_largest_element == index: continue
        
        #reverse the array from the nth index
        arr = flip(arr, index_largest_element)
        # arr = arr[:index_largest_element] + arr[index_largest_element:][::-1]
        
        if index_largest_element != len(arr)-1:
            answer.append(index_largest_element)
            
        #reverse the full array
        arr = flip(arr, index)
        # arr = arr[:index] + arr[index:][::-1]
        
        answer.append(index)
    
    return answer

# arreglo = []
# for i in range(1, 1000+1):
#     arreglo.append(i)
# random.shuffle(arreglo)

# # arreglo = [1, 4, 3, 2, 5]

# print("Arreglo desordenado:", arreglo)  # This should print the shuffled array [5, 4, 3, 2, 1]

# flips = pancake_sort_greedy(arreglo)

# print("Secuencia de flips:", flips)
# #print("Arreglo ordenado:", sorted(arreglo, reverse=True))  # This should print the sorted array [5, 4, 3, 2, 1]
# # print(arreglo)

# for i in flips:
#     arreglo = flip(arreglo,i)
    
# print("comprobacion: ", arreglo)

def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    
    for i in range(0, ncasos):
        numeros = [int(num) for num in linea.split()]
        if len(numeros) > 10:
            respuesta = pancake_graph_sort(numeros)
        else:
            respuesta = pancake_sort_greedy(numeros)
            
        if len(respuesta) == 0:
         answer = "ORDENADO"
        else:
            ans = []
            for i in respuesta:
                ans.append(str(i))
                
            answer = " ".join(ans)
            
        print(answer)
        linea = sys.stdin.readline()

main()


