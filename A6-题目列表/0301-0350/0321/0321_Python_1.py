from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        pass


if __name__ == "__main__":
    # [9, 8, 6, 5, 3]
    print(Solution().maxNumber(nums1=[3, 4, 6, 5],
                               nums2=[9, 1, 2, 5, 8, 3],
                               k=5))

    # [6, 7, 6, 0, 4]
    print(Solution().maxNumber(nums1=[6, 7],
                               nums2=[6, 0, 4],
                               k=5))

    # [9, 8, 9]
    print(Solution().maxNumber(nums1=[3, 9],
                               nums2=[8, 9],
                               k=3))
