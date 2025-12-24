"""
Problem: [Binary Search]
Link: https://leetcode.com/problems/binary-search/description/
Difficulty: [Easy]
Topics: [Array, Binary Search]

Pattern: [Binary Search]
Key Insight:

* From the list of numbers, search for the target and check if that element exists.
* Use binary search and divide the search into half by calculating the mid. If value is equal to mid - then return the index.
* If value of target is greater than the mid-index element, then change low to mid+1.
* Else change high to mid-1.
* Keep on repeating, by calculating the mid, updating the low and high.

Time Complexity: O(log n)
Space Complexity: O(1)

Solved: [21/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        while low<=high:
            mid = (low + high)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
        
if __name__ == "__main__":
    sol = Solution()
    assert sol.search([-1,0,3,5,9,12], 9) == 4
    assert sol.search([-1,0,3,5,9,12], 2) == -1
    print("✅ All tests passed!")