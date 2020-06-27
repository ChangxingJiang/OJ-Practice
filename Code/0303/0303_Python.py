from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        pass

    def sumRange(self, i: int, j: int) -> int:
        pass


if __name__ == "__main__":
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    print(num_array.sumRange(0, 2))  # 1
    print(num_array.sumRange(2, 5))  # -1
    print(num_array.sumRange(0, 5))  # -3
