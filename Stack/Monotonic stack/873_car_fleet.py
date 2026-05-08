# LeetCode 853 - Car Fleet
# https://leetcode.com/problems/car-fleet/
#
# Description:
# Given the position and speed of cars moving toward a target,
# return the number of car fleets that will arrive at the destination.
#
# Technique: Sorting + Stack
# Time Complexity: O(n log n)
# Space Complexity: O(n)
def carfleet(positions,speeds, target):
    car = list(zip(positions,speeds))
    car.sort(reverse=True)
    stack=[]
    for pos, spd in car:
        time= float(target-pos)/spd
        if not stack or time> stack[-1]:
            stack.append(time)
    return len(stack)
        