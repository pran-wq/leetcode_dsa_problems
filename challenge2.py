# Check if an array is a palindrome
# arr = [1, 2, 3, 2, 1]  → True
# arr = [1, 2, 3, 4, 5]  → False
arr = [1, 2, 3, 4, 5] 
def is_pallendrome(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] !=arr[right]:
            return False
        right -=1
        left +=1
    return True
print(is_pallendrome(arr))


        