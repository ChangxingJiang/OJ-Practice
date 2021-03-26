import collections
import math
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        ans = 0
        for k, v in count.items():
            ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans


if __name__ == "__main__":
    print(Solution().numRabbits(answers=[1, 1, 2]))  # 5
    print(Solution().numRabbits(answers=[10, 10, 10]))  # 11
    print(Solution().numRabbits(answers=[]))  # 0
    print(Solution().numRabbits(answers=[1, 0, 1, 0, 0]))  # 5
    print(Solution().numRabbits(answers=[0, 0, 1, 1, 1]))  # 6
