class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        longest_word = ""

        def can_form(string):
            if len(string) > len(s): return False
            a = b = 0
            while a < len(string) and b < len(s):
                if string[a] == s[b]:
                    a += 1
                    b += 1
                else:
                    b += 1
            
            return a == len(string)

        for word in dictionary:
            if can_form(word):
                if len(word) == len(longest_word):
                    longest_word = min(word, longest_word)
                elif len(word) > len(longest_word):
                    longest_word = word
    

        return longest_word