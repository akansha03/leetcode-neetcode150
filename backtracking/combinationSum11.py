"""
Problem: [Combination Sum 2]
Link: https://leetcode.com/problems/combination-sum-ii/description/
Difficulty: [Medium]
Topics: [Combination Sum 2 + Recursion + Backtracking]

Pattern: [Recursion + Backtracking]
Key Insight:
[Difference between combination Sum 1 and 2 is there can be duplicate array elements in combination sum 2
but result should have unique set of numbers. Important : Sort the array elements before starting the recursion so that the
same numbers are besides and could be avoided while creating a result - as with duplicates, multiple sets would be formed.]

🔹 Simple Memory Rule
If reuse is NOT allowed → complexity depends on n.: combination sum2
If reuse IS allowed → complexity depends on target.: combination sum1

Time Complexity: O(n log n)[sorting] + O(n * 2^n) [for every element all possible paths will be explored so n * 2^n]
Space Complexity: O(n) [Recursion stack space] + O(n * 2^n) [saved result if all the elements are used to form a set]

Solved: [26/02/2026]
Revised: [], [], []
Confidence: ⭐⭐
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        n = len(candidates)
        result = []
        candidates.sort()

        def helper(index, target, temp):

            # Condition to form a list
            if target == 0:
                result.append(temp[:])
                return

            # Backtracking condition to stop exploring the wrong paths
            if target<0 or index == n:
                return

            for j in range(index, n):
                if j != index and candidates[j-1] == candidates[j]:
                    continue
                temp.append(candidates[j])
                helper(j+1, target-candidates[j], temp)
                temp.pop()

        helper(0, target, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum2([10,1,2,7,6,1,5], 8) == [[1,1,6],[1,2,5],[1,7],[2,6]]
    assert sol.combinationSum2([2,5,2,1,2], 5) == [[1,2,2],[5]]
    print("✅ All tests passed!")