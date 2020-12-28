from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        dp = [i for i in range(n)]

        for i in range(m):

            # print(i, ":", dp)

            for j in range(n):
                # 如果这个球已经卡住则跳过
                if dp[j] == -1:
                    continue

                # 处理右侧板的情况
                if grid[i][dp[j]] == 1:
                    if dp[j] == n - 1 or grid[i][dp[j] + 1] == -1:
                        dp[j] = -1
                    else:
                        dp[j] += 1

                # 处理左侧板的情况
                else:
                    if dp[j] == 0 or grid[i][dp[j] - 1] == 1:
                        dp[j] = -1
                    else:
                        dp[j] -= 1

        return dp


if __name__ == "__main__":
    # [1,-1,-1,-1,-1]
    print(Solution().findBall(
        grid=[[1, 1, 1, -1, -1],
              [1, 1, 1, -1, -1],
              [-1, -1, -1, 1, 1],
              [1, 1, 1, 1, -1],
              [-1, -1, -1, -1, -1]]
    ))

    # [-1]
    print(Solution().findBall(
        grid=[[-1]]
    ))
