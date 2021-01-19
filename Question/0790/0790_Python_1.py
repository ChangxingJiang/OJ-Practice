class Solution:
    _MOD = 10 ** 9 + 7

    def numTilings(self, n: int) -> int:
        now = [1, 0, 0, 0]  # 两行均无空格，第1行空格，第2行空格，两行空格
        for _ in range(n):
            nxt = [0, 0, 0, 0]
            nxt[0] = (now[0] + now[1] + now[2] + now[3]) % self._MOD
            nxt[1] = (now[2] + now[3]) % self._MOD
            nxt[2] = (now[1] + now[3]) % self._MOD
            nxt[3] = (now[0]) % self._MOD
            now = nxt
        return now[0]


if __name__ == "__main__":
    print(Solution().numTilings(3))  # 5
    print(Solution().numTilings(4))  # 11
