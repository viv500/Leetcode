class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # doesnt work cuz this creates a new list and rebinds the local variable s to it — the original list passed in is untouched.
        # s = s[::-1]

        left, right = 0, len(s) - 1

        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        