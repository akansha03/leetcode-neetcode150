"""
Problem: [Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.]
Link: https://leetcode.com/problems/top-k-frequent-elements/
Difficulty: [Medium]
Topics: [Array, Priority Queue]

Pattern: [Whenever there is k frequent involved then definitely it's a heap problem as we can store the elements based on a condition]
Key Insight: [Min heap could be used here as the smallest will be on top, and it will be removed when size of queue is more than k]

Time Complexity: O(n + k log k)
Space Complexity: O(n + k) - number of distinct elements

Solved: [28/10/2025]
Revised: [19/11/2025], [], []
Confidence: ⭐⭐⭐
"""
from typing import List
from collections import defaultdict
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] +=1
        pq = []
        for key, value in count.items():
            heappush(pq, [value, key])
            while len(pq) > k:
                heappop(pq)
        result = []
        for i in range(k):
            result.append(heappop(pq)[1])
        return result
if __name__ == "__main__":
    sol = Solution()
    assert sol.topKFrequent([1,1,1,2,2,3], 2) == [2,1]
    assert sol.topKFrequent([1], 1) == [1]
    assert sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2) == [1,2]
    print("✅ All tests passed!")