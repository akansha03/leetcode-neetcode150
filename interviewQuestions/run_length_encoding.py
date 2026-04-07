from collections import defaultdict
# Time Complexity = O(n) and Space = O(1) # constant space

class Solution:
    def encode(self, s: str) -> str:
        left = right = 0
        n = len(s)
        result = []
        while right < n:
            count = 0
            while right < n and s[left] == s[right]:
                count += 1
                right += 1
            result.append(s[left] + str(count))
            left = right
        return ''.join(result)

    def decode(self, s: str) -> str:
        result = []
        i, n = 0, len(s)

        while i<n:
            if s[i].isalpha():
                c = s[i]
                i += 1
                count = ''
                while i<n and s[i].isnumeric():
                    count += s[i]
                    i += 1
                count = int(count) if count else 1
                result.append(c * count)
            else:
                i += 1
        return ''.join(result)

    def compress(self, s):
        i, n = 0, len(s)
        result_map = defaultdict(int)
        while i<n:
            c = s[i]
            if c.isalpha():
                count = ''
                while i+1<n and s[i+1].isnumeric():
                    count += s[i+1]
                    i += 1
                count = int(count) if count else 1
                result_map[c] += count
            else:
                i += 1
        result = []
        for key, value in result_map.items():
            result.append(key + str(value))
        return ''.join(result)

if __name__ == "__main__":
    sol = Solution()
    assert sol.encode("wwwwaaadexxxxxx") == "w4a3d1e1x6"
    assert sol.encode("aaaabbbccc") == "a4b3c3"
    assert sol.encode("abbbcdddd") == "a1b3c1d4"

    assert sol.decode("w4a3d1e1x6") == "wwwwaaadexxxxxx"
    assert sol.decode("a0b3c3") == "bbbccc"
    assert sol.decode("10abc") == "abc"

    assert sol.compress("a2b3c1b2c2") == "a2b5c3"
    print("✅ All tests passed!")
