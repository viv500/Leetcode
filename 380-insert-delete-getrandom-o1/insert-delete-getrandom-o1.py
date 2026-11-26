class RandomizedSet:

    def __init__(self):
        self.numbers = []
        self.idx = {}

    def insert(self, val: int) -> bool:
        if val in self.idx: return False

        self.numbers.append(val)
        self.idx[val] = len(self.numbers) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx: return False

        i, last = self.idx[val], self.numbers[-1]
        self.numbers[i] = last
        self.idx[last] = i
        self.numbers.pop()

        del self.idx[val]
        return True
        
    def getRandom(self) -> int:
        return self.numbers[random.randint(0, len(self.numbers) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()