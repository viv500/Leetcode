class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        nums.sort()

        for ai in range(len(nums) - 2):
            a = nums[ai]
            if a > 0: break
            if ai > 0 and a == nums[ai - 1]: continue

            bi, ci = ai + 1, len(nums) - 1

            while bi < ci:
                summ = a + nums[bi] + nums[ci]
                if summ == 0:
                    result.append([a, nums[bi], nums[ci]])

                    while bi < ci and nums[bi] == nums[bi + 1]:
                        bi += 1

                    while bi < ci and nums[ci] == nums[ci - 1]:
                        ci -= 1
                    
                    bi += 1
                    ci -= 1

                elif summ < 0: 
                    bi += 1
                else:
                    ci -= 1
            


        return result


