"""
Problem: [Intersection of Two Arrays]
Link: https://leetcode.com/problems/intersection-of-two-arrays/description/
Difficulty: [Easy]
Topics: [Arrays]

Pattern: [List, Set]
Key Insight: [Navigate through both of the arrays and add the common elements in the set, so that the
repetition is prevented. This will be O(n^2) solution in worst case complexity if there are no common elements.]
[Add all the elements of the nums1 in a map<Integer, Boolean> and mark it as True, traverse the second array and
check if there is a match with a map add it to result and mark that element to false - to eliminate repetition.]

Time Complexity:
For Set : O(n^2)
Space Complexity: O(min(len(nums1), len(nums2))) []

For Map : O(len(nums1) + len(nums2))
Space Complexity: O(min(len(nums1), len(nums2)))

Solved: [03/04/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from operator import truediv
from typing import List

class Solution(object):
    def intersection(self, nums1, nums2):
        result = set()

        for n in nums1:
            for n1 in nums2:
                if n == n1:
                    result.add(n)
        return list(result)

    def intersection_1(self, nums1, nums2):
        result = {}
        for n in nums1:
            result[n] = True
        answer = []
        for n1 in nums2:
            if n1 in result and result[n1]:
                answer.append(n1)
                result[n1] = False
        return answer


if __name__ == "__main__":
    sol = Solution()
    assert sol.intersection([1,2,2,1], [2,2]) == [2]
    assert sol.intersection([4,9,5], [9,4,9,8,4]) == [9,4]

    assert sol.intersection_1([1, 2, 2, 1], [2, 2]) == [2]
    assert sol.intersection_1([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
    print("✅ All tests passed!")