#leetcode 217
# Given an array, return True if any value 
# appears at least twice.

# arr = [1,2,3,1]    → True
# arr = [1,2,3,4]    → False
# arr = [1,1,1,3,3,4,3,2,4,2] → True

def find_repeat(arr):
    seen =set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False

    
print(find_repeat([1,2,3,2]))               # should be True
        
        