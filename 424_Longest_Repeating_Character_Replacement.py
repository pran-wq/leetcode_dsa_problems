# LeetCode 424 - Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
#
# Description:
# Given a string s and an integer k, you can replace at most k characters.
# Find the length of the longest substring containing the same letter
# after at most k replacements.
#
# Technique: Sliding Window + HashMap
# Time Complexity: O(n)
# Space Complexity: O(1)
def characterReplacement(s,k):
    left =0
    max_length = 0
    max_freq=0
    char_freq = {}
    for right in range(len(s)):
        char_freq[s[right]] = char_freq.get(s[right],0)+1
        max_freq= max(max_freq, char_freq[s[right]])
        while (right-left+1) - max_freq > k:
            char_freq[s[left]] -=1
            left +=1
        max_length =max(max_length, right -left+1)
    return max_length
print(characterReplacement("AABABBA",1))