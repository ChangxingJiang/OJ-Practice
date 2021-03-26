import itertools
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        ans = 0
        for pair in itertools.combinations(time, 2):
            remainder = pair[0] + pair[1]
            if remainder == 0 or remainder == 60:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().numPairsDivisibleBy60([30, 20, 150, 100, 40]))  # 3
    print(Solution().numPairsDivisibleBy60([60, 60, 60]))  # 3
