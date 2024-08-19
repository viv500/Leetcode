class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = {}
        for i in strs:
            # lists are unhashable (cant be used as dictionary keys) cuz they're mutable
            # sorted(i) converts it into a list of characters -> convert it back into a string
            sorted_string = ''.join(sorted(i))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = [i]
            else:
                hashmap[sorted_string].append(i)

        new_list = []
        for i in hashmap:
            new_list.append(hashmap[i])


        return new_list
