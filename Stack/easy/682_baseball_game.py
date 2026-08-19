# LeetCode 682 - Baseball Game
# https://leetcode.com/problems/baseball-game/

def calPoints(ops):
    stack = []

    for op in ops:
        if op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        elif op == "+":
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))

    return sum(stack)


print(calPoints(["5","2","C","D","+"]))
