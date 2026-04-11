# LeetCode 739 - Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/
# Technique: Monotonic Stack

def dailyTemperatures(temps):
    stack = []
    res = [0] * len(temps)

    for i in range(len(temps)):
        while stack and temps[i] > temps[stack[-1]]:
            idx = stack.pop()
            res[idx] = i - idx

        stack.append(i)

    return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))