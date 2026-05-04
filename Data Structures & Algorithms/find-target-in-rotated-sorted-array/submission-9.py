class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 1. run minimum in rotated sorted array algorithm
        # 2. each side of the partiion is sorted, figure out which side the target is
        # 3. run regular binary search on that side


        low = 0
        high = len(nums) - 1
        minimum_index = 0

        # 1. finding minmum index
        while low <= high:
            mid = (low + high) // 2

            if nums[low] <= nums[high]: minimum_index = low

            if nums[high] <= nums[mid]:
                low = mid +1
            
            else:
                high = mid
        

        # 2. deciding the half
        if nums[minimum_index] == target: return minimum_index #allows regular binary search on left half
        if minimum_index > 0:
            if nums[0] <= target <= nums[minimum_index - 1]:
                low = 0
                high = minimum_index - 1
            else:
                low = minimum_index
                high = len(nums) - 1
        else:
            low = 0
            high = len(nums) - 1

        print("minimum index: ", minimum_index)
        print("high: ", high)
        print("low: ", low)


        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target: return mid

            elif nums[mid] > target:
                high = mid - 1
            
            else:
                low = mid + 1
            


        return -1