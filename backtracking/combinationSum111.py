"""
Problem: [Combination Sum III]
Link: https://leetcode.com/problems/combination-sum-iii/description/
Difficulty: [Medium]
Topics: [Recursion + Backtracking + Combination]

Pattern: [List, Backtracking, Pruning]
Key Insight: [In this problem 9 choose k will be used along with target. Same pattern as Combination Sum.]

Time Complexity: O(k * C(9, k))
Space Complexity: O(k) [recursion space] + O(k * C(9,k))

Solved: [26/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def helper(i, target, temp):
            if target == 0 and k == len(temp):
                result.append(temp[:])
                return
            for j in range(i, 10):
                temp.append(j)
                helper(j+1, target-j, temp)
                temp.pop()
        helper(1, n, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum3(3, 7) == [[1,2,4]]
    assert sol.combinationSum3(3, 9) == [[1,2,6],[1,3,5],[2,3,4]]
    assert sol.combinationSum3(4, 1) == []
    print("✅ All tests passed!")