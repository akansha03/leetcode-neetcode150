"""
Problem: [Longest Consecutive Sequence]
Link: https://neetcode.io/problems/longest-consecutive-sequence?list=neetcode150
Difficulty: [Medium]
Topics: [Array, HashSet]

Pattern: [Store all elements in a set and check that the next element exists or not, if yes keep on counting]
Key Insight: [Count will give the max length]

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [31/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""
from typing import List, Set
class Solution:
    def longestConsecutiveSequence(self, nums: List[int]) -> int:
        sequence_set = set(nums)
        maxLen = 0
        for num in sequence_set:
            temp_num = num + 1
            count = 1
            while temp_num in sequence_set:
                temp_num += 1
                count += 1
            maxLen = max(maxLen, count)
        return maxLen

if __name__ == "__main__":
    sol = Solution()
    assert sol.longestConsecutiveSequence([2,20,4,10,3,4,5]) == 4
    assert sol.longestConsecutiveSequence([0,3,2,5,4,6,1,1]) == 7
    print("✅ All tests passed!")