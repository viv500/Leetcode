class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0: return False
        part = total // 3

        partitions = 0
        cur_sum = 0
        index = 0

        while index < len(arr):
            cur_sum += arr[index]
            if cur_sum == part:
                cur_sum = 0
                partitions += 1
            
            index += 1


        return partitions >= 3

