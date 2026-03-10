"""
Problem: [Combination Sum]
Link: https://leetcode.com/problems/combination-sum/
Difficulty: [Medium]
Topics: [Recursion, Backtracking, List]

Pattern: [Combination + Recursion + Backtracking]

Key Insight:
	•	The input array elements are unique.
	•	The result combinations can contain repeating elements.
	•	Since repetition is allowed, during recursion:
	•	We use a loop
	•	And we pass the same index again (not i + 1)
	•	This allows the same element to be chosen multiple times.
Both combination problems typically use:
	•	A for loop inside recursion
	•	Controlled index movement to avoid duplicate combinations

🔹 Simple Memory Rule
If reuse is NOT allowed → complexity depends on n : combination sum2
If reuse IS allowed → complexity depends on target : combination sum1
	
	

Time Complexity: O(2^(t/m)) ~ where t is the target number and m is the minimum element
Space Complexity: O(t/m) - target/minimum element

Solved: [26/02/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size = len(candidates)
        result = []

        def helper(index, target, temp):
            if target == 0:
                result.append(temp[:])
                return
            for k in range(index, size):
                if target>0:
                    temp.append(candidates[k])
                    helper(k, target-candidates[k], temp)
                    temp.pop()
        helper(0, target, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.combinationSum([2,3,6,7], 7) == [[2,2,3],[7]]
    assert sol.combinationSum([2,3,5], 8) == [[2,2,2,2],[2,3,3],[3,5]]
    print("✅ All tests passed!")