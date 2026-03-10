"""
Problem: [Subsets]
Link: https://leetcode.com/problems/subsets/
Difficulty: [Medium]
Topics: [List, Recursion, Backtracking ]

Pattern: [Pick and not pick problem]
Key Insight:
This is a classic pick and not pick problem, where you can form subsets by picking a number at a certain index or not
picking it and moving ahead to another number.

Time Complexity: O(n * 2^n) [pick and notPick problem]
Space Complexity: O(n * 2^n) + O(n) [recursive space - depth]

Solved: [20/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(index, n, temp):
            if index == n:
                result.append(temp[:])
                return

            helper(index+1, n, temp)
            temp.append(nums[index])
            helper(index+1, n, temp)
            temp.pop()
        helper(0, len(nums), [])
        return result

    def subsets_reverse(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(index, temp):
            if index<0 :
                result.append(temp[:])
                return
            helper(index-1, temp)
            temp.append(nums[index])
            helper(index-1, temp)
            temp.pop()
        helper(len(nums)-1, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.subsets([1,2,3]) == [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
    assert sol.subsets_reverse([1, 2, 3]) == [[], [1], [2], [2, 1], [3], [3, 1], [3, 2], [3, 2, 1]]
    print("✅ All tests passed!")