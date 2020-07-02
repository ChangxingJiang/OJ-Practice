from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        pass


if __name__ == "__main__":
    param = [1, 0, 2, 3, 0, 4, 5, 0]
    Solution().duplicateZeros(param)
    print(param)  # [1,0,0,2,3,0,0,4]

    param = [1, 2, 3]
    Solution().duplicateZeros(param)
    print(param)  # [1,2,3]
