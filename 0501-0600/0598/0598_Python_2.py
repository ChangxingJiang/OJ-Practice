from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0:
            return m * n
        zipped = list(zip(*ops))
        return min(min(zipped[0]), m) * min(min(zipped[1]), n)


if __name__ == "__main__":
    print(Solution().maxCount(3, 3, [[2, 2], [3, 3]]))  # 4
