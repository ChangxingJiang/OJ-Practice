# 记忆化递归
# O(N^2×K)
# 超出时间限制

import functools


class Solution:
    @functools.lru_cache(None)
    def numberOfSets(self, n: int, k: int) -> int:
        # 处理不够分的情况
        if n - 1 < k:
            return 0

        # 处理刚好够分的情况
        if n - 1 == k:
            return 1

        # 处理只分成一个的情况
        if k == 1:
            return n * (n - 1) // 2

        # 处理更一般的情况
        ans = 0
        for i in range(1, n):
            ans += i * self.numberOfSets(n - i, k - 1)
        return ans % (10 ** 9 + 7)


if __name__ == "__main__":
    print(Solution().numberOfSets(4, 2))  # 5
    print(Solution().numberOfSets(3, 1))  # 3
    print(Solution().numberOfSets(30, 7))  # 796297179
    print(Solution().numberOfSets(5, 3))  # 7
    print(Solution().numberOfSets(3, 2))  # 1
    print(Solution().numberOfSets(633, 64))  # 1
    print(Solution().numberOfSets(751, 201))  # 1
