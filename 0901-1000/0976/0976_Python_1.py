from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        else:
            return 0


if __name__ == "__main__":
    print(Solution().largestPerimeter([2, 1, 2]))  # 5
    print(Solution().largestPerimeter([1, 2, 1]))  # 0
    print(Solution().largestPerimeter([3, 2, 3, 4]))  # 10
    print(Solution().largestPerimeter([3, 6, 2, 3]))  # 8
