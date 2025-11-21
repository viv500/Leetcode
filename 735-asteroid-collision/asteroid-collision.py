class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack to track the topmost element involved in collision
        # loop through for as long as top of stack and next element create a collision ->
        # only possible if next element is negative and top of stack is positive -> <- , not <- ->
        # if first element is negative or last element is positive they will never be involved in a collision
        # each pop is O(1) and theres upto n pops -> O(n)
        stack = []

        for asteroid in asteroids:
            # runs as long as stack is non empty (i.e. incoming asteroid beat all stack asteroids)
            # or collision impossible (incoming asteroid is in the opposite direction of stack.peak())
            while stack and stack[-1] > 0 and asteroid < 0:
                difference = stack[-1] + asteroid
                if difference < 0:
                    # asteroid wins
                    stack.pop()
                elif difference > 0:
                    # stack wins
                    asteroid = 0
                else:
                    # its a tie
                    asteroid = 0
                    stack.pop()
            # asteroid suervived all collision, i.e. it beat all other asteroids
            if asteroid:
                stack.append(asteroid)

        return stack