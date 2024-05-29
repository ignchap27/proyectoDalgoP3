import sys
import random
#Problema que dado un array de numeros de 1 - 5 en un orden aleatorio, los ordena siguendo la
#logica de voltear pancakes

def pancakeSort(arr):
    answer = []
    greatest_element = len(arr)
    
    for index in range(len(arr)):
        index_largest_element = arr.index(greatest_element - index)
        
        if index_largest_element == index: continue
        
        #reverse the array from the nth index
        arr = arr[:index_largest_element] + arr[index_largest_element:][::-1]
        
        if index_largest_element != len(arr)-1:
            answer.append(index_largest_element)
            
        #reverse the full array
        arr = arr[:index] + arr[index:][::-1]
        
        answer.append(index)
    
    if len(answer) == 0:
        return "ORDENADO"
    else:
        ans = []
        for i in answer:
            ans.append(str(i))
        return " ".join(ans)

def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    
    for i in range(0, ncasos):
        numeros = [int(num) for num in linea.split()]
        respuesta = pancakeSort(numeros)
        print(respuesta)
        linea = sys.stdin.readline()
        
def main(pancakes):
    solution = pancakeSort(pancakes)
    print("Secuencia de flips:", solution)

# pancakes = []

# for i in range(1, 1000+1):
#     pancakes.append(i)      
    
# random.shuffle(pancakes)
pancakes = [1, 4, 3, 2, 5]
print(pancakes)
main(pancakes)
# Ejemplo de uso
