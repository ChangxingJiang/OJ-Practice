import collections
from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0

        l, r = 0, 0
        window = collections.Counter()
        while r < len(tree):
            window[tree[r]] += 1
            while len(window) > 2:
                window[tree[l]] -= 1
                if window[tree[l]] == 0:
                    window.pop(tree[l])
                l += 1
            ans = max(ans, r - l + 1)
            r += 1

        return ans


if __name__ == "__main__":
    print(Solution().totalFruit([1, 2, 1]))  # 3
    print(Solution().totalFruit([0, 1, 2, 2]))  # 3
    print(Solution().totalFruit([1, 2, 3, 2, 2]))  # 4
    print(Solution().totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]))  # 5
