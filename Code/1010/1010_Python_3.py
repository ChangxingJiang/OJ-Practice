import collections
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count = collections.Counter([t % 60 for t in time])
        ans = 0
        if 0 in count:
            n = count[0]
            ans += n * (n - 1) / 2
        if 30 in count:
            n = count[30]
            ans += n * (n - 1) / 2
        for k, v in count.items():
            if k < 30 and 60 - k in count:
                n = count[60 - k]
                ans += v * n
        return int(ans)


if __name__ == "__main__":
    print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # 3
    print(Solution().numPairsDivisibleBy60([60, 60, 60]))  # 3
