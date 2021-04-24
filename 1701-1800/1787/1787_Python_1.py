import collections
from typing import List


class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        size = len(nums)

        # ----- 处理k=1的特殊情况 -----
        if k == 1:
            return sum(1 for num in nums if num != 0)

        # ----- 统计每个循环节中每个位置的出现频率 -----
        # O(N)
        max_bit = 0  # 最大位数
        total = collections.Counter()  # 统计循环节中每个位置的总数
        count = [collections.Counter() for _ in range(k)]
        for i in range(size):
            count[i % k][nums[i]] += 1
            total[i % k] += 1
            max_bit = max(max_bit, nums[i].bit_length())

        # ----- 计算循环节中只有1个数不使用最高频的最优解 -----
        # O(K×(N/K)+K)=O(N+K)
        xor = 0  # 最高频结果异或结果
        most_common_num = 0  # 最高频结果总频率
        common_count = []
        for i in range(k):
            common_count.append(count[i].most_common(1)[0])
            xor ^= common_count[-1][0]
            most_common_num += common_count[-1][1]

        least_ans = size - most_common_num  # 至少需要修改的数量
        # print("至少需要修改的数量:", least_ans)

        # 处理异或结果为0的情况情况
        if xor == 0:
            return least_ans

        # 遍历每一个数，尝试只修改它
        min_diff = size
        for i in range(k):
            num = xor ^ common_count[i][0]  # 当前数需要改为的数
            diff = count[i][common_count[i][0]] - count[i][num]  # 需要增加的修改数
            min_diff = min(min_diff, diff)
        # print("损失量:", min_diff)

        # ----- 计算循环节中有多个数不使用最高频的最优解 -----
        # 动态规划思路：但凡超过修改1个数的最优解则忽略当前结果
        # 理论时间复杂度:O((N-K)*K*(2**10))

        # 定义状态矩阵：dp[i][j] i=到循环节的第i个字符（省略） j=异或结果为j的情况下 dp[i][j] = 最少的改变数
        dp1 = {0: 0}
        for i in range(k):
            dp2 = {}
            most_common = common_count[i][1]
            for k2, v2 in count[i].items():
                diff2 = most_common - v2
                if diff2 < min_diff:
                    for k1, diff1 in dp1.items():
                        if diff1 + diff2 < min_diff:
                            if (k1 ^ k2) not in dp2 or dp2[k1 ^ k2] > (diff1 + diff2):
                                dp2[k1 ^ k2] = diff1 + diff2
            dp1 = dp2

        if 0 in dp1:
            return least_ans + dp1[0]
        else:
            return least_ans + min_diff


if __name__ == "__main__":
    print(Solution().minChanges(nums=[1, 2, 0, 3, 0], k=1))  # 3
    print(Solution().minChanges(nums=[3, 4, 5, 2, 1, 7, 3, 4, 7], k=3))  # 3
    print(Solution().minChanges(nums=[1, 2, 4, 1, 2, 5, 1, 2, 6], k=3))  # 3

    # 测试用例39/81
    print(Solution().minChanges(nums=[26, 19, 19, 28, 13, 14, 6, 25, 28, 19, 0, 15, 25, 11], k=3))  # 11

    # 自制用例
    print(Solution().minChanges(nums=[3, 3, 3, 7, 4, 6, 3, 4, 6], k=3))  # 5
