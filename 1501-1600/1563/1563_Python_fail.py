from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        size = len(stoneValue)

        # 计算前缀和
        prefix = [0]
        last = 0
        for stone in stoneValue:
            last += stone
            prefix.append(last)
        print(prefix)

        # 初始化状态矩阵
        dp = [[0] * size for _ in range(size)]

        # 从短到长的状态转移
        for length in range(1, size):  # 遍历行的长度
            for i in range(0, size - length):  # 遍历行的第一个下标位置
                j = i + length  # 计算行的最后一个下标位置

                # 二分查找最合理的分割位置
                # 最合理的分割位置一定在左侧行和右侧行最接近的位置
                l, r = i, i + length - 1
                while l < r:
                    m = (l + r) // 2
                    # left_val, right_val = prefix[m] - prefix[i], prefix[j + 1] - prefix[m]
                    left_val, right_val = prefix[m + 1] - prefix[i], prefix[j + 1] - prefix[m + 1]
                    if left_val <= right_val:
                        l = m + 1
                    else:
                        r = m

                print(i, j, "->", l - 1, l, "(", prefix[i:j + 2], ")")
                # 可能的解为l-1或l
                for k in range(max(i, l - 1), l + 1):
                    left_val, right_val = prefix[k + 1] - prefix[i], prefix[j + 1] - prefix[k + 1]
                    if left_val < right_val:
                        dp[i][j] = max(dp[i][j], left_val + dp[i][k])
                    elif left_val > right_val:
                        dp[i][j] = max(dp[i][j], right_val + dp[k + 1][j])
                    else:
                        dp[i][j] = max(dp[i][j], left_val + max(dp[i][k], dp[k + 1][j]))

        # 返回最终结果
        return dp[0][-1]


if __name__ == "__main__":
    # 18
    print(Solution().stoneGameV(stoneValue=[6, 2, 3, 4, 5, 5]))

    # 28
    print(Solution().stoneGameV(stoneValue=[7, 7, 7, 7, 7, 7, 7]))

    # 0
    print(Solution().stoneGameV(stoneValue=[4]))

    # 9033330
    print(Solution().stoneGameV(
        stoneValue=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 100, 100, 100, 100, 100, 100,
                    100, 100, 100, 100, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000, 10000, 10000, 10000,
                    10000, 10000, 10000, 10000, 10000, 10000, 10000, 100000, 100000, 100000, 100000, 100000, 100000,
                    100000, 100000, 100000, 100000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000, 1000000,
                    1000000, 1000000, 1000000]))

    # 330
    print(Solution().stoneGameV(stoneValue=[98, 77, 24, 49, 6, 12, 2, 44, 51, 96]))
