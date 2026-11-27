# note: write character, remmebr coutns can be multidigit, needs to be separate characters
class Solution:
    def compress(self, chars: list[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            char = chars[read]
            count = 0
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # need to write the character, could be a different one
            chars[write] = char
            write += 1
            
            if count != 1:
                count_chars = str(count)
                for c in count_chars:
                    chars[write] = c
                    write += 1

        return write


                
