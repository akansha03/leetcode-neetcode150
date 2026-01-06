"""
Problem: [Find the Duplicate Number]
Link: https://leetcode.com/problems/find-the-duplicate-number/
Difficulty: [Medium]
Topics: [List, HashSet, slow and fast pointer]

Pattern: [Pink Floyd - slow and fast pointer]

Key Insight:
*  First solution is to use a set and then check if a number already exists or not.
* If yes, then return that number - as it's a duplicate
* If not then add the element in the set

* Second solution is not that intuitive, but it will solve the problem in O(1)
* We will use the concept of slow and fast pointer here i.e., same as linked list.
* First loop will be to figure out if the cycle exits or not - by cycle means an elements occurs more than once.
* Second loop will be to find that element which is repeated multiple times.

Time Complexity: O(n)
Space Complexity: O(n) if set is used, else O(1) using slow and fast pointer

Solved: [30/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                return num
            unique_nums.add(num)
        return -1

    def findDuplicatePinkFloyd(self, nums) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                break
        return slow

if __name__ == "__main__":
    sol = Solution()
    assert sol.findDuplicate([1,3,4,2,2]) == 2
    assert sol.findDuplicate([3,1,3,4,2]) == 3
    assert sol.findDuplicate([3,3,3,3,3]) == 3

    assert sol.findDuplicatePinkFloyd([1, 3, 4, 2, 2]) == 2
    assert sol.findDuplicatePinkFloyd([3, 1, 3, 4, 2]) == 3
    assert sol.findDuplicatePinkFloyd([3, 3, 3, 3, 3]) == 3
    print("✅ All tests passed!")