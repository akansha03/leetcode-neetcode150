"""
Problem: [Median of Two Sorted Arrays]
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
Difficulty: [Easy/Medium/Hard]
Topics: [List, Binary Search]

Pattern: [Binary Search, Partition]

Key Insight:
* Original solution was to perform the merge sort and club both of them in one single array and then calculate the median
standard way for odd and even length arrays.
* Aforementioned solution would have been O(m+n).
* As per the expectation, algorithm should be O(log min(m, n)).
* Idea is to not merge the arrays and calculate the median. We have to form a partition and evaluate the boundary elements.
* To do so, we'll get the total length and perform binary search on array with the minimum length to get the min(m,n) complexity.
* Calculate the index partition of the left array and the index partitioning the right.
* Get the 4 boundary elements of both the arrays and check for boundaries if <0 then negative infinity else positive one.
* Make sure that the left elements of the first array are smaller than the right elements of the second array, and left
elements of the second array are smaller than the right elements of the first array.
* If the above conditions are met, then partition is correct and we can calculate the median -
    if length is odd then min of right element of the both the arrays
    if length is even then add the max of left elements and min of right elements - divide it by 2.
* If partition is not correct, i.e., aleft>bright , update the right to be mid-1 else left = mid+1

Time Complexity: O(log min(m,n))
Space Complexity: O(1)

Solved: [26/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        size = len(nums1) + len(nums2)
        half = size//2

        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1

        l, r = 0, len(nums1)-1
        while True:
            mid = (l+r)//2
            mid1 = half - mid - 2

            aleft = nums1[mid] if mid>=0 else float('-inf')
            aright = nums1[mid+1] if mid+1 <len(nums1) else float('inf')
            bleft = nums2[mid1] if mid1>=0 else float('-inf')
            bright = nums2[mid1+1] if mid1+1<len(nums2) else float('inf')

            # Check the boundary
            if aleft<=bright and bleft<=aright:
                if size%2:
                    return min(aright, bright)
                return float(max(aleft, bleft) + min(aright, bright))/2
            elif aleft>bright:
                r = mid-1
            else:
                l = mid+1

if __name__ == "__main__":
    sol = Solution()
    assert sol.findMedianSortedArrays([1,3], [2]) == 2.00000
    assert sol.findMedianSortedArrays([1,2], [3,4]) == 2.50000
    print("✅ All tests passed!")