"""
Problem: [Kth Largest Element in an Array]
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Difficulty: [Medium]
Topics: [Min Heap, List]

Pattern: [Min Heap]
Key Insight: [Add the elements to the min heap and pop as the length of the heap is more than k. Return the 0th
element as it will be the k-th largest]

Time Complexity: O(nlogk)
Space Complexity: O(k)

Solved: [25/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
from heapq import heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []
        for num in nums:
            heappush(heap, num)
            while len(heap) > k:
                heappop(heap)
        return heap[0]

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    print("✅ All tests passed!")