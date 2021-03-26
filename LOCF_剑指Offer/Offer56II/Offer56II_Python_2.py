from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0  # 每个数的状态的二进制的个位
        two = 0  # 每个数的状态的二进制的十位
        for n in nums:
            one = one ^ n & ~two
            two = two ^ n & ~one
        return one


if __name__ == "__main__":
    print(Solution().singleNumber([3, 4, 3, 3]))  # 4
    print(Solution().singleNumber([9, 1, 7, 9, 7, 9, 7]))  # 1
