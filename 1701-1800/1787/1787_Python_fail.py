import collections
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        size = len(nums)

        # 处理k=1的特殊情况
        if k == 1:
            return sum(1 for num in nums if num != 0)

        # 统计每个循环节中每个位置的出现频率
        max_bit = 0  # 最大位数
        total = collections.Counter()  # 统计循环节中每个位置的总数
        count = [collections.Counter() for _ in range(k)]
        for i in range(size):
            count[i % k][nums[i]] += 1
            total[i % k] += 1
            max_bit = max(max_bit, nums[i].bit_length())

        # 动态规划计算最优解
        # 时间复杂度：2000*(2^10)
        maybe = 2 ** max_bit

        # 定义状态矩阵：dp[i][j] i=到循环节的第i个字符（省略） j=异或结果为j的情况下 dp[i][j] = 最少的改变数
        dp1 = [0 for _ in range(maybe)]
        for i in range(k):
            dp2 = [dp1[i] + 1 for i in range(maybe)]


if __name__ == "__main__":
    print(Solution().minChanges(nums=[1, 2, 0, 3, 0], k=1))  # 3
    print(Solution().minChanges(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3))  # 3
    print(Solution().minChanges(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3))  # 3
