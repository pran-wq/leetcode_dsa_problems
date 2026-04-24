# LeetCode 76 - Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/
#
# Description:
# Given two strings s and t, return the minimum window substring of s
# such that every character in t (including duplicates) is included.
# If no such substring exists, return an empty string "".
#
# Technique: Sliding Window + HashMap
# Time Complexity: O(n)
# Space Complexity: O(m)
def minimum_window_substring(s, t):
    from collections import Counter

    need = Counter(t)
    window = {}

    left = 0
    min_length = float('inf')
    res = ""

    required = len(need)
    formed = 0

    for right in range(len(s)):
        window[s[right]] = window.get(s[right], 0) + 1

        if s[right] in need and window[s[right]] == need[s[right]]:
            formed += 1

        while formed == required:
            # update result
            if (right - left + 1) < min_length:
                min_length = right - left + 1
                res = s[left:right+1]

            # shrink
            window[s[left]] -= 1

            if s[left] in need and window[s[left]] < need[s[left]]:
                formed -= 1

            left += 1

    return res
print(minimum_window_substring("ADOBECODEBANC","ABC"))