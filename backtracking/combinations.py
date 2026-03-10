"""
Problem: [Combinations]
Link: https://leetcode.com/problems/combinations/
Difficulty: [Medium]
Topics: [Recursion + Combination]

Pattern: [Combination problem of n choose k]
Key Insight: This is a match problem of n choose k, I have used a standard pattern of combination sum, used a loop
to iterate to the next element so that for 1 - [1,2][1,3][1,4] could be generated and so on.

Time Complexity: O(k*C(n,k)) [n choose k problem and to copy the elements to result which will be O(k)]
Space Complexity: O(k) [recursion depth] + O(k*C(n,k))

Solved: [26/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def helper(i, temp):
            if k == len(temp):
                result.append(temp[:])
                return

            for j in range(i, n+1):
                temp.append(j)
                helper(j+1, temp)
                temp.pop()
        helper(1, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.combine(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert sol.combine(1, 1) == [[1]]
    print("✅ All tests passed!")