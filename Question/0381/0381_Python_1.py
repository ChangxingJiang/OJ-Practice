import collections
import random


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.dict = collections.defaultdict(set)

    def insert(self, val: int) -> bool:
        self.dict[val].add(len(self.nums))
        self.nums.append(val)

        # print(self.nums, self.dict)

        return len(self.dict[val]) == 1

    def remove(self, val: int) -> bool:
        if self.dict[val]:
            idx = self.dict[val].pop()
            if len(self.nums) > 1 and idx != len(self.nums) - 1:
                self.dict[self.nums[-1]].remove(len(self.nums) - 1)
                self.dict[self.nums[-1]].add(idx)
                self.nums[idx] = self.nums[-1]
            self.nums.pop()

            # print(self.nums, self.dict)

            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)


if __name__ == "__main__":
    obj = RandomizedCollection()
    obj.insert(0)
    obj.insert(1)
    obj.remove(0)
    obj.insert(2)
    obj.remove(1)
    print(obj.getRandom())

    obj = RandomizedCollection()
    obj.insert(1)
    obj.remove(1)
    obj.insert(1)

    obj = RandomizedCollection()
    obj.insert(4)
    obj.insert(3)
    obj.insert(4)
    obj.insert(2)
    obj.remove(4)
    obj.remove(3)
    obj.remove(4)
    obj.remove(4)
