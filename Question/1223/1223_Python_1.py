from typing import List


class Solution:
    _MOD = 10 ** 9 + 7

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        # 初始化
        dp1 = [[0] * 16 for _ in range(6)]
        sum1 = [1] * 6
        dp1[0][0] = dp1[1][0] = dp1[2][0] = dp1[3][0] = dp1[4][0] = dp1[5][0] = 1

        for _ in range(1, n):
            dp2 = [[0] * 15 for _ in range(6)]
            sum2 = [0] * 6

            # 和上一个数不同的情况
            total = sum(sum1)
            for i in range(6):
                dp2[i][0] = (total - sum1[i]) % self._MOD
                sum2[i] = (sum2[i] + dp2[i][0]) % self._MOD

            # 和上一个相同
            for i in range(6):
                for j in range(1, min(16, rollMax[i])):
                    dp2[i][j] = dp1[i][j - 1]
                    sum2[i] = (sum2[i] + dp2[i][j]) % self._MOD

            dp1 = dp2
            sum1 = sum2

        return sum(sum1) % self._MOD


if __name__ == "__main__":
    print(Solution().dieSimulator(n=2, rollMax=[1, 1, 2, 2, 2, 3]))  # 34
    print(Solution().dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]))  # 30
    print(Solution().dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]))  # 181
