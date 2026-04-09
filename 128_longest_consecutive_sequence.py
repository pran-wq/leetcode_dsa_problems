# Given an unsorted array of integers, find the length of the longest consecutive elements sequence
arr = [105,101,102,103,104,105,107,1,2,3,4]
def find_sequence(arr):
    num_set = set(arr)
    longest = 0
    for num in num_set:
        if num-1 not in num_set:
            current = num
            length =1
            while current +1 in num_set:
                current+=1
                length +=1
            longest= max(longest,length)
    return longest
print(find_sequence(arr))           
