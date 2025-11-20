"""
Problem: [Container with most water]
Link: https://leetcode.com/problems/container-with-most-water/description/
Difficulty: [Medium]
Topics: [Array]

Pattern: [Two Pointer]

Key Insight:
* In this problem, we have to figure out the max area a container could hold water.
* For this again take two pointers, left and right.
* Get the maximum area by calculating the length and breadth
* For length, get the minimum of two heights i.e., of left and right
* For breadth, calculate the right-left

Time Complexity: O(n)
Space Complexity: O(1)

Solved: [20/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        n = len(nums)
        left, right, max_area = 0, n-1, 0
        while left<right:
            area = (right-left) * min(nums[left], nums[right])
            max_area = max(max_area, area)
            if nums[left]<nums[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert sol.maxArea([1,1]) == 1
    print("✅ All tests passed!")