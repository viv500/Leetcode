class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
        
            while stack and a < 0 and stack[-1] > 0: # negative check, also < 0 prevents collision diff 0 from continuing
                b = stack.pop()
                diff = a + b

                if diff == 0: 
                    a = 0
                elif diff > 0: 
                    a = b

            if a != 0: stack.append(a)
        
        return stack
