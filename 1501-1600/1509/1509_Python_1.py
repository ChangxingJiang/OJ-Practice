from typing import List


# O(N)
# 数组


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # 处理长度小于4的情况
        if len(nums) <= 4:
            return 0

        # 4个最小值和4个最大值
        min_val = list(sorted(nums[:4]))  # 从小到大
        max_val = min_val[::-1]  # 从大到小

        # 遍历数组寻找4个最小值和4个最大值
        for i in range(4, len(nums)):
            num = nums[i]
            if num < min_val[-1]:
                min_val.pop()
                min_val.append(num)
                min_val.sort()

            if num > max_val[-1]:
                max_val.pop()
                max_val.append(num)
                max_val.sort(reverse=True)

        # 处理4种可能的删除方法
        return min(max_val[i] - min_val[3 - i] for i in range(4))


if __name__ == "__main__":
    print(Solution().minDifference([5, 3, 2, 4]))  # 0
    print(Solution().minDifference([1, 5, 0, 10, 14]))  # 1
    print(Solution().minDifference([6, 6, 0, 1, 1, 4, 6]))  # 2
    print(Solution().minDifference([1, 5, 6, 14, 15]))  # 1
