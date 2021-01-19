import collections
from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        allows = collections.defaultdict(list)
        for allow in allowed:
            allows[allow[0:2]].append(allow[2])

        def dfs1(now_level):
            if len(now_level) == 1:
                return True
            for next_level in dfs2(now_level, 0, ""):
                if dfs1(next_level):
                    return True
            return False

        def dfs2(now_level, i, next_level):
            if i == len(now_level) - 1:
                return [next_level]
            else:
                ch1, ch2 = now_level[i], now_level[i + 1]
                if ch1 + ch2 not in allows:
                    return []
                else:
                    res = []
                    for ch3 in allows[ch1 + ch2]:
                        res.extend(dfs2(now_level, i + 1, next_level + ch3))
                    return res

        return dfs1(bottom)


if __name__ == "__main__":
    print(Solution().pyramidTransition(bottom="BCD", allowed=["BCG", "CDE", "GEA", "FFF"]))  # True
    print(Solution().pyramidTransition(bottom="AABA", allowed=["AAA", "AAB", "ABA", "ABB", "BAC"]))  # False
