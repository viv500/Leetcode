class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0": return 0
        if len(s) == 1: return 1

        ways = [0] * len(s)
        ways[0] = 1

        if s[1] != "0":
            ways[1] += 1

        if 10 <= int(s[0:2]) <= 26:
            ways[1] += 1

        for i in range(2, len(s)):
            if s[i] != "0":
                ways[i] += ways[i - 1]

            if 10 <= int(s[i - 1: i + 1]) <= 26:
                ways[i] += ways[i - 2]

        print(ways)
        return ways[len(s) - 1]