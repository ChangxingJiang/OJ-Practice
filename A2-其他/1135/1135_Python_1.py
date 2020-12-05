from typing import List


class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minimumCost(N=3, connections=[[1, 2, 5], [1, 3, 6], [2, 3, 1]]))  # 6
    print(Solution().minimumCost(N=4, connections=[[1, 2, 3], [3, 4, 4]]))  # -1
