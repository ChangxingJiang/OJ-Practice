class Solution:
    def racecar(self, target: int) -> int:
        dp = [float("inf")] * (target + 1)
        dp[0] = 0
        for t in range(1, target + 1):
            k1 = t.bit_length()

            # 处理不用重置直接到达的情况
            if t == 2 ** k1 - 1:
                dp[t] = k1
                continue

            # 考虑重置前最后一步走出后的最优解
            # 换句话说就是在之前的移动中考虑是否需要穿插一个反向的步子
            # 加的2为两次转身的步数
            for k2 in range(k1 - 1):
                dp[t] = min(dp[t], dp[t - 2 ** (k1 - 1) + 2 ** k2] + (k1 - 1) + k2 + 2)

            # 考虑从后面走回来的情况
            # (2**k1-1)为下一次移动到的位置
            # 加的1位一次转身的步数
            dp[t] = min(dp[t], dp[(2 ** k1 - 1) - t] + k1 + 1)

        # print(dp)

        return int(dp[-1])


if __name__ == "__main__":
    print(Solution().racecar(3))  # 2
    print(Solution().racecar(5))  # 7
    print(Solution().racecar(6))  # 5
    print(Solution().racecar(20))  # 12

    # [0, 1, 4, 2, 5, 7, 5, 3, 6, 8, 7, 10, 7, 9, 6, 4, 7, 9, 8, 11, 12, 10, 9, 12, 9, 11, 13, 11, 8]
