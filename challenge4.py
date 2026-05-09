# Find TWO numbers that add up to a target
# Return their INDICES

arr = [2, 7, 11, 15]
target = 9

# Move all zeros to the END
# without creating a new array!


arr = [0, 1, 0, 3, 12]
def move_zero(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr.pop(i)
            arr.append(0)
    return arr

print(move_zero([0, 0, 1]))
arr = [0, 1, 0, 3, 12]
def move_zero(arr):
    place = 0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[place]= arr[i]
            place +=1
    for i in range (place, len(arr)):
        arr[i]=0
    return arr
print(move_zero(arr))

