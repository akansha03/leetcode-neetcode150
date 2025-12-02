"""
Problem: [Sliding Window Maximum]
Link: https://leetcode.com/problems/sliding-window-maximum/description/
Difficulty: [Hard]
Topics: [Array, Priority Queue]

Pattern: [Sliding Window]
Key Insight:
* Iterate the whole array, and add the elements in the heap, since it's min heap - add the negative sign before.
* Add a condition , to check for the window - if right pointer is less than k-1 then continue
* Once the window is equal to k-1 or more, calculate the left pointer condition using : right-k+1
* Check if the left pointer is greater than top element index
* If yes, that means it's already computed so pop that
* Add the top element in the queue

Time Complexity: O(n log n)
Space Complexity: O(n-k+1)

Solved: [01/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        pq = []
        for right, num in enumerate(nums):
            heappush(pq, (-num, right))
            if right<k-1:
                continue
            left = right-k+1
            while left > pq[0][1]:
                heappop(pq)
            result.append(-pq[0][0])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sol.maxSlidingWindow([1], 1) == [1]
    print("✅ All tests passed!")