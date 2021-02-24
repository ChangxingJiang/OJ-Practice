import collections
from typing import List


class Solution:
    _BIG = 6001

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        visited0 = set(forbidden)
        visited1 = set(forbidden)
        queue = collections.deque([(0, 0)])
        step = 0
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                if i == x:
                    return step
                if i + a < self._BIG and i + a not in visited0:
                    queue.append((i + a, 0))
                    visited0.add(i + a)
                if j == 0 and i - b >= 0 and i - b not in visited1:
                    queue.append((i - b, 1))
                    visited1.add(i - b)
            step += 1
        return -1


if __name__ == "__main__":
    print(Solution().minimumJumps(forbidden=[14, 4, 18, 1, 15], a=3, b=15, x=9))  # 3
    print(Solution().minimumJumps(forbidden=[8, 3, 16, 6, 12, 20], a=15, b=13, x=11))  # -1
    print(Solution().minimumJumps(forbidden=[1, 6, 2, 14, 5, 17, 4], a=16, b=9, x=7))  # 2

    # 121
    print(Solution().minimumJumps(forbidden=
                                  [162, 118, 178, 152, 167, 100, 40, 74, 199, 186, 26, 73, 200, 127, 30, 124, 193, 84,
                                   184, 36, 103, 149, 153, 9, 54, 154, 133, 95, 45, 198, 79, 157, 64, 122, 59, 71, 48,
                                   177, 82, 35, 14, 176, 16, 108, 111, 6, 168, 31, 134, 164, 136, 72, 98],
                                  a=29, b=98, x=80))

