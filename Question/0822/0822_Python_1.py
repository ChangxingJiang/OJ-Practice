import itertools
from typing import List


class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {fronts[i] for i in range(len(fronts)) if fronts[i] == backs[i]}
        ans = 2001
        for x in itertools.chain(fronts, backs):
            if x not in same:
                ans = min(ans, x)
        return ans if ans != 2001 else 0


if __name__ == "__main__":
    print(Solution().flipgame(fronts=[1, 2, 4, 4, 7], backs=[1, 3, 4, 1, 3]))  # 2
    print(Solution().flipgame(fronts=[1, 1], backs=[1, 2]))  # 2
