import functools
from typing import List


class Solution:
    _BIG = 10 ** 9 + +1

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        size = len(days)
        costs = [[1, costs[0]], [7, costs[1]], [30, costs[2]]]

        @functools.lru_cache(None)
        def dp(i):
            if i >= size:
                return 0
            ans = self._BIG
            j = i
            for day, cost in costs:
                while j < size and days[j] < days[i] + day:
                    j += 1
                ans = min(ans, dp(j) + cost)
            return ans

        return dp(0)


if __name__ == "__main__":
    # 11
    print(Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]))

    # 17
    print(Solution().mincostTickets(days=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], costs=[2, 7, 15]))
