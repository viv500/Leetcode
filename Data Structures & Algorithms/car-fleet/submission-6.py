class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(([p,s] for p,s in zip(position, speed)), reverse=True)
        stack = []

        for pos, spd in cars:
            finish = (target - pos) / spd

            if not stack or finish > stack[-1]: stack.append(finish)

        return len(stack)
        