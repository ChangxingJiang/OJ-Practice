import collections
from typing import List


class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = collections.Counter({0: 1})

        ans = 0
        last = 0
        for n in A:
            last += n
            if last - S in count:
                ans += count[last - S]
            count[last] += 1

        return ans


if __name__ == "__main__":
    print(Solution().numSubarraysWithSum(A=[1, 0, 1, 0, 1], S=2))  # 4
