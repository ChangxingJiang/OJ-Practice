from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numRescueBoats([1, 2], 3))  # 1
    print(Solution().numRescueBoats([3, 2, 2, 1], 3))  # 3
    print(Solution().numRescueBoats([3, 5, 3, 4], 5))  # 4
