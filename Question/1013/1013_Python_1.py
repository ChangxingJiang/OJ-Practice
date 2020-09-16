from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        aim = sum(A) / 3
        if aim % 1 != 0:
            return False

        cut = 0
        total = 0
        for a in A:
            total += a
            if total == aim:
                cut += 1
                total = 0
                if cut >= 3:
                    return True
        else:
            return False


if __name__ == "__main__":
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))  # True
    print(Solution().canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))  # False
    print(Solution().canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))  # True
    print(Solution().canThreePartsEqualSum([18, 12, -18, 18, -19, -1, 10, 10]))  # True
    print(Solution().canThreePartsEqualSum([6, 1, 1, 13, -1, 0, -10, 20]))  # False
    print(Solution().canThreePartsEqualSum([10, -10, 10, -10, 10, -10, 10, -10]))  # True
