"""
Problem: [Find Minimum in Rotated Sorted Array]
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
Difficulty: [Medium]
Topics: [List, Binary Search]

Pattern: [Binary Search]

Key Insight:

* This array was once sorted and then rotated so idea is to find the first drop point - where ith element is larger than
the i+1 element.
* Return that element.
* This can be done linearly as well, but we'll use binary search for logarithmic complexity.
* For this, first calculate the mid and then check if that nums[low] < nums[mid].
* If yes, then there can be two options that the minimum element exists either on the left of the mid or right of the mid.
    * Check for 2 conditions, check that the mid is greater than high - then it's on right : low = mid+1
    * else high = mid
* If low is greater than mid for sure, lowest element is on the left then high = mid

Time Complexity: O(log n)
Space Complexity: O(1)

Solved: [22/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def linearMin(self, nums):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]

    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low<high:
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                if nums[mid]>nums[high]:
                    low = mid+1
                else:
                    high = mid
            else:
                high = mid
        return nums[low]

if __name__ == "__main__":
    sol = Solution()
    assert sol.linearMin([3, 4, 5, 1, 2]) == 1
    assert sol.linearMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert sol.linearMin([11, 13, 15, 17]) == 11
    assert sol.linearMin([5, 1, 2, 3, 4]) == 1

    assert sol.findMin([3,4,5,1,2]) == 1
    assert sol.findMin([4,5,6,7,0,1,2]) == 0
    assert sol.findMin([11,13,15,17]) == 11
    assert sol.findMin([5,1,2,3,4]) == 1
    print("✅ All tests passed!")