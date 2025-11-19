"""
Problem: Given an integer array nums and an integer k, return the kth largest element in the array.
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Difficulty: [Medium]
Topics: [Array, Priority Queue]

Pattern: [Use Priority Queue to get the kth largest element]
Key Insight: [Push the elements in the min heap where minimum element will be at the top and once the size is more than k
- pop it out, so that the top element of the min heap is the kth largest]

Time Complexity: O(n log k)
Space Complexity: O(k)

Solved: [29/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐⭐⭐
"""

from heapq import heappush, heappop

class Solution:
    def findKthLargest(self, nums, k):
        pq = []
        for num in nums:
            heappush(pq, num)
            while len(pq) > k:
                heappop(pq)
        return heappop(pq)

if __name__ == "__main__":
    sol = Solution()
    assert sol.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert sol.findKthLargest([3,2,3,1,2,4,5,5,6], 1) == 6
    print("✅ All tests passed!")