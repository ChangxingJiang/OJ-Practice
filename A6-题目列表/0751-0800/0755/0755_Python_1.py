from typing import List


class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        pass


if __name__ == "__main__":
    # [2,2,2,3,2,2,2]
    print(Solution().pourWater(heights=[2, 1, 1, 2, 1, 2, 2], V=4, K=3))

    # [2,3,3,4]
    print(Solution().pourWater(heights=[1, 2, 3, 4], V=2, K=2))

    # [4,4,4]
    print(Solution().pourWater(heights=[3, 1, 3], V=5, K=1))
