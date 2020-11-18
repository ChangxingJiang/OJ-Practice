from typing import List


class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        pass


if __name__ == "__main__":
    # [0.5,0]
    print(Solution().intersection([0, 0], [1, 0], [1, 1], [0, -1]))

    # [1,1]
    print(Solution().intersection([0, 0], [3, 3], [1, 1], [2, 2]))

    # []
    print(Solution().intersection([0, 0], [1, 1], [1, 0], [2, 1]))
