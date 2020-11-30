import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size1, size2 = len(s), len(p)
        if size1 < size2:
            return []

        ans = []
        aim = collections.Counter(p)
        count = collections.Counter()
        for i in range(size2):
            count[s[i]] += 1
        if count == aim:
            ans.append(0)
        for i in range(size1 - size2):
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]
            count[s[i + size2]] += 1
            if count == aim:
                ans.append(i + 1)

        return ans


if __name__ == "__main__":
    print(Solution().findAnagrams("cbaebabacd", "abc"))  # [0,6]
    print(Solution().findAnagrams("abab", "ab"))  # [0,1,2]
