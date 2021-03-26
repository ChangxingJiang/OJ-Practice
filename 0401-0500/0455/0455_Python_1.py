from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        idx1 = 0
        idx2 = 0
        while idx1 < len(g) and idx2 < len(s):
            if g[idx1] <= s[idx2]:
                idx1 += 1
                idx2 += 1
            else:
                idx2 += 1
        return idx1


if __name__ == "__main__":
    print(Solution().findContentChildren([1, 2, 3], [1, 1]))  # 1
    print(Solution().findContentChildren([1, 2], [1, 2, 3]))  # 2
