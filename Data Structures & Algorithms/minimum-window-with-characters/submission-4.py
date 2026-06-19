from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        minimum_window = [0, len(s) + 1]
        need = Counter(t)
        count = defaultdict(int)
        have = 0
        print(need)
        left = right = 0

        while right < len(s):
            while right < len(s) and have != len(need):
                count[s[right]] += 1
                if count[s[right]] == need.get(s[right], 0): have += 1
                right += 1

            while left < len(s) and have == len(need):
                if right - left < minimum_window[1] - minimum_window[0]:
                    minimum_window = [left, right] 
                count[s[left]] -= 1
                if s[left] in need and count[s[left]] == need[s[left]] - 1: have -= 1
                left += 1


        return "" if minimum_window[1] == len(s) + 1 else s[minimum_window[0]:minimum_window[1]]
        