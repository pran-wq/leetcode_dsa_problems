'''Given two strings ransomNote and magazine,
return True if ransomNote can be constructed 
using letters from magazine.
Each letter in magazine can only be used ONCE!'''

def can_construct(r,m):
    freq={}
    for char in m:
        freq[char]=freq.get(char,0)+1
    for char in r:
        if char  not in m:
            return False
        elif freq[char]<0:
            return False
        freq[char]-=1
    else:
        return True
print(can_construct("ac","aabb"))