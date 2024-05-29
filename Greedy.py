def flip(arr, k):
    """Función auxiliar para voltear el array desde 0 hasta k"""
    return arr[:k] + arr[k:][::-1]

def pancake_sort(arr):
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
    
    return answer, arr

# Example usage
pancakes = [1, 4, 3, 2, 5]
flips, arr = pancake_sort(pancakes)
print("Sorted pancakes:", pancakes)
print("Flips to sort the pancakes:", flips)
print("Sorted array:", arr)
