import collections
from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        count = collections.Counter({0: 1})

        ans = 0

        last = 0
        for n in A:
            last = (last + n) % K
            ans += count[last]
            count[last] += 1

        return ans


if __name__ == "__main__":
    print(Solution().subarraysDivByK(A=[4, 5, 0, -2, -3, 1], K=5))  # 7
    print(Solution().subarraysDivByK(A=[5], K=9))  # 0
