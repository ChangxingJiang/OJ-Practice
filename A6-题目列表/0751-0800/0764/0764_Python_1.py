from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().orderOfLargestPlusSign(N=5, mines=[[4, 2]]))

    # 1
    print(Solution().orderOfLargestPlusSign(N=2, mines=[]))

    # 0
    print(Solution().orderOfLargestPlusSign(N=1, mines=[[0, 0]]))
