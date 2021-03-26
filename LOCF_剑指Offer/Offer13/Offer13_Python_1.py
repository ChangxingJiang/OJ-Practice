class Solution:
    def simple_range(self, m, n, k):
        """一个单独的区域的计算（即一个10*10的范围中的计算）"""
        ans = 0
        m, n = min(m, 10), min(n, 10)
        for i in range(m):
            for j in range(n):
                if sum([int(ch) for ch in str(i)]) + sum([int(ch) for ch in str(j)]) <= k:
                    ans += 1
        return ans

    def movingCount(self, m: int, n: int, k: int) -> int:
        ans = self.simple_range(m, n, k)
        idx = 1
        while k >= 9:
            k -= 1
            for i in range(idx + 1):
                mm = m - i * 10
                nn = n - (idx - i) * 10
                if mm > 0 and nn > 0:
                    # print(mm, nn, k, "->", self.simple_range(mm, nn, k))
                    ans += self.simple_range(mm, nn, k)
            idx += 1
        return ans


if __name__ == "__main__":
    print(Solution().movingCount(m=2, n=3, k=1))  # 3
    print(Solution().movingCount(m=3, n=1, k=0))  # 1
    print(Solution().movingCount(m=16, n=8, k=4))  # 15
    print(Solution().movingCount(m=3, n=2, k=17))  # 6
    print(Solution().movingCount(m=38, n=15, k=9))  # 135
    print(Solution().movingCount(m=11, n=8, k=16))  # 88
    print(Solution().movingCount(m=57, n=12, k=15))  # 588
