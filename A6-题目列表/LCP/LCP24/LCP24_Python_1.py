from typing import List


class Solution:
    def numsGame(self, nums: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().numsGame([3, 4, 5, 1, 6, 7]))  # [0,0,0,5,6,7]
    print(Solution().numsGame([1, 2, 3, 4, 5]))  # [0,0,0,0,0]
    print(Solution().numsGame([1, 1, 1, 2, 3, 4]))  # [0,1,2,3,3,3]
