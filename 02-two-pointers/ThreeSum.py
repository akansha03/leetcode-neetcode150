"""
Problem: [Three Sum]
Link: https://leetcode.com/problems/3sum/description/
Difficulty: [Medium]
Topics: [Array, Sorting, Two Pointers]

Pattern: [Two Sum]
Key Insight:
 	•	First, sort the array — this makes spotting duplicates and moving pointers predictable.
	•	In the main loop, skip any duplicate element by checking if nums[i] == nums[i-1].
	•	Set up the two-pointer window (left and right).
	•	While left < right:
	•	If the sum hits the target, store the triplet, then move both pointers.
	•	After shifting, skip duplicates in the window by checking if the new left equals the previous left, or the new right equals the previous right.
	•	If sum < target → move left
	•	If sum > target → move right
Time Complexity: O(nlogn) + O(n^2)
Space Complexity: O(m) - worst case could be O(n/2)

Solved: [19/11/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐⭐
"""
from typing import List
class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i>0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            left, right = i+1, n-1
            while left<right:
                temp = nums[left] + nums[right]
                if temp == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif temp>target:
                    right -= 1
                else:
                    left += 1
        return result
if __name__ == "__main__":
    sol = Solution()
    assert sol.three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert sol.three_sum([0,1,1]) == []
    assert sol.three_sum([0,0,0,0]) == [[0,0,0]]
    print("✅ All tests passed!")