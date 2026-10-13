import random
class RandomizedSet:

    def __init__(self):
        self.set_arr = []
        self.val_to_index = dict()

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.set_arr.append(val)
        self.val_to_index[val] = len(self.set_arr) - 1
        

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]

        self.set_arr[index], self.set_arr[-1] = self.set_arr[-1], self.set_arr[index]
        self.val_to_index[self.set_arr[index]] = index
        self.set_arr.pop()

        del self.val_to_index[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.set_arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()