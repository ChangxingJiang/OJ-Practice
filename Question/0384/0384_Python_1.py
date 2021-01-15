import random
from typing import List


class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = list(nums)

    def reset(self) -> List[int]:
        self.nums = self.original
        self.original = list(self.original)
        return self.nums

    def shuffle(self) -> List[int]:
        for i1 in range(len(self.nums)):
            i2 = random.randrange(i1, len(self.nums))
            self.nums[i1], self.nums[i2] = self.nums[i2], self.nums[i1]
        return self.nums


if __name__ == "__main__":
    obj = Solution([1, 2, 3])
    print(obj.shuffle())  # [3,1,2]
    print(obj.reset())  # [1,2,3]
    print(obj.shuffle())  # [1,3,2]
