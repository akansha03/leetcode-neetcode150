"""
Problem: [Kth Largest Element in a Stream]
Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/
Difficulty: [Easy]
Topics: [Data Stream, Min Heap]

Pattern: []
Key Insight: [Use a Min Heap and pop the elements when length of the heap is more than k. This will make sure that the
kth largest element is always at the 0th location.]

Time Complexity: O(n logk)
Space Complexity: O(k)

Solved: [22/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from heapq import heappush, heappop
class KthLargest:
    def __init__(self, k: int, nums):
        self.k = k
        self.heap = []
        for num in nums:
            heappush(self.heap, num)
            while len(self.heap) > k:
                heappop(self.heap)
                
    def add(self, val: int) -> int:
        heappush(self.heap, val)
        while len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]

if __name__ == "__main__":
    sol = KthLargest(3, [4, 5, 8, 2])
    assert sol.add(3) == 4
    assert sol.add(5) == 5
    assert sol.add(10) == 5
    assert sol.add(9) == 8
    assert sol.add(4) == 8
    print("✅ All tests passed!")