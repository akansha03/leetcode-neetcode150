"""
Problem: [Search in Rotated Sorted Array]
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: [Medium]
Topics: [List]

Pattern: [Binary Search]
Key Insight:
*

Time Complexity: O(log n)
Space Complexity: O(1)

Solved: [23/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            if nums[low]<=nums[mid]:
                if nums[low]<=target<nums[mid]:
                    high = mid
                else:
                    low = mid+1
            else:
                if nums[mid]<target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid
        return -1
if __name__ == "__main__":
    sol = Solution()
    assert sol.search([4,5,6,7,0,1,2], 0) == 4
    assert sol.search([4,5,6,7,0,1,2], 3) == -1
    assert sol.search([1], 0) == -1

    assert sol.search([3,4,5,6,1,2], 1) == 4
    assert sol.search([3,5,6,0,1,2], 4) == -1

    assert sol.search([5,1,3], 5) == 0
    assert sol.search([5,1,3], 3) == 2
    print("✅ All tests passed!")