def reverse_string(s):
    arr = list(s)      # convert to list
    
    # fill this part — you already know this!
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right]= arr[right], arr[left]
        left += 1
        right -= 1
    
    return "".join(arr)

print(reverse_string("hello"))   
print(reverse_string("pranav"))  
#IMPORTANT NOTES

# s = "Hello World"

# s.lower()        # "hello world"
# s.upper()        # "HELLO WORLD"
# s.strip()        # removes spaces from both ends
# s.split(" ")     # ["Hello", "World"]
# s.replace("l","x") # "Hexxo Worxd"
# s.count("l")     # 3
# s.startswith("He") # True
# "llo" in s       # True — O(n)