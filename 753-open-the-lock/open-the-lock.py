from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        if target == "0000": return 0
        visited = set()

        # easier lookup
        deadends = set(deadends)
        moves = 0

        def children(lock):
            output = []
            for i in range(4):
                to_change = int(lock[i])
                # increment
                new_number_1 = (to_change + 1) % 10
                # decrement
                new_number_2 = (to_change + 9) % 10

                output.append(lock[0:i] + str(new_number_1) + lock[i + 1:4])
                output.append(lock[0:i] + str(new_number_2) + lock[i + 1:4])

            print(output)
            # only returning legal states
            return output

        q = deque(["0000"])

        while q:
            depth = len(q)

            for _ in range(depth):
                lock = q.popleft()

                for child in children(lock):
                    if child not in visited and child not in deadends:
                        if child == target: return moves + 1
                        
                        visited.add(child)
                        q.append(child)

            moves += 1

        return -1


         

