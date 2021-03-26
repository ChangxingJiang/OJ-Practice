from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        ans = -1
        N = len(strs)
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                i1, i2 = 0, 0
                while i1 < len(strs[i]) and i2 < len(strs[j]):
                    if strs[i][i1] == strs[j][i2]:
                        i1 += 1
                    i2 += 1
                if i1 == len(strs[i]):
                    break
            else:
                ans = max(ans, len(strs[i]))
        return ans


if __name__ == "__main__":
    print(Solution().findLUSlength(["aba", "cdc", "eae"]))  # 3
    print(Solution().findLUSlength(["aba", "aba", "cac", "cac", "ca"]))  # -1
    print(Solution().findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]))  # 2
