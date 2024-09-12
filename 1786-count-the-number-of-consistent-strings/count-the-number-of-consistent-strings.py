class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        consistent = 0
        
        for word in words:
            is_consistent = True  # Assume the word is consistent
            for char in word:
                if char not in allowed_set:  # If a char is not in allowed, mark as inconsistent
                    is_consistent = False
                    break  # No need to check further if one char is not allowed
            if is_consistent:
                consistent += 1
        
        return consistent
