class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sorting helps us stop the algorithm early and helps with efficiency
        # it also allows us to avoid duplicate triplets by skipping duplicate starting indices
        output = []
        nums.sort() # O(log n)

        for i in range(len(nums) - 2):
            # important - checking (i + 1) could lead to skipping a potential dupe
            # ex. (i + 1) would've skipped [-1, -1, 0] the second -1 has a smaller search space, so skip that, not the first -1
            if i > 0 and nums[i] == nums[i - 1]: continue 
            if nums[i] > 0: break # sorted order, so future vales cant be -ve ( won't add up to 0)

            j = i + 1
            k = len(nums) - 1

            while j < k: # can't be equal
                summ = nums[i] + nums[j] + nums[k]

                if summ == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    # need to avoid duplicates here
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    # one more duplicate left
                    j += 1
                    k -= 1
                    # since i is fixed, we can't have another j or k repeat (it would be a dupe triplet)
                    
                elif summ > 0:
                    k -= 1
                else:
                    j += 1

        return output

        [-4, -1, -1, 0, 1, 2]



