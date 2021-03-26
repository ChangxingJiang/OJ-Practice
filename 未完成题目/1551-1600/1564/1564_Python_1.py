from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().maxBoxesInWarehouse(boxes=[4, 3, 4, 1], warehouse=[5, 3, 3, 4, 1]))  # 3
    print(Solution().maxBoxesInWarehouse(boxes=[1, 2, 2, 3, 4], warehouse=[3, 4, 1, 2]))  # 3
    print(Solution().maxBoxesInWarehouse(boxes=[1, 2, 3], warehouse=[1, 2, 3, 4]))  # 1
    print(Solution().maxBoxesInWarehouse(boxes=[4, 5, 6], warehouse=[3, 3, 3, 3, 3]))  # 0
