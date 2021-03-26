from typing import List


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().stoneGameIII(stoneValue=[1, 2, 3, 7]))  # "Bob"
    print(Solution().stoneGameIII(stoneValue=[1, 2, 3, -9]))  # "Alice"
    print(Solution().stoneGameIII(stoneValue=[1, 2, 3, 6]))  # "Tie"
    print(Solution().stoneGameIII(stoneValue=[1, 2, 3, -1, -2, -3, 7]))  # "Alice"
    print(Solution().stoneGameIII(stoneValue=[-1, -2, -3]))  # "Tie"
