# LeetCode 383 - Ransom Note
# https://leetcode.com/problems/ransom-note/
#
# Description:
# Given two strings ransomNote and magazine,
# return True if ransomNote can be constructed
# using letters from magazine.
# Each letter in magazine can only be used once.
#
# Technique: Hash Map / Frequency Count
# Time Complexity: O(n)
# Space Complexity: O(1)

def can_construct(r,m):
    freq={}
    for char in m:
        freq[char]=freq.get(char,0)+1
    for char in r:
        if char  not in freq:
            return False
        elif freq[char]<1:
            return False
        freq[char]-=1
    else:
        return True
print(can_construct("ac","aabb"))
