from typing import List


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().closestDivisors(8))  # [3,3]
    print(Solution().closestDivisors(123))  # [5,25]
    print(Solution().closestDivisors(999))  # [40,25]
