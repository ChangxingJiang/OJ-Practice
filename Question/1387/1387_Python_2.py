DP = {1: 0}


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def dfs(x):
            if x not in DP:
                if x % 2 == 1:
                    DP[x] = dfs(x * 3 + 1) + 1
                else:
                    DP[x] = dfs(x // 2) + 1
            return DP[x]

        lst = []
        for i in range(lo, hi + 1):
            v = dfs(i)
            lst.append((v, i))

        lst.sort()

        return lst[k - 1][1]


if __name__ == "__main__":
    print(Solution().getKth(lo=12, hi=15, k=2))  # 13
    print(Solution().getKth(lo=1, hi=1, k=1))  # 1
    print(Solution().getKth(lo=7, hi=11, k=4))  # 7
    print(Solution().getKth(lo=10, hi=20, k=5))  # 13
    print(Solution().getKth(lo=1, hi=1000, k=777))  # 570
