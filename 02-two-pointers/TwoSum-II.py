"""
Problem: [Two sum - Sorted Array]
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
Difficulty: [Medium]
Topics: [Array Sorted]

Pattern: [Two Pointer]
Key Insight: [Since array is already sorted, so we can take two pointers, sum them up and
check if the sum is greater than then the target, reduce the right else increase the left pointer,
once sum is equal to target, return both the pointers]

Time Complexity: O(n)
Space Complexity: O(2)

Solved: [19/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List

class Solution:
    def two_sum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers:
            return []
        left, right  = 0, len(numbers)-1
        while left<right:
            temp_sum = numbers[left] + numbers[right]
            if temp_sum == target:
                return [left+1, right+1]
            if temp_sum>target:
                right -= 1
            else:
                left += 1
        return []

if __name__ == "__main__":
    sol = Solution()
    assert sol.two_sum([2,7,11,15], 9) == [1,2]
    assert sol.two_sum([2,3,4], 6) == [1,3]
    assert sol.two_sum([-1,0], -1) == [1,2]
    print("✅ All tests passed!")