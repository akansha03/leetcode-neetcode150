"""
Problem: [Trapping Rain Water]
Link: https://leetcode.com/problems/trapping-rain-water/description/
Difficulty: [Hard]
Topics: [Array, Two Pointer]

Pattern: [Two Pointer, Left and Right Max Array]

Key Insight:

* Suppose I am standing at a building i with a height x, I want to know what is the max height on the left of that index.
* And what is the max of the right index. To capture that, I will have two arrays - left and right.
* Now, I have to calculate the water trapped at index i, for that find the min height of left and right building.
* subtract the min height of left and right building with the building i.

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [20/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0]*n
        right_max = [0]*n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        count = 0
        for i in range(n):
            count += min(left_max[i], right_max[i]) - height[i]
        return count

if __name__ == "__main__":
    sol = Solution()
    assert sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert sol.trap([4,2,0,3,2,5]) == 9
    print("✅ All tests passed!")