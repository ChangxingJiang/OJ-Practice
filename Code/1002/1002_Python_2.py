import collections
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = collections.Counter(A[0])

        for a in A[1:]:
            ans &= collections.Counter(a)

        return list(ans.elements())


if __name__ == "__main__":
    print(Solution().commonChars(["bella", "label", "roller"]))  # ["e","l","l"]
    print(Solution().commonChars(["cool", "lock", "cook"]))  # ["c","o"]
