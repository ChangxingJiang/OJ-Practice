import itertools
from typing import List


class Solution:
    def __init__(self):
        self.ans = set()

    def getFactors(self, n: int) -> List[List[int]]:
        if n == 1:
            return []

        # 因子分解
        factor = []
        now = 2
        while now <= n:
            while n % now == 0:
                factor.append(now)
                n //= now
            now += 1

        if len(factor) == 1:
            return []

        self.dfs(tuple(sorted(factor)))

        return list(list(elem) for elem in self.ans)

    def dfs(self, factor):
        if len(factor) > 1:
            self.ans.add(factor)
            visited = set()
            for f1, f2 in itertools.combinations(factor, 2):
                f1, f2 = min(f1, f2), max(f1, f2)
                if (f1, f2) not in visited:
                    visited.add((f1, f2))
                    new_factor = list(factor)
                    new_factor.remove(f1)
                    new_factor.remove(f2)
                    new_factor.append(f1 * f2)
                    self.dfs(tuple(sorted(new_factor)))


if __name__ == "__main__":
    # []
    print(Solution().getFactors(1))

    # []
    print(Solution().getFactors(37))

    # [
    #   [2, 6],
    #   [2, 2, 3],
    #   [3, 4]
    # ]
    print(Solution().getFactors(12))

    # [
    #   [2, 16],
    #   [2, 2, 8],
    #   [2, 2, 2, 4],
    #   [2, 2, 2, 2, 2],
    #   [2, 4, 4],
    #   [4, 8]
    # ]
    print(Solution().getFactors(32))
