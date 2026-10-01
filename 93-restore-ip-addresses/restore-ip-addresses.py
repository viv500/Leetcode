class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        if len(s) < 4 or len(s) > 12: return []

        def is_valid_ip(number): 
            stripped = str(int(number))
            return len(stripped) == len(number) and 0 <= int(number) <= 255

        partition = []
        result = []
        def backtrack(index):
            # success
            if len(partition) == 4 and index == len(s):
                result.append(".".join(partition))
                return
            
            # deadend
            if len(partition) == 4 or index == len(s): 
                return

            # to prevent an out of bounds error
            for i in range(index + 1, min(index + 4, len(s) + 1)):
                substring = s[index:i]
                if is_valid_ip(substring):
                    partition.append(substring)
                    backtrack(i)
                    partition.pop()


        backtrack(0)

        return result
