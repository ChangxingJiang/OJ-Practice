from typing import List


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxSizeSlices(slices=[1, 2, 3, 4, 5, 6]))  # 10
    print(Solution().maxSizeSlices(slices=[8, 9, 8, 6, 1, 1]))  # 16
    print(Solution().maxSizeSlices(slices=[4, 1, 2, 5, 8, 3, 1, 9, 7]))  # 21
    print(Solution().maxSizeSlices(slices=[3, 1, 2]))  # 3
