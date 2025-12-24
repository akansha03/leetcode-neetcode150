"""
Problem: [Search 2D Matrix]
Link: https://leetcode.com/problems/search-a-2d-matrix/description/
Difficulty: [Medium]
Topics: [Array, List, Binary Search]

Pattern: [Binary Search]

Key Insight:

Solution 1

Run binary search on each row
TC: O(m) * O(log n)
SC: O(1)

Solution 2

* Play with the border indices and check if the target is greater then the last element in the row
* If yes, then increase the row index
* If not, then decrease the column index

TC: O(m+n)
SC: O(1)

Time Complexity: O(m log n)
Space Complexity: O(1)

Solved: [21/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""
from typing import List

class Solution:
    def searchMatrix_1(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def binarySearch(row):
            low, high = 0, n-1
            while low<=high:
                mid = (low + high)//2
                if matrix[row][mid] == target:
                    return True
                elif target>matrix[row][mid]:
                    low = mid+1
                else:
                    high = mid-1
            return False
        for row in range(m):
            if binarySearch(row):
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i<m and j>=0:
            if matrix[i][j] == target:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

if __name__ == "__main__":
    sol = Solution()
    assert sol.searchMatrix_1([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3) == True
    assert sol.searchMatrix_1([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
    assert sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3) == True
    assert sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13) == False
    print("✅ All tests passed!")