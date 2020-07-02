from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left = 0
        right = len(A) - 1
        while left < right:
            mid = (left + right) // 2
            if A[mid] > A[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([0, 1, 0]))  # 1
    print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))  # 1
