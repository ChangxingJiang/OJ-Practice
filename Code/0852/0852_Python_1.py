from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                return i


if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([0, 1, 0]))  # 1
    print(Solution().peakIndexInMountainArray([0, 2, 1, 0]))  # 1
