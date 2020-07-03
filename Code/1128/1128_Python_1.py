import collections
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = collections.Counter((d[0], d[1]) if d[0] < d[1] else (d[1], d[0]) for d in dominoes)
        ans = 0
        for val in count.values():
            ans += val * (val - 1) / 2
        return int(ans)


if __name__ == "__main__":
    print(Solution().numEquivDominoPairs(dominoes=[[1, 2], [2, 1], [3, 4], [5, 6]]))  # 1
