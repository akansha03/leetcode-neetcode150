"""
Problem: [K Closest Points to Origin]
Link: https://leetcode.com/problems/k-closest-points-to-origin/
Difficulty: [Medium]
Topics: [List + Min Heap]

Pattern: [Min Heap + Distance]
Key Insight: [Distance is calculated and pushed into the min heap, and then extracted based on the value of k.]

Time Complexity: O(nlogn)
Space Complexity: O(n)

Solved: [22/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

from heapq import heappush, heappop
class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for x, y in points:
            distance = x*x + y*y
            heappush(heap, (distance, [x,y]))
        result = []
        while k>0:
            result.append(heappop(heap)[1])
            k -= 1
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.kClosest([[1,3],[-2,2]], 1) == [[-2,2]]
    assert sol.kClosest([[3,3],[5,-1],[-2,4]], 2) == [[3,3],[-2,4]]
    print("✅ All tests passed!")