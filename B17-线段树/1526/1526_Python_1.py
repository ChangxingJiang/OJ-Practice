from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minNumberOperations([1, 2, 3, 2, 1]))  # 3
    print(Solution().minNumberOperations([3, 1, 1, 2]))  # 4
    print(Solution().minNumberOperations([3, 1, 5, 4, 2]))  # 7
    print(Solution().minNumberOperations([1, 1, 1, 1]))  # 1
