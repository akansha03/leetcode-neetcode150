"""
Problem: [Last Stone Weight]
Link: https://leetcode.com/problems/last-stone-weight/
Difficulty: [Easy]
Topics: [Min Heap + List]

Pattern: [Min Heap]
Key Insight: [Using the max heap functionality to extract the top 2 max elements so multiply by -1; due to the default
min heap behaviour. Then heapify the heap so that top elements are the max ones. Now extract 2 values until the length
is 1 and then calculate the y-x and push it to heap.]

Time Complexity: O(nlogn)
Space Complexity: O(n)

Solved: [22/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from typing import List
from heapq import heappush, heappop, heapify

class Solution(object):
    def lastStoneWeight(self, stones):

        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapify(stones)
        while len(stones) > 1:
            y = -heappop(stones)
            x = -heappop(stones)
            if x!=y:
                heappush(stones, -(y-x))
        return -stones[0] if stones else 0

if __name__ == "__main__":
    sol = Solution()
    assert sol.lastStoneWeight([2,7,4,1,8,1]) == 1
    assert sol.lastStoneWeight([1]) == 1
    print("✅ All tests passed!")