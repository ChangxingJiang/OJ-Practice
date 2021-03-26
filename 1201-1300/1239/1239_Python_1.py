from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr = [s for s in arr if len(s) == len(set(s))]

        stats = []
        for word in arr:
            stat = 0
            for ch in word:
                stat |= 1 << (ord(ch) - 97)
            stats.append(stat)

        def dfs(i, s, x):
            if i == len(arr):
                return x
            res = dfs(i + 1, s, x)
            if not s & stats[i]:
                res = max(res, dfs(i + 1, s | stats[i], x + len(arr[i])))
            return res

        return dfs(0, 0, 0)


if __name__ == "__main__":
    print(Solution().maxLength(arr=["un", "iq", "ue"]))  # 4
    print(Solution().maxLength(arr=["cha", "r", "act", "ers"]))  # 6
    print(Solution().maxLength(arr=["abcdefghijklmnopqrstuvwxyz"]))  # 26
    print(Solution().maxLength(arr=["yy", "bkhwmpbiisbldzknpm"]))  # 0
