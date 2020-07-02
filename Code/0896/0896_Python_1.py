from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        ans = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if ans > 0:
                    return False
                ans = -1
            elif A[i] < A[i + 1]:
                if ans < 0:
                    return False
                ans = 1
        else:
            return True


if __name__ == "__main__":
    print(Solution().isMonotonic([1, 2, 2, 3]))  # True
    print(Solution().isMonotonic([6, 5, 4, 4]))  # True
    print(Solution().isMonotonic([1, 3, 2]))  # False
    print(Solution().isMonotonic([1, 2, 4, 5]))  # True
    print(Solution().isMonotonic([1, 1, 1]))  # True
