"""
LeetCode Problem: 346. Moving Average from Data Stream
Link: https://leetcode.com/problems/moving-average-from-data-stream/

Topic: Queue / Sliding Window
Difficulty: Easy

Given a stream of integers and a window size k,
return the moving average of the last k numbers.
"""

from collections import deque


def moving_average(nums, k):
    q = deque()
    window_sum = 0
    result = []

    for num in nums:
        q.append(num)
        window_sum += num

        if len(q) > k:
            window_sum -= q.popleft()

        if len(q) == k:
            result.append(window_sum / k)

    return result


if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    k = 2
    print(moving_average(nums, k))
