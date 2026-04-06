'''Given two strings s and t, 
return True if t is an anagram of s.'''

from collections import Counter
def are_anagram(s,t):
    if len(s)!= len(t):
        return False
    freq = Counter(s)
    for c in t:
        freq[c]= freq.get(c,0)-1
    if freq.values !=0:
        return False
    return all(v == 0 for v in freq.values())
print(are_anagram("anagram","nagaram" ))





