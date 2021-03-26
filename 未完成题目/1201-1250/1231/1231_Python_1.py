from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        pass


if __name__ == "__main__":
    # 6
    print(Solution().maximizeSweetness(sweetness=[1, 2, 3, 4, 5, 6, 7, 8, 9], K=5))

    # 1
    print(Solution().maximizeSweetness(sweetness=[5, 6, 7, 8, 9, 1, 2, 3, 4], K=8))

    # 5
    print(Solution().maximizeSweetness(sweetness=[1, 2, 2, 1, 2, 2, 1, 2, 2], K=2))
