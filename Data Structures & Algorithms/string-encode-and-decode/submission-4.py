class Solution:
    # need to convert list of strings to string in such a way that it can be converted back into original string
    # need a delimiter for this but the problem is the string can contain any character

    # encode using the pattern count#wordcount#word
    # ex. "love","you" is 4#love3#you
    # now no matter what numbers are #'s are in the string, the 4# will skip over it and consider it in the word
    # we can assume that deocde() only recieves strings that were encoded by encode()


    # can't do number only and not hash cuz number at start of string could confuse how many characters to skip
    # ex. "hello", "1hi"
    # would be 5hello31hi which would skip 31 and not 3 -> 5#hello3#1hi would fix this
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += (str(len(word)) + "#" + word)

        return result

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        # note: count can be more than 1 character long

        while i < len(s):
            word = ""
            count = 0
            count = ""

            while s[i] != "#":
                count += s[i]
                i += 1          

            i += 1 # skip the #
            for _ in range(int(count)):
                word += s[i]
                i += 1

            print(word)
            output.append(word)
        
        return output


"5He3llo4Wo1r2ld"

"hello5#6#"

"9#hello5#6# "

"9#1"

"5#Hel5#5222023lo5Wworld"



