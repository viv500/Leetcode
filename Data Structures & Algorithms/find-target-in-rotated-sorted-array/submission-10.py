class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        # finding the minimum
        while low < high:
            # if this is true, we are in the sorted section and low is the minimum
            if nums[low] <= nums[high]: break

            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[low]:
                high = mid

        # low now stores the minimum
        def binarySearch(nums):
            low, high = 0, len(nums) - 1

            while low <= high:
                mid = (low + high) // 2

                if nums[mid] == target: return mid
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            
            return -1
                
        search1 = binarySearch(nums[:low])
        search2 = binarySearch(nums[low:])

        if search1 != -1:
            return search1
        elif search2 != -1:
            return search2 + len(nums[:low])
        else:
            return -1

            