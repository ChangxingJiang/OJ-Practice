from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        size = len(A)
        ans = size
        for k in range(1, 7):
            n1, n2 = 0, 0
            for i in range(size):
                if A[i] != k and B[i] != k:
                    break
                if A[i] == k:
                    n1 += 1
                if B[i] == k:
                    n2 += 1
            else:
                ans = min(ans, size - n1, size - n2)
        return ans if ans < size else -1


if __name__ == "__main__":
    print(Solution().minDominoRotations(A=[2, 1, 2, 4, 2, 2], B=[5, 2, 6, 2, 3, 2]))  # 2
    print(Solution().minDominoRotations(A=[3, 5, 1, 2, 3], B=[3, 6, 3, 3, 4]))  # -1
