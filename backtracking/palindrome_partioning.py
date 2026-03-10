"""
Problem: [Palindrome Partitioning]
Link: https://leetcode.com/problems/palindrome-partitioning/description/
Difficulty: [Medium]
Topics: [Recursion, Backtracking, String]

Pattern: [Recursion + Backtracking]
Key Insight: [Following the same pattern as the combination problem, check for the palindrome or not then add the
range[i->j] in the temp]

Time Complexity: O(N*2^N)
Space Complexity: O(len(s)) [Recursion Stack] + O(N*2^N) [result storage]

Solved: [08/03/2026]
Revised: [], [], []
Confidence: ⭐⭐⭐
"""

class Solution(object):
    def partition(self, s):
        n = len(s)
        result = []

        def is_palindrome(i, j):
            while i<=j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        def helper(index, temp):
            if index == n:
                result.append(temp[:])
                return
            for j in range(index, n):
                if is_palindrome(index, j):
                    temp.append(s[index:j+1])
                    helper(j+1, temp)
                    temp.pop()
        helper(0, [])
        return result

if __name__ == "__main__":
    sol = Solution()
    assert sol.partition("aab") == [["a","a","b"],["aa","b"]]
    assert sol.partition("a") ==  [["a"]]
    print("✅ All tests passed!")