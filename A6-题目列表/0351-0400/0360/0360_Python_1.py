from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        pass


if __name__ == "__main__":
    #  [3,9,15,33]
    print(Solution().sortTransformedArray(nums=[-4, -2, 2, 4], a=1, b=3, c=5))

    # [-23,-5,1,7]
    print(Solution().sortTransformedArray(nums=[-4, -2, 2, 4], a=-1, b=3, c=5))
