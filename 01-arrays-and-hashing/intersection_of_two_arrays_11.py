"""
Problem: [Intersection of Two Arrays II]
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
Difficulty: [Easy]
Topics: [List, Hash Table]

Pattern: [Frequency Calculation]
Key Insight: [Calculate the frequency of the first array and check in the second if frequency of elements is greater
than 0, if yes then append it as it's common and reduce it by 1]

Time Complexity: O(len(nums1) + len(nums2))
Space Complexity: O(min(len(nums1), len(nums2)))

Solved: [03/04/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
from collections import defaultdict

class Solution(object):
    def intersect(self, nums1, nums2):

        freq = defaultdict(int)
        for i in nums1:
            freq[i] += 1

        result = []
        for j in nums2:
            if freq[j]>0:
                result.append(j)
                freq[j] -= 1
        return result


if __name__ == "__main__":
    sol = Solution()
    assert sol.intersect([1,2,2,1], [2,2]) == [2,2]
    assert sol.intersect([4,9,5], [9,4,9,8,4]) == [9,4]
    assert sol.intersect([1, 2, 2, 1], [2]) == [2]
    print("✅ All tests passed!")