from typing import List


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)

        # 计算前缀和数列
        prefix = [0]
        now = 0
        for s in stones:
            now += s
            prefix.append(now)

        # print("前缀和:", prefix)

        dp = [[0] * n for _ in range(n)]

        for l in range(1, n):
            for i in range(n - l):
                j = i + l

                # 当剩下2个石头时
                if l == 1:
                    dp[i][j] = max(stones[i], stones[j])

                # 当剩下3个及以上的石头时
                else:
                    # print((i, j), stones[i:j + 1], "拿走:", stones[i], "->", (prefix[j + 1] - prefix[i + 1]),
                    #       dp[i + 1][j], "=", prefix[j + 1] - prefix[i + 1] - dp[i + 1][j])
                    # print((i, j), stones[i:j + 1], "拿走:", stones[j], "->", (prefix[j] - prefix[i]), dp[i][j - 1], "=",
                    #       (prefix[j] - prefix[i]) - dp[i][j - 1])
                    dp[i][j] = max((prefix[j + 1] - prefix[i + 1]) - dp[i + 1][j],  # 拿掉i
                                   (prefix[j] - prefix[i]) - dp[i][j - 1])  # 拿掉j

        # for row in dp:
        #     print(row)

        return dp[0][-1]


if __name__ == "__main__":
    print(Solution().stoneGameVII([5, 3, 1, 4, 2]))  # 6
    print(Solution().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]))  # 122
