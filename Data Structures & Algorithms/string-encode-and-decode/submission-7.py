class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)


        return "".join(result)

    def decode(self, s: str) -> List[str]:
        index = 0
        result = []

        while index < len(s):
            number = ""
            while index < len(s) and s[index].isdecimal():
                number += s[index]
                index += 1
            
            number = int(number)
            start, end = index + 1, index + 1 + number
            
            result.append(s[start:end])

            index = end

        return result


