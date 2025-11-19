"""
Problem: [Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.]
Link: https://leetcode.com/problems/two-sum/description/
Difficulty: [Easy]
Topics: [Array, Hash Map, etc.]

Pattern: [Since it's not sorted, so we'll use an additional space to store the indices along with the difference]
Key Insight: [If sorted then go for two pointer]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [28/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return []
        two_sum_map = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in two_sum_map:
                return [two_sum_map[diff], i]
            two_sum_map[num] = i
        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.twoSum([2,7,11,15], 9) == [0,1]
    assert sol.twoSum([3,2,4],  6) == [1,2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
    print("✅ All tests passed!")