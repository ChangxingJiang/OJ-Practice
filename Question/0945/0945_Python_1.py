import collections
from typing import List


class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = collections.Counter(A)

        ans = 0
        last, waiting = -1, 0
        for now in sorted(count):
            if waiting > 0:
                diff = now - last - 1
                while diff > 0 and waiting > 0:
                    waiting -= 1
                    diff -= 1
                    ans += waiting
            waiting += count[now] - 1
            last = now

            ans += waiting

        while waiting:
            waiting -= 1
            ans += waiting

        return ans


if __name__ == "__main__":
    print(Solution().minIncrementForUnique([1, 2, 2]))  # 1
    print(Solution().minIncrementForUnique([3, 2, 1, 2, 1, 7]))  # 6
    print(Solution().minIncrementForUnique([0, 2, 0]))  # 1
    print(Solution().minIncrementForUnique([4, 4, 7, 5, 1, 9, 4, 7, 3, 8]))  # 12
