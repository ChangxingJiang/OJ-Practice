import itertools
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return [list(elem) for elem in itertools.combinations(range(1, n + 1), k)]


if __name__ == "__main__":
    # [
    #   [2,4],
    #   [3,4],
    #   [2,3],
    #   [1,2],
    #   [1,3],
    #   [1,4],
    # ]
    print(Solution().combine(4, 2))

    # [[1]]
    print(Solution().combine(1, 1))
