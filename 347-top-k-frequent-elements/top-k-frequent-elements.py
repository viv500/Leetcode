class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        total = []

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        
        hashmap = sorted([[value, key] for key, value in hashmap.items()], reverse=True)

        for i in range(k):
            total.append(hashmap[i][1])

        return total
        
