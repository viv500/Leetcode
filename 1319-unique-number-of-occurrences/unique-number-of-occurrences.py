class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        has = {}
        for i in arr:
            if i in has:
                has[i] += 1
            else:
                has[i] = 1

        # cuz has.values() is a dict_values object not a list
        occurances = list(has.values())


        #checking if the array of the occruances and array of unique occurances has the same number of elements
        return len(occurances) == len(list(set(occurances)))
        