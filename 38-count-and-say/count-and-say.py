class Solution:
    def countAndSay(self, n: int) -> str:
        # recursive sol more elegant but less efficient
        # iteratively carry out the algo n times

        res = "1"

        # n - 1 cuz of the relation in the problem
        for _ in range(n - 1):
            new_res = ""
            i = 0

            while i < len(res):
                count = 1 

                # i + 1 limit so we can check one ahead
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1

                new_res += str(count) + res[i]
                count = 1
                i += 1

            res = new_res

        return res
