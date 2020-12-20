from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numTeams(rating=[2, 5, 3, 4, 1]))  # 3
    print(Solution().numTeams(rating=[2, 1, 3]))  # 0
    print(Solution().numTeams(rating=[1, 2, 3, 4]))  # 4
