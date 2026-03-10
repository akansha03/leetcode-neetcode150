"""
Problem: [Permutation]
Link: https://leetcode.com/problems/permutations/
Difficulty: [Medium]
Topics: [List, Recursion, Backtracking]

Pattern: [Recursion + Backtracking + swapping]
Key Insight: [At each index, we fix one element by swapping it into position and recursively permute the remaining elements,
restoring the array state after each recursive call.

It is important to recurse using index i + 1, because i represents the position we are currently fixing. Using j in the
recursive call would break the structure and not generate all permutations correctly.

Fix → Recurse → Undo (swap back)]

Time Complexity: O(n!)
Space Complexity: O(n) [recursion stack space] + O(n!)

Solved: [28/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []

        def helper(i):
            if i == n:
                result.append(nums[:])
                return
            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                helper(i+1)
                nums[i], nums[j] = nums[j], nums[i]
        helper(0)
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.permute([1,2,3]) == [[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,2,1], [3,1,2]]
    print("✅ All tests passed!")