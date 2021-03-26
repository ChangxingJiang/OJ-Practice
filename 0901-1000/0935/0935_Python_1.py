class Solution:
    _JUMP = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }
    _MOD = 10 ** 9 + 7

    def knightDialer(self, n: int) -> int:
        dp1 = [1] * 10
        for _ in range(n - 1):
            dp2 = [0] * 10
            for i in range(10):
                for j in self._JUMP[i]:
                    dp2[j] += dp1[i]
                    dp2[j] %= self._MOD
            dp1 = dp2
        return sum(dp1) % self._MOD


if __name__ == "__main__":
    print(Solution().knightDialer(1))  # 10
    print(Solution().knightDialer(2))  # 20
    print(Solution().knightDialer(3))  # 46
