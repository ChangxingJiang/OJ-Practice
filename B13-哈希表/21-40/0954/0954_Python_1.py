from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().canReorderDoubled([3, 1, 3, 6]))  # False
    print(Solution().canReorderDoubled([2, 1, 2, 6]))  # False
    print(Solution().canReorderDoubled([4, -2, 2, -4]))  # True
    print(Solution().canReorderDoubled([1, 2, 4, 16, 8, 4]))  # False
