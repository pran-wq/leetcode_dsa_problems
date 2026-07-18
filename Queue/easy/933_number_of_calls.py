# LeetCode 933 - Number of Recent Calls
# https://leetcode.com/problems/number-of-recent-calls/
#
# Description:
# You have a RecentCounter class which counts the number of recent requests
# within the last 3000 milliseconds.
#
# Technique: Queue (Deque) + Sliding Window
# Time Complexity: O(1) amortized per call
# Space Complexity: O(n)

from collections import deque

class RecentCounter:

    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        # Remove timestamps older than t - 3000
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
rc = RecentCounter()

print(rc.ping(1))     # Expected: 1
print(rc.ping(100))   # Expected: 2
print(rc.ping(3001))  # Expected: 3
print(rc.ping(3002))  # Expected: 3
