"""
Problem: [Car Fleet]
Link: https://leetcode.com/problems/car-fleet/description/
Difficulty: [Medium]
Topics: [List, Stack]

Pattern: [Monotonic Stack]

Key Insight:

* The pattern I could figure out is to calculate the time by subtracting the points and diving by the speed.
* So, calculate time by (target-p)/s, then store it in an increasing monotonic stack.
* To achieve so, first sort the position array along with speed as pair, in a descending order.
* Extract each pair, calculate the time and append it to the stack.
* Then check the last two entries, if the top one is equal to or less than the 2nd last entry then
behind car will catch up and form the fleet - pop the entry from the stack.

Time Complexity: O(nlogn)
Space Complexity: O(n)

Solved: [13/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p,s) for p,s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        for p,s in pair:
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)

if __name__ == "__main__":
    sol = Solution()
    assert sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert sol.carFleet(10, [3], [3]) == 1
    assert sol.carFleet(100, [0,2,4], [4,2,1]) == 1
    assert sol.carFleet(10, [6,8], [3,2]) == 2
    print("✅ All tests passed!")