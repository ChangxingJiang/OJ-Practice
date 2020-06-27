from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.adds = [0]
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            self.adds.append(add)
        print(self.adds)

    def sumRange(self, i: int, j: int) -> int:
        return self.adds[j + 1] - self.adds[i]


if __name__ == "__main__":
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    print(num_array.sumRange(0, 2))  # 1
    print(num_array.sumRange(2, 5))  # -1
    print(num_array.sumRange(0, 5))  # -3
