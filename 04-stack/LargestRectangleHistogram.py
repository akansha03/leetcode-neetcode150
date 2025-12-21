"""
Problem: [Largest Rectangle in Histogram]
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/
Difficulty: [Hard]
Topics: [Array, Monotonic Stack]

Pattern: [Increasing Monotonic Stack]
Key Insight:
* Idea is to take a monotonic stack and store the height in an increasing order.
* Whenever, a smaller height bar comes then pop the element from the stack and then calculate the area and
get the maxArea
* Repeat this and then iterate the elements of the stack, in case all the heights are in an increasing order.
* This area will be calculated from the length of the array

Time Complexity: O(n)
Space Complexity: O(n)

Solved: [14/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][0] > h:
                height, index = stack.pop()
                maxArea = max(maxArea, (i-index) * height)
                start = index
            stack.append((h, start))

        for h,i in stack:
            maxArea = max(maxArea, (len(heights) - i) * h)
        return maxArea

if __name__ == "__main__":
    sol = Solution()
    assert sol.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert sol.largestRectangleArea([2,4]) == 4
    print("✅ All tests passed!")