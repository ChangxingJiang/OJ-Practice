from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        up = 0
        down = 0
        for i in range(len(A) - 1):
            if A[i] < A[i + 1]:
                if down:
                    return False
                up += 1
            elif A[i] > A[i + 1]:
                down += 1
            else:
                return False
        return up > 0 and down > 0


if __name__ == "__main__":
    print(Solution().validMountainArray([2, 1]))  # False
    print(Solution().validMountainArray([3, 5, 5]))  # False
    print(Solution().validMountainArray([0, 3, 2, 1]))  # True
