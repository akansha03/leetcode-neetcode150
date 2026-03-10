"""
Problem: [Subsets II]
Link: https://leetcode.com/problems/subsets-ii/description/
Difficulty: [Medium]
Topics: [List, Recursion, Sorting]

Pattern: [Pick or Not Pick, Sorting]
Key Insight: [As part of this problem, apply the sorting so that the same elements are next to each other.
 now p]

Time Complexity: O(n*2^n) + O(nlogn)
Space Complexity: O(n)[recursion space] + O(n*2^n) [result space]

Solved: [07/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
class Solution(object):
    def subsetsWithDup(self, nums: List[int]):
        result = []
        nums.sort()
        n = len(nums)

        def helper(index, temp):
            result.append(temp[:])
            for j in range(index, n):
                if j != index and nums[j-1] == nums[j]:
                    continue
                temp.append(nums[j])
                helper(j+1, temp)
                temp.pop()
        helper(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.subsetsWithDup([1,2,2]) == [[],[1],[1,2],[1,2,2],[2],[2,2]]
    assert sol.subsetsWithDup([0]) == [[],[0]]
    print("✅ All tests passed!")