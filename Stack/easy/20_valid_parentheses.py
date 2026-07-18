# LeetCode 20 - Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
#
# Description:
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
#
# Technique: Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
def check_parentheses(bracket):
    stack=[]
    pairs = {
        ')':'(',
        '}':'{',
        ']':'['    }
    for char in bracket:
        if char in '[{(':
            stack.append(char)
        else:
            if len(stack)==0:
                return False
            if stack.pop() != pairs[char]:
                return False
    return len(stack)==0
print(check_parentheses("[{()}]"))
