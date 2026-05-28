class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        for string in strs:
            output.append(str(len(string)))
            output.append("#")
            output.append(string)
        
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            word = ""
            count = ""

            while s[i] != "#":
                count += s[i]
                i += 1
            
            # skip the #
            i += 1

            length = int(count)

            output.append(s[i:i + length])

            i += length

        return output
