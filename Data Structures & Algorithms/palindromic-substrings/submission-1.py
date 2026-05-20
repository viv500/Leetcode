class Solution:
    def countSubstrings(self, s: str) -> int:
        palindrome_count = 0

        def count(index1, index2):
            count = 0

            while index1 >= 0 and index2 < len(s) and s[index1] == s[index2]:
                count += 1
                index1 -= 1
                index2 += 1

            return count

        for i in range(len(s)):
            palindrome_count += count(i, i)

        for i in range(len(s) - 1):
            palindrome_count += count(i, i + 1)

        return palindrome_count



        