# LeetCode 155 - Min Stack
# https://leetcode.com/problems/min-stack/
#
# Description:
# Design a stack that supports push, pop, top,
# and retrieving the minimum element in constant time.
#
# Technique: Stack
# Time Complexity: O(1) for all operations
# Space Complexity: O(n)

class Ministack:
    def __init__ (self):
        self.stack=[]
        self.ministack =[]

    def push(self,val):
        self.stack.append(val)
        if not self.ministack:
            self.ministack.append(val)
        else:
            self.ministack.append(min(val,self.ministack[-1]))
    def pop (self):
        self.stack.pop()
        self.ministack.pop()
    def top(self):
        return self.stack[-1]
    def getmin(self):
        return self.ministack[-1]

s = Ministack()

s.push(5)
print("After push 5")
print("Stack:", s.stack)
print("MinStack:", s.ministack)
print("Current Min:", s.getmin())
print()


s.push(3)
print("After push 3")
print("Stack:", s.stack)
print("MinStack:", s.ministack)
print("Current Min:", s.getmin())
print()

s.push(2)
print("After push 2")
print("Stack:", s.stack)
print("MinStack:", s.ministack)
print("Current Min:", s.getmin())
print()


s.pop()
print("After pop")
print("Stack:", s.stack)
print("MinStack:", s.ministack)
print("Current Min:", s.getmin())
print()


s.pop()
print("After pop")
print("Stack:", s.stack)
print("MinStack:", s.ministack)
print("Current Min:", s.getmin())
print()