from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shortestBridge([[0, 1], [1, 0]]))  # 1
    print(Solution().shortestBridge([[0, 1, 0], [0, 0, 0], [0, 0, 1]]))  # 2
    print(Solution().shortestBridge(
        [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]))  # 1
