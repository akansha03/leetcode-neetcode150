"""
Problem: [Search in Rotated Sorted Array]
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
Difficulty: [Medium]
Topics: [List]

Pattern: [Binary Search]
Key Insight:
•	We solve search in a rotated sorted array using binary search.
•	Compute mid between low and high; if nums[mid] equals target, return mid.
•	There are two cases to handle — check which half is sorted.
•	If nums[low] <= nums[mid], the left half is sorted; check if target lies between low and mid, then move high to mid − 1, else move low to mid + 1.
•	Else, the right half is sorted; check if target lies between mid and high,
•	If yes, move low to mid + 1, else move high to mid − 1.
•	Always use <= where mid should be excluded, and initialize low = 0 and high = len(nums) − 1.

Time Complexity: O(log n)
Space Complexity: O(1)

Solved: [23/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
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