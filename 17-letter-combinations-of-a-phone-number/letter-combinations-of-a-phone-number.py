class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)

        #edge case
        if length == 0:
            return []

        #hashmap for conversions 
        convert = {"2":"abc",
                "3":"def",
                "4":"ghi",
                "5":"jkl",
                "6":"mno",
                "7":"pqrs",
                "8":"tuv",
                "9":"wxyz"}

        # this contains every permutation
        possible = []

        def backtrack(index, current_combination):

            #checks if we have enough characters in string to append to collection
            if length == len(current_combination):
                possible.append(current_combination)

                #end the recursive call
                return
            
            # all possible characters for a given digit
            possible_chars = convert[digits[index]]
            for character in possible_chars:

                # recursive call for every starting character possible
                backtrack(index + 1, current_combination + character)

        backtrack(0, "")

        return possible
        