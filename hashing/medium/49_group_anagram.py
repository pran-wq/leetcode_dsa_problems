# LeetCode 49 - Group Anagrams
# https://leetcode.com/problems/group-anagrams/
#
# Description:
# Given an array of strings, group the anagrams together.
# An anagram is a word formed by rearranging the letters of another word.
#
# Technique: Hash Map + Sorting
# Time Complexity: O(n * k log k)
# n = number of words, k = length of each word
# Space Complexity: O(n)

def group_anagrams(words):
    group ={}
    for word in words:
        key = "".join(sorted(word))
        if key not in group:
            group[key]=[]
        group[key].append(word)
    return list(group.values())
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
