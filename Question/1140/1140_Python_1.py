import functools
from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        size = len(piles)

        # 计算后缀和
        suffix = [0]
        for ii in range(size - 1, -1, -1):
            suffix.append(suffix[-1] + piles[ii])
        suffix.reverse()
        suffix.pop()

        @functools.lru_cache(None)
        def dfs(i, x):
            # 处理已经没有石子的情况
            if i == size:
                return

            # 处理剩下的石子可以一次拿走的情况
            if size - i <= 2 * x:
                return suffix[i]

            ans = 0
            for j in range(1, 2 * x + 1):
                ans = max(ans, suffix[i] - dfs(i + j, max(j, x)))
            return ans

        return dfs(0, 1)


if __name__ == "__main__":
    print(Solution().stoneGameII(piles=[2, 7, 9, 4, 4]))  # 10
