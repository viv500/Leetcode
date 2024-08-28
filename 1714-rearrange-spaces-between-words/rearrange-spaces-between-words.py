class Solution:
    def reorderSpaces(self, text: str) -> str:
        count = text.count(" ")
        if count == 0:
            return text
        wordlist = text.split()
        
        if len(wordlist) < 2:
            return "".join(wordlist) + (count * " ")

        even = int(count / (len(wordlist) - 1))
        remaining = count % (len(wordlist) - 1)

        return (even * " ").join(wordlist) + (remaining * " ")