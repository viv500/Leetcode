class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if nums[abs(n)] < 0: return abs(n)
            nums[abs(n)] *= -1
        # using set, O(n) time and O(n) space
        seen = set()
        for num in nums:
            if num in seen: 
                pass # return num
            seen.add(num)

        # O(1) space Approaces: 

        # Negative Marking (If modifying the input is okay)
        # the duplicate value appears twice in the list and indexes the same valid entry in the array (1 to n range, (n + 1) indices)
        # if the duplicae value is d and we mark nums[d] as negative, when we find d again, we'll see that nums[d] is negative

        
        
        
        # (if we can't modify the input)
        # Floys Tortoise and Hare cycle detection -> model the array as a linked list, then use Floyd's cycle detection.
        #
        # Linked list construction:
        #   - Each index i is a node with one outgoing edge to nums[i].
        #   - Since every value in nums is in [1, n], every value is a valid index, traversal never terminates.
        #
        # Why a cycle must exist:
        #   - There are n + 1 indices but only n distinct possible values - by pigeonhole, some node must be revisited
        #
        # Why the cycle entrance is the duplicate:
        #   - The duplicate value d appears at two indices i and j, so both nums[i] and nums[j] point to node d.
        #   - Node d is the only node with in-degree 2: one edge from inside cycle, other from "tail" leading in.
        #
        # Floyd's algorithm:
        #   Phase 1: Advance slow by 1 and fast by 2 until they meet at SOME node inside the cycle.
        #   Phase 2: Reset one pointer to the start. Move both one step at time; they meet exactly at cycle's entrance

        slow, fast = 0, 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]] # always valid

            if slow == fast: break

        slow2 = 0


        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2: return slow


