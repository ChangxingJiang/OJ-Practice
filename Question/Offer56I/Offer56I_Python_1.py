from typing import List


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        # 找到只出现了一次的两个数的异或结果
        lst = 0
        for n in nums:
            lst ^= n

        # 找到两个数第一个不相同的位
        diff = 1
        while diff & lst == 0:
            diff <<= 1

        # 依据第一个不相同的位对该位的两种情况分别进行异或操作（此时每组只有一个出现一次的数）
        a, b = 0, 0
        for n in nums:
            if n & diff:
                a ^= n
            else:
                b ^= n

        return [a, b]


if __name__ == "__main__":
    # [1,6] 或 [6,1]
    print(Solution().singleNumbers([4, 1, 4, 6]))

    # [2,10] 或 [10,2]
    print(Solution().singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
