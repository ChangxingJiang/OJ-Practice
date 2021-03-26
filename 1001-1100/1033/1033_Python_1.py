from typing import List


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        t = sorted([a, b, c])
        d1 = t[2] - t[1] - 1
        d2 = t[1] - t[0] - 1
        maximum = d1 + d2
        if d1 == 0 and d2 == 0:
            minimum = 0
        elif d1 == 0 or d2 == 0 or d1 == 1 or d2 == 1:
            minimum = 1
        else:
            minimum = 2
        return [minimum, maximum]


if __name__ == "__main__":
    print(Solution().numMovesStones(a=1, b=2, c=5))  # [1, 2]
    print(Solution().numMovesStones(a=4, b=3, c=2))  # [0, 0]
    print(Solution().numMovesStones(a=3, b=5, c=1))  # [1, 2]
