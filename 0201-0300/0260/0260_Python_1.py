from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 异或找到出现次数为奇数次的二进制位
        xor1 = 0
        for num in nums:
            xor1 ^= num

        # 找到第1个（从右往左）出现次数为奇数次的二进制位
        diff = xor1 & (-xor1)

        # 异或找到第1个出现次数为奇数次的二进制位为1的出现次数为奇数次的数（此时只会有1个）
        xor2 = 0
        for num in nums:
            if diff & num:
                xor2 ^= num

        return [xor1 ^ xor2, xor2]


if __name__ == "__main__":
    print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))  # [3,5]
