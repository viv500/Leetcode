class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        low = 0
        high = len(arr) - k

        while low < high:
            mid = (low + high) // 2

            if x - arr[mid] > arr[mid + k] - x:
                low = mid + 1
            else:
                high = mid

        return arr[low:low + k]

        # -------------------- EXPLANATION (LeetCode Interview Style) --------------------
        #
        # \U0001f9e9 Problem Understanding:
        # "Closest" means minimizing absolute difference from `x`, and in case of ties, 
        # the smaller elements are preferred.
        #
        # \U0001f50d Intuition:
        # - Since `arr` is sorted, the closest `k` elements will always form a *contiguous subarray*.
        # - The task reduces to finding the correct *starting index* of this subarray of size `k`.
        #
        # \U0001f4a1 Core Logic:
        # - Use **binary search** on the possible starting indices of the `k`-sized window.
        # - For each `mid` (potential window start):
        #   - Compare which side `x` is closer to:
        #       If `x - arr[mid] > arr[mid + k] - x`, move the window right (closer to larger values).
        #       Else, move the window left.
        # - Continue narrowing until `low` points to the leftmost start index of the closest subarray.
        #
        # ✅ Why This Works:
        # - The array’s sorted nature guarantees the monotonicity of closeness — 
        #   as you shift the window, differences move consistently in one direction.
        # - Hence, binary search efficiently finds the optimal window.
        #
        # ⏱️ Time Complexity:
        # - O(log(n - k)) → binary search over possible starting indices.
        # - O(k) → slicing the final subarray.
        # - Overall: **O(log(n - k) + k)**
        #
        # \U0001f4be Space Complexity:
        # - O(1) extra space (excluding output).
        #
        # ⚖️ Why This Approach:
        # - **Binary search** is faster than:
        #   - Two-pointer shrinking method (O(n - k))
        #   - Heap-based approach (O(n log k))
        # - Exploits the sorted order to minimize comparisons.
        #
        # \U0001f422 Brute Force (for contrast):
        # - Compute absolute difference for each element, sort by difference, take first `k`.
        #   → O(n log n)
        # - Inefficient because sorting all elements is unnecessary.
        #
        # \U0001f527 Trade-offs:
        # - Binary search solution is more complex to reason about than a two-pointer approach,
        #   but scales better for large arrays (n up to 10^5).
        # - Readability slightly reduced, but performance greatly improved.
        #
        # \U0001f9e0 Follow-up Discussion:
        # - **If array not sorted:** must sort first (O(n log n)), then apply same logic.
        # - **If multiple targets x1, x2, ...:** could preprocess prefix sums or binary indexed trees 
        #   for more efficient repeated range queries.
        # - **If dynamic stream input:** maintain a sliding window or use a balanced BST structure 
        #   for real-time updates.
        #
        # -------------------------------------------------------------------------------
