from typing import List


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minTransfers([[0, 1, 10], [2, 0, 5]]))  # 2
    print(Solution().minTransfers([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]]))  # 1
