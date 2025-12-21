"""
Problem: [Daily Temperatures]
Link: https://leetcode.com/problems/daily-temperatures/
Difficulty: [Medium]
Topics: [Array, Monotonic Stack]

Pattern: [Monotonic Stack]

Key Insight:

	•	Use a monotonic decreasing stack while iterating the temperatures from the end.
	•	Start by pushing the last day’s (temperature, index) into the stack.
	•	For each temperature (moving backwards):
            – While the current temperature is greater than or equal to the stack’s top, pop it.
            – This keeps the stack in strict increasing order of temperatures (from bottom → top).
	•	After popping, if the stack still has elements, the top gives the next warmer day.
	Use its index to update the result.
	•	Push the current (temperature, index) into the stack and continue.
	•	Finally, return the result array.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [07/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        result = [0]*n
        for i in range(n-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if stack:
                result[i] = stack[-1][1] - i
            stack.append((temperatures[i], i))
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert sol.dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert sol.dailyTemperatures([30,60,90]) == [1,1,0]
    assert sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]) == [8,1,5,4,3,2,1,1,0,0]
    print("✅ All tests passed!")