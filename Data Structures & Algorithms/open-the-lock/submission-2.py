from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if target in deadends or "0000" in deadends: return -1

        def generate_neighbors(code):
            result = set()
            for i in range(len(code)):
                val = int(code[i])
                nxt = (val + 1) % 10
                prev = (val - 1) % 10

                result.add(code[:i] + str(nxt) + code[i + 1:])
                result.add(code[:i] + str(prev) + code[i + 1:])

            return result

        steps = 0
        q = deque(["0000"])

        while q:
            level_size = len(q)

            for _ in range(level_size):
                code = q.popleft()
                if code == target: return steps

                neis = generate_neighbors(code)

                for nei in neis:
                    if nei not in deadends:
                        deadends.add(nei)
                        q.append(nei)

            steps += 1

        return -1