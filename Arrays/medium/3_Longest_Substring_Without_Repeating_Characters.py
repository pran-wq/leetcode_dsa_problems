# LeetCode 3 - Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Description:
# Given a string s, find the length of the longest substring
# without repeating characters.
#
# Technique: Sliding Window + HashSet
# Time Complexity: O(n)
# Space Complexity: O(n)
def lengthOfLongestSubstring(s):
    char_set=set()
    left = 0
    max_length=0
    for right in range (len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_length= max(max_length,right-left+1)
    return max_length
            
print(lengthOfLongestSubstring("aabcddca"))           
    



