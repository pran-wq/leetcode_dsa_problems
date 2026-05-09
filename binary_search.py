arr = [1, 3, 5, 7, 9, 11, 13]
def binary_search(arr,target):
    left = 0
    right = len(arr)-1
    while left<= right:
        mid = (left + right)//2
        if arr[mid]== target:
            return mid
        elif left< target:
            left = mid+1
        else:
            right = mid -1
    return-1
print(binary_search(arr, 7))   
print(binary_search(arr, 11))  
print(binary_search(arr, 4))
        