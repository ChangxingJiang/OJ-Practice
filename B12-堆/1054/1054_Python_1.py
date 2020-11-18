from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    # [2,1,2,1,2,1]
    print(Solution().rearrangeBarcodes([1, 1, 1, 2, 2, 2]))

    # [1,3,1,3,2,1,2,1]
    print(Solution().rearrangeBarcodes([1, 1, 1, 1, 2, 2, 3, 3]))
