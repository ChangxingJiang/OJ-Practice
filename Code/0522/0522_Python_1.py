import collections
from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=lambda s: len(s), reverse=True)
        count = collections.Counter(strs)
        visited = []
        for str in strs:
            if count[str] == 1:
                for visit in visited:
                    i1 = 0
                    i2 = 0
                    while i1 < len(str) and i2 < len(visit):
                        if str[i1] == visit[i2]:
                            i1 += 1
                        i2 += 1
                    if i1 == len(str):
                        break
                else:
                    return len(str)
            visited.append(str)
        return -1


if __name__ == "__main__":
    print(Solution().findLUSlength(["aba", "cdc", "eae"]))  # 3
    print(Solution().findLUSlength(["aba", "aba", "cac", "cac", "ca"]))  # -1
    print(Solution().findLUSlength(["aabbcc", "aabbcc", "cb", "abc"]))  # 2
