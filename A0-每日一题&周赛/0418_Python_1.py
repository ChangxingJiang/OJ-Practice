from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 计算总和
        sum_ = sum(nums)

        # 处理奇数的情况
        if sum_ % 2 == 1:
            return False

        # 计算目标值
        aim = sum_ / 2

        # 使用集合计算
        value_lst = set()
        for num in nums:
            if num == aim:
                return True
            for value in list(value_lst):
                if value + num == aim:
                    return True
                value_lst.add(value + num)
            value_lst.add(num)

        return False


if __name__ == "__main__":
    print(Solution().canPartition([1, 5, 11, 5]))  # True
    print(Solution().canPartition([1, 2, 3, 5]))  # False
