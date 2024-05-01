def reverse(array, n_times):
    low = 0 
    high = 1 
    while low<high:
        temp=array[low]
        array[low] = array[high]
        array[high] = temp 
        low+=1
        high-=1 
    return array 

array = [10, 5, 7, 30]

reverse = reverse(array, 5)
print(reverse)