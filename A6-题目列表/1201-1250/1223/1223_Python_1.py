from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().dieSimulator(n=2, rollMax=[1, 1, 2, 2, 2, 3]))  # 34
    print(Solution().dieSimulator(n=2, rollMax=[1, 1, 1, 1, 1, 1]))  # 30
    print(Solution().dieSimulator(n=3, rollMax=[1, 1, 1, 2, 2, 3]))  # 181
