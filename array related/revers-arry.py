def reverse(array):
    low = 0 
    high = len(array) - 1 
    while low < high:
        temp = array[low]
        array[low] = array[high]
        array[high] = temp 
        low += 1
        high -= 1 
    return array 

array = [10, 5, 7, 30]

reversed_array = reverse(array)
print(reversed_array)
