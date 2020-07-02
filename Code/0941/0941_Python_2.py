from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        idx1 = 0
        idx2 = len(A) - 1
        while idx1 < idx2:
            if A[idx1] < A[idx1 + 1]:
                idx1 += 1
            elif A[idx2 - 1] > A[idx2]:
                idx2 -= 1
            else:
                return False
        return idx1 != 0 and idx2 != len(A) - 1


if __name__ == "__main__":
    print(Solution().validMountainArray([2, 1]))  # False
    print(Solution().validMountainArray([3, 5, 5]))  # False
    print(Solution().validMountainArray([0, 3, 2, 1]))  # True
