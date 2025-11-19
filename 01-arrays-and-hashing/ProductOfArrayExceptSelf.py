"""
Problem: [Products of Array Except Self]
Link: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
Difficulty: [Medium]
Topics: [Array, List]

Pattern: [Keep 2 arrays, left and right and store the left product and right product of each element in consecutive arrays]
Key Insight: [keep a single array and use it to multiply both left and right side of numbers]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [29/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]*n
        for i in range(1, n):
            result[i] = result[i-1] * nums[i-1]
        right = 1
        for j in range(n-1, -1, -1):
            result[j] *= right
            right *= nums[j]
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.productExceptSelf([1,2,4,6]) == [48,24,12,8]
    assert sol.productExceptSelf([-1,0,1,2,3]) == [0,-6,0,0,0]
    print("✅ All tests passed!")