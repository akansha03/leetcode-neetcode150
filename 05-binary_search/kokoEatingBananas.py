"""
Problem: [Koko Eating Bananas]
Link: https://leetcode.com/problems/koko-eating-bananas/
Difficulty: [Medium]
Topics: [List, Binary Search]

Pattern: [Binary Search]

Key Insight:

* This took me some time to figure out, but basic idea was that get the max from the piles and that can be a possible number
to devour the bananas per hour.
* We can take 1 as lower bound and max(piles) as upper bound.
* Either we go from lower to upper linearly or we can apply binary search.
* So we take the mid of left and right, and divide that with the pile of bananas, calculate the totalTime and if time is
less than number of hours. Store that as a result.
* Keep on performing the binary search until the smallest integer is found.

Time Complexity: O(len(piles) * log (len(piles))
Space Complexity: O(1)

Solved: [22/12/2025]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        speed = right

        while left<=right:
            mid = (left + right)//2
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(float(pile)/mid)
            if totalTime <= h:
                speed = mid
                right = mid-1
            else:
                left = mid+1
        return speed


if __name__ == "__main__":
    sol = Solution()
    assert sol.minEatingSpeed([3,6,7,11], 8) == 4
    assert sol.minEatingSpeed([30,11,23,4,20], 5) == 30
    assert sol.minEatingSpeed([30,11,23,4,20], 6) == 23
    print("✅ All tests passed!")