from typing import List


# 数组
# O(N^2logN^2)


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        # 计算所有结果
        # O(N^2)
        lst = []
        for length in range(1, len(nums) + 1):
            first = sum(nums[:length])
            lst.append(first)
            for i in range(len(nums) - length):
                first = first - nums[i] + nums[i + length]
                lst.append(first)

        # 排序结果
        # O(N^2logN^2)
        lst.sort()

        return sum(lst[left - 1:right]) % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().rangeSum(nums=[1, 2, 3, 4], n=4, left=1, right=5))  # 13
