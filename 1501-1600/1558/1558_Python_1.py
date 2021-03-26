from typing import List


# 数学
# O(NlogV) : 其中V为每个数的最大值


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op_2_min = 0  # 第2种操作的最小次数
        op_1 = 0  # 第1种操作的次数总数
        for num in nums:
            op_2 = 0
            while num:
                if num % 2 == 1:
                    num -= 1
                    op_1 += 1
                else:
                    num //= 2
                    op_2 += 1
            op_2_min = max(op_2_min, op_2)

        return op_1 + op_2_min


if __name__ == "__main__":
    print(Solution().minOperations([1, 5]))  # 5
    print(Solution().minOperations([2, 2]))  # 3
    print(Solution().minOperations([4, 2, 5]))  # 6
    print(Solution().minOperations([3, 2, 2, 4]))  # 7
    print(Solution().minOperations([2, 4, 8, 16]))  # 8
