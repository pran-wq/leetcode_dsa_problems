# LeetCode 242 - Valid Anagram
# https://leetcode.com/problems/valid-anagram/
#
# Approach:
# Count the frequency of characters in string s using Counter.
# Decrease the frequency while iterating through string t.
# If all frequencies become zero, the strings are anagrams.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

def are_anagram(s,t):
    freq={}
    if len(s)!= len(t):
        return False
    for char in s:
        freq[char]=freq.get(char,0)+1
    for char in t:
        if char not in freq or freq[char]==0:
            return 
        False
        freq[char]-=1
    
print(are_anagram("anagram","nagaram" ))





